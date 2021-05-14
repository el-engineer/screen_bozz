import serial
import time

#Connect to the Arduino Mega 2560 over serial connection
if __name__ == '__main__':
  ser = serial.Serial("COM6",250000, timeout=1)
  ser.flush()

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

print("process completed")
