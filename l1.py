import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setwarnings(False)

class Lights(object):
    def __init__(self):
        pass

    def lights_on(self):
        GPIO.output(11, GPIO.HIGH)

    def lights_off(self):
		GPIO.output(11, GPIO.LOW)

    def show_off(self):
		GPIO.output(11, GPIO.HIGH)        	
		time.sleep(1)
		GPIO.output(11, GPIO.LOW)
		time.sleep(1)