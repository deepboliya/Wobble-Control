#!/usr/bin/env python
'''
Pin out
GPIO 22 Servo 1
GPIO 23 Servo 2
'''

import pigpio
import time

pi =  pigpio.pi()                    # object to access class pigpio
#pi.set_mode(22, pigpio.OUTPUT)
#pi.set_mode(23, pigpio.OUTPUT)

#pi.set_servo_pulsewidth(22, 800)  # set_servo_pulsewidth(pin_no, pulse_width in ms)
#pi.set_servo_pulsewidth(23, 800)
#time.sleep(2)
#Servo at pin 23 not working
for i in range(3):
    pi.set_servo_pulsewidth(22, 1900) # set_servo_pulsewidth(pin_no, pulse_width in ms)
    pi.set_servo_pulsewidth(23, 1900)
    time.sleep(1)

    pi.set_servo_pulsewidth(22, 1100) # set_servo_pulsewidth(pin_no, pulse_width in ms)
    pi.set_servo_pulsewidth(23, 1100)
    time.sleep(1)


    pi.set_servo_pulsewidth(22, 1500) # 900set_servo_pulsewidth(pin_no, pulse_width in ms)
    pi.set_servo_pulsewidth(23, 1500) #1100rear
    time.sleep(1)


pi.stop()
