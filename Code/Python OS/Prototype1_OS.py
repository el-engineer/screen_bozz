# -----------------------------------------------------------------------#
#																		#
# 	The following script was developed by Dr. Thomas Campbell			#
# 	while working on the creation of a novel XYZ positioning system		#
# 	for use during neurophysiology experiments.  						#
#												              			#
# 	This work was carried out as part of doctoral research being 		#
#	undertaken at University College Dublin 							#
# 	under the supervision of Prof. James FX Jones. 						#
#	 																	#
# 	I would sincerely like to thank the extended maker community 		#
# 	for their generosity in sharing knowledge with myself and others	#
# 	through various online platforms. Your generosity has made the 		#
#	maker space far more accessible for all.							#
#																		#
# 	For queries regarding this code please email me at:					#
# 																		#
# 	thomas.campbell@ucd.ie												#
#							     										#
# -----------------------------------------------------------------------#

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
import cv2  # imports OpenCV resources
import os  # required for creating folders
import RPi.GPIO as GPIO  # allows use of GPIO pins by script

# Set the relevant GPIO pins
GPIO.setmode(GPIO.BOARD)  # choose BCM or board
GPIO.setwarnings(False)
pins = (18)
GPIO.setup(18, GPIO.OUT)  # set physical pin #18 as an output pin, used for TTL signalling

# Connect to the Arduino Mega 2560 over serial connection
print("Opening Serial Connection to Arduino")
ser = serial.Serial("/dev/ttyACM0",
                    250000)  # at home using big printer system it is "/dev/tty/USB0" but with actual system in lab it is /dev/tty/ACM0
ser.baudrate = 250000
ArduinoBootSerialOutput = 0
while ArduinoBootSerialOutput < 30:  # for Marlin 1.1.7 this value should be "<35". For Marlin 1.1.9 the value should be "<30"
    read_ser = ser.readline()
    print(read_ser)
    ArduinoBootSerialOutput += 1
print("Arduino startup complete. Arduino is ready for user input.")

# Once the arduino has had sufficient time to boot up (time taken
# for 35 serial outputs), progress to the rest of the code.

StretchTravelDirection_Str = str("Left")

