#Import the necessary libraries
import RPi.GPIO as GPIO 
import time GPIO.setmode(GPIO.BCM)

#Setup pin 18 as an output 
GPIO.setmode(GPIO.BCM) 
GPIO.setup(18, GPIO.OUT)

# An actValve function turns the valve on for 5 sec and off for 10 sec.
def actValve(Pin):
	while True: 
	GPIO.output(18, GPIO.HIGH)
	print(”Solenoid Valve is opened to irrigate.")
	time.sleep(5) #waiting time in seconds 
	GPIO.output(18, GPIO.LOW)
	print(”Solenoid Valve is closed.")
	time.sleep(10)

# An actValve function is executed, then the GPIO is cleaned up.
actValve(18)
GPIO.cleanup()
