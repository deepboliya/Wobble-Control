
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
    #print("Accelerometer (m/s^2): {}".format(sensor.acceleration))
    #print("Magnetometer (microteslas): {}".format(sensor.magnetic))
    #print("Gyroscope (rad/sec): {}".format(sensor.gyro))
    print(f'Euler angles:- roll:{roll:.4f}, pitch, {pitch:.4f}, yaw {yaw:.4f}')
    #print("Quaternion: {}".format(sensor.quaternion))
    #print("Linear acceleration (m/s^2): {}".format(sensor.linear_acceleration))
    #print("Gravity (m/s^2): {}".format(sensor.gravity))

    time.sleep(0.05)
