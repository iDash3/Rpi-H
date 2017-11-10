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
                print('Lights on')

        def lights_off(self):
                GPIO.output(11, GPIO.LOW)
                print('Lights off')