while True:

    print("")
    print("------------------------------------------------------------")
    print("")
    print("Welcome to the Main Menu.")
    print("To navigate to submenus enter a number and press enter.")
    print("1. Manually type and stream G-Code commands to the arduino.")
    print("2. iphone 7, 8")
    print("3. iphone 7+, 8+")
    print("10. Exit")
    print("")
    print("------------------------------------------------------------")
    UserMenuInput = input("")

    # ------------------------------------------------------------#
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

            # ------------------------------------------------------------#

    elif UserMenuInput == "2":
        UserMenuInput = str("")
        iPhone7GCodeInput = str

        print("Perform an auto home before starting? (Y/N) ")
        iPhone7GCodeInput = input("")
        if iPhone7GCodeInput in ListofPositiveResponses:
            HomingCommandInBytes = bytes(("G28" + " \n"), 'UTF-8')
            ser.write(HomingCommandInBytes)
            print("Homing. This will take approximately 2 minutes. ")
            time.sleep(120)

        while iPhone7GCodeInput != "Main Menu":
            print("------------------------------------------------------------")
            print("")
            print("You have selected option 2. iphone 7, 8")
            print("Type the desired G-Code command and press enter.")
            print("To return to the Main Menu type 'Main Menu' and press enter.")
            print("")
            print("------------------------------------------------------------")
            iPhone7GCodeInput = ("") #Insert the tasks for robot to complete
            ArduinoChangeLine = str("\n")
            print(iPhone7GCodeInput + " " + ArduinoChangeLine)
            ManualCommandInBytes = bytes((iPhone7GCodeInput + " " + ArduinoChangeLine), 'UTF-8')
            ser.write(ManualCommandInBytes)



    # ------------------------------------------------------------#

    elif UserMenuInput == "3":  # this is the spindle stretching section
        print("")
        print("------------------------------------------------------------")
        print("")
        print("Welcome to the Repeat Dynamic Stretching Section.")
        print("")
        print("------------------------------------------------------------")
        print("")

        ListofPositiveResponses = ["Y", "y", "Yes", "yes"]
        ListofNegativeResponses = ["N", "n", "No", "no"]

        print("Perform an auto home before starting? (Y/N) ")
        UserManualGCodeInput = input("")
        if UserManualGCodeInput in ListofPositiveResponses:
            HomingCommandInBytes = bytes(("G28" + " \n"), 'UTF-8')
            ser.write(HomingCommandInBytes)
            print("Homing. This will take approximately 2 minutes. ")
            time.sleep(120)

        print("Move to the default starting position of X150.0 Y90.0 Z70.0? (Y/N)  ")
        UserManualGCodeInput = input("")
        if UserManualGCodeInput in ListofPositiveResponses:
            MoveToSpindleStartingPositionInBytes = bytes(("G1X140Y95Z10" + " \n"), 'UTF-8')
            ser.write(MoveToSpindleStartingPositionInBytes)
            print("Moving to spindle starting position. This will take approximately 1 minutes. ")
            time.sleep(60)

        print("")
        print("------------------------------------------------------------")
        print("Maximum travel speed will remain constant at 30mm/s. ")
        ChangeSpeedTo30_Str = str("M203 X30 \n")
        ChangeSpeedTo30_Bytes = bytes(ChangeSpeedTo30_Str, 'UTF-8')
        ser.write(ChangeSpeedTo30_Bytes)
        print("Acceleration will constant remain at 100mm/s^2. ")
        ChangeAccelTo100_Str = str("M204 T100 \n")
        ChangeAccelTo100_Bytes = bytes(ChangeAccelTo100_Str, 'UTF-8')
        ser.write(ChangeAccelTo100_Bytes)

        print("Please manually enter G-Code commands to perform fine")
        print("positioning of the hook.")
        print("Once the hook is in place, please enter 'Continue' to")
        print("proceed to the next step.")
        print("To return to the main menu, enter 'Main Menu'. ")
        print("------------------------------------------------------------")
        print("")

        UserManualGCodeInput = str("")
        ListOfWaysOut = ["Main Menu", "main menu", "Main menu", "main Menu", "Continue", "continue"]

        while UserManualGCodeInput not in ListOfWaysOut:
            UserManualGCodeInput = input("")
            ArduinoChangeLine = str("\n")
            print("You entered " + UserManualGCodeInput + ". " + ArduinoChangeLine)
            ManualCommandInBytes = bytes((UserManualGCodeInput + " " + ArduinoChangeLine), 'UTF-8')
            ser.write(ManualCommandInBytes)

        if UserManualGCodeInput in ["Continue", "continue"]:
            print("")
            print("------------------------------------------------------------")
            print("")
            print("Hook in position, continuing to stretch settings. ")
            print("")
            PullsPerCycle_Str = input(
                "How many pulls per cycle? (Maximum 8) ")  # maximum of 8 because the standard buffer size for queued moves in marlin is 16. if there are 8 pulls there also need to be 8 returns to starting position, hence 8 is max.
            PullsPerCycle_Int = int(PullsPerCycle_Str)
            print("")
            TotalNumberofCycles_Str = input("How many cycles to carry out? ")
            TotalNumberofCycles_Int = int(TotalNumberofCycles_Str)
            print("")
            TravelDistancePerPull_Str = input("How far should the hook travel during one pull? (value in millimeters) ")

            # some declaration of variables before tugging!

            if StretchTravelDirection_Str == "Left":
                PullCommand_Str = str("G1X-" + TravelDistancePerPull_Str + " \n")
                PullCommand_Bytes = bytes(PullCommand_Str, 'UTF-8')
                RestCommand_Str = str("G1X+" + TravelDistancePerPull_Str + " \n")
                RestCommand_Bytes = bytes(RestCommand_Str, 'UTF-8')

            if StretchTravelDirection_Str == "Right":
                PullCommand_Str = str("G1X+" + TravelDistancePerPull_Str + " \n")
                PullCommand_Bytes = bytes(PullCommand_Str, 'UTF-8')
                RestCommand_Str = str("G1X-" + TravelDistancePerPull_Str + " \n")
                RestCommand_Bytes = bytes(RestCommand_Str, 'UTF-8')

            ConvertToRelativeCoordinates_Str = str("G91 \n")
            ConvertToRelativeCoordinates_Bytes = bytes(ConvertToRelativeCoordinates_Str, 'UTF-8')
            ConvertToAbsoluteCoordinates_Str = str("G90 \n")
            ConvertToAbsoluteCoordinates_Bytes = bytes(ConvertToAbsoluteCoordinates_Str, 'UTF-8')

            ShortBeepSound = str("M300 P10")
            ShortBeepSoundBytes = bytes((ShortBeepSound + " \n"), 'UTF-8')
            LongBeepSound = str("M300 P1000")
            LongBeepSoundBytes = bytes((LongBeepSound + " \n"), 'UTF-8')

            CurrentPull = int(0)
            MaximumPull = int(PullsPerCycle_Int)
            CurrentCycle_Int = int(1)
            MaximumCycle = int(TotalNumberofCycles_Int)

            # logic to pull and relax the lumbrical in cycles
            ser.write(ConvertToRelativeCoordinates_Bytes)  # swap to relative coordinates is G91
            while CurrentCycle_Int < (MaximumCycle + 1):

                while CurrentPull < MaximumPull:
                    CurrentPull = (CurrentPull + 1)
                    ser.write(PullCommand_Bytes)
                    GPIO.output(18, 1)  # TTL output high
                    GPIO.output(18, 0)  # TTL output low
                    ser.write(RestCommand_Bytes)
                CurrentPull = (0)  # resets the current pull back to zero

                RemainingCycles_Int = int(MaximumCycle - CurrentCycle_Int)
                RemainingCycles_Str = str(RemainingCycles_Int)
                CurrentCycle_Str = str(CurrentCycle_Int)
                print("Cycle " + CurrentCycle_Str + " complete. " + RemainingCycles_Str + " cycles remaining.")
                CurrentCycle_Int = (CurrentCycle_Int + 1)  # having completed a cycle of pulls, increases cycle by one
                time.sleep(1.0)
                ser.write(ShortBeepSoundBytes)
                time.sleep(1.0)

            ser.write(ConvertToAbsoluteCoordinates_Bytes)  # swap back to absolute coordinates = G90
            print("Maximum travel speed has been reset to 100mm/s. ")
            ChangeSpeedTo100_Str = str("M203 X100 \n")
            ChangeSpeedTo100_Bytes = bytes(ChangeSpeedTo100_Str, 'UTF-8')
            ser.write(ChangeSpeedTo100_Bytes)
            print("Acceleration has been reset to 1000mm/s^2. ")
            ChangeAccelTo1000_Str = str("M204 T1000 \n")
            ChangeAccelTo1000_Bytes = bytes(ChangeAccelTo1000_Str, 'UTF-8')
            ser.write(ChangeAccelTo1000_Bytes)
            print("All Cycles completed. Returning to Main Menu.")
            # exit to main menu

            # Change acceleration for travel moves = M204 TVALUE, check current settings with M503
            # G1X-1, G1X1





        elif UserManualGCodeInput in ["Main Menu", "main menu"]:
            print("You chose to return to the main menu. Returning to main menu. ")


    # ------------------------------------------------------------#

    elif UserMenuInput == "10":
        print("Exiting script and returning to Terminal.")
        ser.close()
        quit()

    # ------------------------------------------------------------#

    elif UserMenuInput != "1" and UserMenuInput != "2" and UserMenuInput != "3" and UserMenuInput != "4" and UserMenuInput != "5" and UserMenuInput != "10":
        print("You entered an invalid input. Please try again.")

    # ------------------------------------------------------------#

    # UserInput = raw_input("Enter the desired G-Code command and press the enter key.")
    # print(UserInput)
    # serial.write(UserInput)

# now it is 500. Whoops 735 now
