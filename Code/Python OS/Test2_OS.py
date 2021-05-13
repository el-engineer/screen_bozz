# ls /dev/tty*
# I once I included the space after ls this command worked
# run this line with device plugged out
# then run the line again with the device plugged in.
# the difference between the two lists is the device directory
# that should be included in the code.
# raw_input for strings, input for integers

# Import the necessary Librarires
import sys
import serial
import time
import cv2 #imports OpenCV resources
import os #required for creating folders
import RPi.GPIO as GPIO #allows use of GPIO pins by script

# Set the relevant GPIO pins
GPIO.setmode(GPIO.BOARD) #choose BCM or board
GPIO.setwarnings(False)
pins = (18)
GPIO.setup(18, GPIO.OUT) #set physical pin #18 as an output pin, used for TTL signalling

#Connect to the Arduino Mega 2560 over serial connection
print("Opening Serial Connection to Arduino")
ser = serial.Serial("/dev/ttyACM0",250000) #at home using big printer system it is "/dev/tty/USB0" but with actual system in lab it is /dev/tty/ACM0
ser.baudrate=250000
ArduinoBootSerialOutput = 0
while ArduinoBootSerialOutput < 30: #for Marlin 1.1.7 this value should be "<35". For Marlin 1.1.9 the value should be "<30"
    read_ser=ser.readline()
    print(read_ser)
    ArduinoBootSerialOutput += 1
print("Arduino startup complete. Arduino is ready for user input.")

#Once the arduino has had sufficient time to boot up (time taken
#for 35 serial outputs), progress to the rest of the code.

StretchTravelDirection_Str = str("Left")

while True:

    print("")
    print("------------------------------------------------------------")
    print("")
    print("Welcome to the Main Menu.")
    print("To navigate to submenus enter a number and press enter.")
    print("1. Manually type and stream G-Code commands to the arduino.")
    print("2. Automated Camera Scanning")
    print("3. Repeat Dynamic Stretching Section")
    print("4. Ramping Dynamic Threshold Assessment Section: Distance, Speed & Acceleration")
    print("5. Repeat Hybrid of Dynamic & Static Spindle Stretching Section (DDDS)")
    print("9. Change direction of stretches.")
    print("10. Exit")
    print("")
    print("------------------------------------------------------------")
    UserMenuInput = input("")

    #------------------------------------------------------------#
    if UserMenuInput == "1":
        UserMenuInput = str("")
        UserManualGCodeInput = str
        while UserManualGCodeInput != "Main Menu":
            print("------------------------------------------------------------")
            print("")
            print("You have selected option 1. Manually type and stream G-Code commands to the arduino")
            print("Type the desired G-Code command and press enter.")
            print("To return to the Main Menu type 'Main Menu' and press enter.")
            print("")
            print("------------------------------------------------------------")      
            UserManualGCodeInput = input("")
            ArduinoChangeLine = str("\n")
            print(UserManualGCodeInput + " " + ArduinoChangeLine)
            ManualCommandInBytes = bytes((UserManualGCodeInput + " " + ArduinoChangeLine), 'UTF-8')
            ser.write(ManualCommandInBytes)   
