import RPi.GPIO as GPIO
 
# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)
 
# set up the GPIO channels - one input and one output
GPIO.setup(11, GPIO.IN)
GPIO.setup(12, GPIO.OUT)
 
# input from pin 11
input_value = GPIO.input(11)
 
# output to pin 12
GPIO.output(12, GPIO.HIGH)
 
# the same script as above but using BCM GPIO 00..nn numbers
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
GPIO.setup(18, GPIO.OUT)
input_value = GPIO.input(17)
GPIO.output(18, GPIO.HIGH)
