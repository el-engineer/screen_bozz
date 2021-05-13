import serial

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
