import RPi.GPIO as GPIO  
import time 

channel = 4 

GPIO.setmode (GPIO.BCM)
GPIO.setup (channel, GPIO.OUT)


def motor_on (pin) :
    GPIO.out (pin, GPIO.HIGH)

def motor_off (pin) : 
    GPIO.output (pin, GPIO.LOW)

    if_name_ == '_main_' :
    try:
        motor_on (channel)
        time.sleep (1)
        motor_off (channel)
        time.sleep (1)
        GPIO.cleanup ()
    except KeyboardInterrupt:
        GPIO.cleanup ()
        pass