#!/usr/bin/env python
import time
import pigpio
import board 
import busio 
import adafruit_bno055
# import pandas as pd
import numpy as np
import os

pi = pigpio.pi()
pi.set_mode(13,pigpio.OUTPUT)  #PWMA 13   7
pi.set_mode(17,pigpio.OUTPUT)  #AIN2 17   11
pi.set_mode(18,pigpio.OUTPUT)  #AIN1 18   12
pi.set_mode(27,pigpio.OUTPUT)  #STBY 27   13



class spbot():
    t_start = time.time()
    t_runtime = 15
    i2c = busio.I2C(board.SCL, board.SDA)
    imu_bno055 = adafruit_bno055.BNO055_I2C(i2c)

    def __init__(self):
        return

    def get_body_rates(self):
        return self.imu_bno055.gyro

    def get_orientation(self):
        return self.imu_bno055.euler

    def get_linear_acceleration(self):
        return self.imu_bno055.acceleration

    def forward(self,duty):
        pi.write(27,1)
        pi.write(18,1)
        pi.write(17,0)
        pi.set_PWM_dutycycle(13,duty)
        return

    def backward(self,duty):
        pi.write(27,1)
        pi.write(18,0)
        pi.write(17,1)
        pi.set_PWM_dutycycle(13,duty)
        return

    def set_servo_angle(self, value):
        # Value belongs to [-1, 1]. -1 is leftmost point the pendulum can reach, +1 is rightmost
        # The pulse value can vary from 1200 to 1800 with 1500 as middle.
        max_deviation = 300
        print(f"Angle value:{value}")
        pi.set_servo_pulsewidth(22, 1500 + value*max_deviation)
        pi.set_servo_pulsewidth(23, 1500 + value*max_deviation) 
        return
    
    def gpio_cleanup(self):
        pi.write(18,0)
        pi.write(17,0)
        pi.set_PWM_dutycycle(13, 0)
        pi.write(27,0)
        pi.stop()
            
if __name__ == "__main__":
    spbot_ = spbot()
    data_time_stamped = []

    while(1):
        time.sleep(0.05)
        current_time = time.time() - spbot_.t_start
        if current_time > spbot_.t_runtime :
            break

        spbot_.forward(120)
        yaw, roll, pitch = spbot_.get_orientation()
        q, p, r = spbot_.get_body_rates()
        try:
             value = - 1 * roll / 20
        except:
             continue
        value = max(min(1, value), -1) # Constrain between -1 and +1
        spbot_.set_servo_angle(value)
        data_time_stamped.append([current_time, yaw, pitch, roll, p, q, r])

    print(data_time_stamped)
    filename = 'bot_ypr_pqr_data_forward_stabilized'
    extension = '.txt'
    index = 1

    # Check if the file exists and create a new file name with incrementing number if it does
    while os.path.exists(f"{filename}{index}{extension}"):
        index += 1

    # Saving the array to a text file
    np.savetxt(f"{filename}{index}{extension}", data_time_stamped, fmt='%.2f', header='Timestamp Yaw Pitch Roll p q r', comments='')

    spbot_.gpio_cleanup()

