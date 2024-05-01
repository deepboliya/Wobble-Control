import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(22,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
r_pwm = 32 #pwm_a
r1 = 22 #servo1
r2 = 23 #servo2
'''
GPIO.setup(33,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
l_pwm = 33 #pwm_b
l1 = 22 #inb1
l2 = 24 #inb2
#GPIO.setup(16,GPIO.OUT)
standby = 16

GPIO.output(standby,1)

GPIO.output(r1,1)
GPIO.output(r2,0)
GPIO.output(l1,1)
GPIO.output(l2,0)
'''
leftmotor = GPIO.PWM(r1,50)
rightmotor = GPIO.PWM(r2,50)

leftmotor.start(10)
rightmotor.start(10)

leftmotor.ChangeDutyCycle(7.5)
rightmotor.ChangeDutyCycle(7.5)
time.sleep(2)
leftmotor.ChangeDutyCycle(7)
rightmotor.ChangeDutyCycle(8)
time.sleep(2)
leftmotor.stop()
rightmotor.stop()
