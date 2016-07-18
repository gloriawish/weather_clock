import RPi.GPIO as GPIO
pin = 24

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(pin,GPIO.OUT)

GPIO.output(pin,GPIO.LOW)
GPIO.output(pin,GPIO.HIGH)
