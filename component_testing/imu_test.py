#!usr/bin/env python
import time
import board 
import busio 
import adafruit_bno055

#import machine 

#i2c = machine.I2C(board.SCL, board.SDA)
# Use these lines for I2C
#print(board.SCL, board.SDA)
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_bno055.BNO055_I2C(i2c)

# User these lines for UART
# uart = busio.UART(board.TX, board.RX)
# sensor = adafruit_bno055.BNO055_UART(uart)

while True:

    yaw, roll, pitch = sensor.euler
    #print(yaw, roll, pitch)
    #print("Temperature: {} degrees C".format(sensor.temperature))
    # Assuming sensor.acceleration returns a tuple (x, y, z)
    #print("Accelerometer (m/s^2): x={:.4f}, y={:.4f}, z={:.4f}".format(*sensor.acceleration))

    #print(f"Accelerometer (m/s^2): {sensor.acceleration:.4f}")
    #print("Magnetometer (microteslas): {}".format(sensor.magnetic))
    #print(f"Gyroscope (rad/sec): {sensor.gyro}")
    print("Gyro (m/s^2): q={:.4f}, p={:.4f}, r={:.4f}".format(*sensor.gyro))
    print(f'Euler angles:- roll:{roll:.4f}, pitch, {pitch:.4f}, yaw {yaw:.4f}')
    #print("Quaternion: {}".format(sensor.quaternion))
    # Assuming sensor.acceleration returns a tuple (x, y, z)
    #print("Linear accn (m/s^2): x={:.4f}, y={:.4f}, z={:.4f}".format(*sensor.linear_acceleration))

    #print(f"Linear acceleration (m/s^2): {sensor.linear_acceleration:.4f}")
    #print("Gravity (m/s^2): {}".format(sensor.gravity))

    time.sleep(0.05)
