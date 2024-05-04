#!/usr/bin/env python
import time
import pigpio
import board 
import busio 
import adafruit_bno055
import pandas as pd
import numpy as np

pi = pigpio.pi()
pi.set_mode(13,pigpio.OUTPUT)  #PWMA 13   7
pi.set_mode(17,pigpio.OUTPUT)  #AIN2 17   11
pi.set_mode(18,pigpio.OUTPUT)  #AIN1 18   12
pi.set_mode(27,pigpio.OUTPUT)  #STBY 27   13



class spbot():
    t_start = time.time()
    t_runtime = 1
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

        spbot_.forward(50)
        yaw, roll, pitch = spbot_.get_orientation()
        data_time_stamped.append([current_time, yaw, pitch, roll])

    print(data_time_stamped)
    store_data_time_stamped = np.array(data_time_stamped)
    df = pd.DataFrame(data_time_stamped, columns = ['time', 'yaw', 'pitch', 'roll'])
    df.to_csv('robot_data.csv', index=True)

    spbot_.gpio_cleanup()
