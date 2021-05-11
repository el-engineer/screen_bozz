#-----------------------------------------------------------------------#
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
#-----------------------------------------------------------------------#

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
        
    #------------------------------------------------------------#
            
    elif UserMenuInput == "2":
        print("------------------------------------------------------------")
        print("")
        print("Welcome to the automated camera scanning menu.")
        print("Please note that this section does not yet support Z stacking.")
        print("First the user must to define the area to be imaged.")
        print("A rectangular area to be imaged which will be defined by the boundaries of X1Y1, X2Y2, and X3Y3.")
        print("")
        print("  X1Y1-------X2Y2 ")
        print("  -             - ")
        print("  -             - ")
        print("  -             - ")
        print("  -             - ")
        print("  -----------X3Y3 ")
        print("")
        print("While entering these coordinates, should the user wish to return to the Main Menu at any time type 'Main Menu' and press enter.")
        print("")
        print("------------------------------------------------------------")
        #User Coordinate Input Section
        print("Please type the following coordinates (mm) correct to three decimal places, pressing enter after each coordinate.")
        
        print("X1 Coordinate: (Max 430.0)")
        UserX1CoordinateInputStr = input("")
        UserX1CoordinateInputFloat = float(UserX1CoordinateInputStr)
        
        print("Y1 Coordinate: (Max 150.0)")        
        UserY1CoordinateInputStr = input("")
        UserY1CoordinateInputFloat = float(UserY1CoordinateInputStr)
        
        print("X2 Coordinate: (Max 430.0)")
        UserX2CoordinateInputStr = input("")
        UserX2CoordinateInputFloat = float(UserX2CoordinateInputStr)
        
        print("Y2 Coordinate: (Max 150.0)")
        UserY2CoordinateInputStr = input("")
        UserY2CoordinateInputFloat = float(UserY2CoordinateInputStr)
                
        print("X3 Coordinate: (Max 430.0)")
        UserX3CoordinateInputStr = input("")
        UserX3CoordinateInputFloat = float(UserX3CoordinateInputStr)
                
        print("Y3 Coordinate: (Max 150.0)")
        UserY3CoordinateInputStr = input("")
        UserY3CoordinateInputFloat = float(UserY3CoordinateInputStr)
        
        print("")                        
        print("A node is a coordinate at which an image will be taken.")
        print("Please specify the distance between nodes in the X and Y directions.")
        print("X-axis spacing between nodes (mm):")
        UserXNodeSpacingStr = input("")
        UserXNodeSpacingFloat = float(UserXNodeSpacingStr)
        print("Y-Axis spacing between nodes (mm):")
        UserYNodeSpacingStr = input("")
        UserYNodeSpacingFloat = float(UserYNodeSpacingStr)
        
        print("")
        print("Upon arriving at a new node, it may take some time for vibration to subside.")
        print("How many milliseconds should the device wait before taking an image?")
        UserNodeInitialDelayStr = input("")
        UserNodeInitialDelayFloat = float(UserNodeInitialDelayStr)
        
        print("")
        print("Having captured an image at a node, how many milliseconds should the device wait before moving to the next node?")
        UserNodePostDelayStr = input("")
        UserNodePostDelayFloat = float(UserNodePostDelayStr)
        
        print("")
        UserDefinedFolderNameStr = input("Please enter the name of the folder in which these images will be stored. This folder will be placed on the desktop: ")   #User needs to define a folder title in which the images will be stored. This folder is stored onthe desktop
        
        print("")
        UserDefinedPixelsPerMM_Str = input("Please enter the number of pixels per mm. This is required to generate the coordinates of images in pixels for the TextConfiguration file required for the ImageJ (Fiji) stitching plugin. ") #user needs to define the number of pixels per mm. this value is required in order to generate the test file which has all of the file coordinates in it.
        UserDefinedPixelsPerMM_Float = float(UserDefinedPixelsPerMM_Str)
        UserDefinedPixelsPerMM_Round = round(UserDefinedPixelsPerMM_Float, 3)
        UserDefinedPixelsPerMM_Str = str(UserDefinedPixelsPerMM_Round)
        
        print("")
        print("------------------------------------------------------------")
        print("")
        print("User has defined the following criteria for Automated Camera Scanning.")
        print("X1Y1","=","(",UserX1CoordinateInputFloat,",",UserY1CoordinateInputFloat,")")
        print("X2Y2","=","(",UserX2CoordinateInputFloat,",",UserY2CoordinateInputFloat,")")
        print("X3Y3","=","(",UserX3CoordinateInputFloat,",",UserY3CoordinateInputFloat,")")
        print("X distance between nodes =",UserXNodeSpacingFloat)
        print("Y distance between nodes =",UserYNodeSpacingFloat)
        print("Upon arriving at a new node, the device will wait",UserNodeInitialDelayFloat,"ms before taking an image.")
        print("Having taken an image at a node, the device will wait",UserNodePostDelayFloat,"ms before moving to the next node.")
        print("Images and TileConfiguration file will be stored in a folder on the desktop called"+" '"+UserDefinedFolderNameStr+ "'" +".")
        print("Pixels per mm = " + UserDefinedPixelsPerMM_Str + ".")
        print("")
        print("------------------------------------------------------------")
        
        print("")
        print("Enter Y to confirm the above settings or N to specify new settings.")
        ConfirmAutomatedCameraScanning = input("")
        if ConfirmAutomatedCameraScanning == "Y":
            
            #Create the folder that the images will be stored in
            Path = "/home/pi/Desktop/"
            os.mkdir(Path+UserDefinedFolderNameStr) #creates a folder at /home/pi/Desktop/ which is called UserDefinedFolderNameStr
            DirectoryToStoreImages = str(Path+UserDefinedFolderNameStr+"/")
            
            #Create the TileConfiguration.txt file in which the image coordinates (in pixels) are stored and write the initial lines of this document
            DirectoryToStoreTileConfiguration = str(Path+UserDefinedFolderNameStr+"/")
            f= open(DirectoryToStoreTileConfiguration+"TileConfiguration.txt","w+")   #this will create a file called TileConfiguration.txt use w+ to write a file, use a+ to append a file (continually add lines to the file)
            f.write("#first define the number of dimensions, 2 for XY scanning, 3 for XYZ scanning") #write a line
            f.write("\n") #this makes it skip a line
            f.write("dim=2")
            f.write("\n")
            f.write("\n")
            f.write("#Define the image coordinates")
            f.write("\n")
            f.write("#ImageFileName.FileExtension; ; (XCoordinatesInPixels,YCoordinatesInPixels)")
            f.write("\n")
            f.close() #this closes the instance of the created file.

            
            
            #Section where the XY area to scan is deduced from users X1Y1 X2Y2 X3Y3 inputs           
            MinimumXBoundaryFloat = min(UserX1CoordinateInputFloat, UserX2CoordinateInputFloat, UserX3CoordinateInputFloat) #X-Nodes first. Get the largest X-distance from the specified nodes
            MaximumXBoundaryFloat = max(UserX1CoordinateInputFloat, UserX2CoordinateInputFloat, UserX3CoordinateInputFloat) #Defines the min() and max() of the specified X values
            LengthofXBoundaryFloat = float(MaximumXBoundaryFloat - MinimumXBoundaryFloat)
            NumberofNodesinXBoundary = int(LengthofXBoundaryFloat / UserXNodeSpacingFloat)                                #Find out how many times the specified x-node distance divides into the largest X-distance
            
            MinimumYBoundaryFloat = min(UserY1CoordinateInputFloat, UserY2CoordinateInputFloat, UserY3CoordinateInputFloat) #Y-Nodes second. Get the largest Y-distance from the specified nodes
            MaximumYBoundaryFloat = max(UserY1CoordinateInputFloat, UserY2CoordinateInputFloat, UserY3CoordinateInputFloat) #Defines the min() and max() of the specified Y values
            LengthofYBoundaryFloat = float(MaximumYBoundaryFloat - MinimumYBoundaryFloat)
            NumberofNodesinYBoundary = int(LengthofYBoundaryFloat / UserYNodeSpacingFloat)                                #Find out how many times the specified y-node distance divides into the largest Y-distance
            
            
            #This section will calculate the duration of the scan 
            TotalNumberofNodesinXYPlane = int(NumberofNodesinXBoundary * NumberofNodesinYBoundary)
            TimeToScanOneNodeInMilliseconds = float(UserNodeInitialDelayFloat + UserNodePostDelayFloat)
            TimeToScanOneNodeInSecondsFloat = (TimeToScanOneNodeInMilliseconds/1000)
            TotalScanTimeInSeconds = (TotalNumberofNodesinXYPlane*TimeToScanOneNodeInSecondsFloat)
            TotalScanTimeInHours = round((TotalScanTimeInSeconds / 3600),1)
                   
                   
            #Feedback to user to indicate that the scan is starting and approximately how long it will take.
            print("------------------------------------------------------------")
            print("")
            print("You entered Y.")
            print("This scan will take approximately",TotalScanTimeInHours,"hours to complete.")
            print("Starting scan in...")
            time.sleep(1)
            print("3...")
            ShortBeepSound = str("M300 P10")
            ShortBeepSoundBytes = bytes((ShortBeepSound + " \n"), 'UTF-8')
            LongBeepSound = str("M300 P1000")
            LongBeepSoundBytes = bytes((LongBeepSound + " \n"), 'UTF-8')
            ser.write(ShortBeepSoundBytes)
            time.sleep(1)
            print("2...")
            ser.write(ShortBeepSoundBytes)
            time.sleep(1)
            print("1...")
            ser.write(ShortBeepSoundBytes)
            time.sleep(1)
            print("Beginning now!")
            ser.write(LongBeepSoundBytes)
            print("")
            print("------------------------------------------------------------")
            
            #Scanning Logic: First home, pi waits to hear from the arduino that it has reached home.
            ser.write(bytes("G28\n", 'UTF-8'))  #return to home
            print("Returning to home position.")
            time.sleep(180)
            #while read_ser != (b'X:0.00 Y:150.00 Z:430.00 E:0.00 Count X:0 Y:60000 Z:172000\n'): #this while loop makes the pi listen for the arduino's signal that it has completed homing.
            #    read_ser=ser.readline()
            #    #print(read_ser)
            #    ser.flush()
            #    #time.sleep(1)
            
            CameraScanXStartingPointStr = str((round(MinimumXBoundaryFloat,3))) #Generates a minimum X and minimum Y coordinate from user inputs, rounded to three decimal places
            CameraScanYStartingPointStr = str((round(MinimumYBoundaryFloat,3))) #Generates a minimum X and minimum Y coordinate from user inputs rounded to three decimal places
            CameraScanStartingPointStr = str("G1X" + CameraScanXStartingPointStr + "Y" + CameraScanYStartingPointStr + "Z10\n") #Generates a string "G1X-Y-Z10\n"
            CameraScanStartingPointInBytes = bytes(CameraScanStartingPointStr, 'UTF-8') #converts above string to bytes
            ser.write(CameraScanStartingPointInBytes) #sends Gcode to the arduino to move to XminYMinZ10 i.e. our starting point.
            print("Travelling to starting position.")
            time.sleep(120)
            
            #define the variables to watch for
            #CameraScanXStartingPoint_StrToListenforStartingPoint = str((round(MinimumXBoundaryFloat,2)))
            #CameraScanYStartingPoint_StrToListenforStartingPoint = str((round(MinimumYBoundaryFloat,2)))
            #define the string to watch for
            #EchoStartingPointReached = str("X:"+ CameraScanXStartingPoint_StrToListenforStartingPoint + " Y:" + CameraScanYStartingPoint_StrToListenforStartingPoint + " Z:10.00 E:0.00 Count X:0 Y:60000 Z:172000\n")
            #EchoStartingPointReached_Bytes = bytes(EchoStartingPointReached, 'UTF-8')
            #read_ser=ser.readline()
            #start listening for start point reached
            #while True: #read_ser != EchoStartingPointReached_Bytes: #this while makes the pi listen for the arduino's signal that it has reached the starting point
            #    read_ser=ser.readline()
            #    print(read_ser)
            #    ser.flush()
            #    #time.sleep(1)
            #time.sleep(5) #wait 1 second before moving on with the code
            

            #in this section we define variables used for the scanning loop
            #initial X node in each row is node 1, max node is whatever the max length divided by the x node spacing is.
            #Current X node is 1 and Y node is 1
            MinXNode = int(1)
            MaxXNode = int(NumberofNodesinXBoundary)
            MinYNode = int(1)
            MaxYNode = int(NumberofNodesinYBoundary)
            CurrentXNode = int(1) #initially set this to 1 as camera is in the starting position
            CurrentYNode = int(1) #initially set this to 1 as camera is in the starting position
            
            #now starts the logic loop. keep on scanning until Current Y node is greater than max Y node.
            while CurrentYNode <= (MaxYNode+1):
                
                NewYCoordinate_Round = round((MinimumYBoundaryFloat+((CurrentYNode-1)*UserYNodeSpacingFloat)), 3)
                NewYCoordinate_Str_Hidden = str(NewYCoordinate_Round)
                NewYCoordinateStr = str("G1Y"+NewYCoordinate_Str_Hidden+"\n")
                
                NewXCoordinate_Round = round((MinimumXBoundaryFloat+((CurrentXNode-1)*UserXNodeSpacingFloat)), 3)
                NewXCoordinate_Str_Hidden = str(NewXCoordinate_Round)
                NewXCoordinateStr = str("G1X"+NewXCoordinate_Str_Hidden+"\n")
                
                print("G1"+"X"+NewXCoordinate_Str_Hidden+" "+"Y"+NewYCoordinate_Str_Hidden+"\n")
                NewXCoordinateBytes = bytes(NewXCoordinateStr, 'UTF-8')
                ser.write(NewXCoordinateBytes) #move to the new x-coordinate
                
                #logic to wait, take a picture, wait,
                time.sleep(UserNodeInitialDelayFloat/1000) #wait specified amount of time before taking picture
                         
                #Logic to add to picture taking, Pi will need to save these images in a user specified folder on the desktop.
                #Title of images should be in the format (X,Y). Files should save images as .tiff
                XCoordinatesForFileName = str(NewXCoordinate_Str_Hidden)
                YCoordinatesForFileName = str(NewYCoordinate_Str_Hidden)
                XYCoordinatesForFileName = str("(" + XCoordinatesForFileName + "," + YCoordinatesForFileName + ")" + '.tiff')
                ImageWriteDirectoryAndFileName = str(DirectoryToStoreImages+XYCoordinatesForFileName)
                #print("The string variable ImageWriteDirectoryAndFileName is"+" "+ImageWriteDirectoryAndFileName)
                
                #This segment uses OpenCV Libraries to take a picture and store it in the user named folder on the desktop
                cap = cv2.VideoCapture(0)
                ret, frame = cap.read()
                cv2.imshow("imshow",frame)
                cv2.imwrite(ImageWriteDirectoryAndFileName, frame)
                cap.release()
                print("Image saved to folder.")
                
                #This section appends the TileConfiguration.txt file to include the file name and pixel coordinates for the newly taken image.
                #variables used in this section NewXCoordinate_Round, NewYCoordinate_Round, NewXCoordinate_Str_Hidden, NewYCoordinate_Str_Hidden
                NewXCoordinateInPixels_Round = round((NewXCoordinate_Round*UserDefinedPixelsPerMM_Round),3)
                NewXCoordinateInPixels_Str = str(NewXCoordinateInPixels_Round)
                
                
                CurrentYPositioninMM_Round =  round((MinimumYBoundaryFloat + (CurrentYNode * UserYNodeSpacingFloat)),3)
                InvertedNewYCoordinateInMM_Round = round((MaximumYBoundaryFloat-CurrentYPositioninMM_Round),3) #need to include some logic here that inverts the Y coordinate pixel value
                InvertedNewYCoordinateInPixels_Round = round((InvertedNewYCoordinateInMM_Round*UserDefinedPixelsPerMM_Round),3)
                InvertedNewYCoordinateInPixels_Str = str(InvertedNewYCoordinateInPixels_Round)
                
                f= open(DirectoryToStoreTileConfiguration+"TileConfiguration.txt","a+")   #this will create a file called TileConfiguration.txt use w+ to write a file, use a+ to append a file (continually add lines to the file)
                f.write("(" + NewXCoordinate_Str_Hidden + "," + NewYCoordinate_Str_Hidden + ")" + ".tiff" + "; ; " + "(" + NewXCoordinateInPixels_Str + ", " + InvertedNewYCoordinateInPixels_Str + ")") #write a line
                f.write("\n") #this makes it skip a line
                f.close()
                  
                ser.write(ShortBeepSoundBytes)
                time.sleep(UserNodePostDelayFloat/1000) #wait specified amount of time after taking picture
                CurrentXNode = (CurrentXNode+1)#increase X node value by 1
                print("Travelling to next X node.")
                #travel to new coordinates.
                
                                
                if CurrentXNode > (MaxXNode+1): #or (CurrentXNode = MaxXNode) #X node value exceeds maximum X node value
                    CurrentXNode = 1 #reset X node value to 1
                    #logic to return to first x-node
                    NewXCoordinate_Round = round((MinimumXBoundaryFloat+((CurrentXNode-1)*UserXNodeSpacingFloat)), 3)
                    NewXCoordinate_Str_Hidden = str(NewXCoordinate_Round)
                    NewXCoordinateStr = str("G1X"+NewXCoordinate_Str_Hidden+"\n")
                    NewXCoordinateBytes = bytes(NewXCoordinateStr, 'UTF-8')
                    ser.write(NewXCoordinateBytes) #move to the new x-coordinat
                    print("Row complete. Returning to first X-node in row.")
                    time.sleep(5)
                    
                    
                    print("Moving up one Y node and continuing to scan.")
                    CurrentYNode = CurrentYNode+1 #increase Y node value by 1
                    NewYCoordinate_Round = round((MinimumYBoundaryFloat+((CurrentYNode-1)*UserYNodeSpacingFloat)), 3)
                    NewYCoordinate_Str_Hidden = str(NewYCoordinate_Round)
                    NewYCoordinateStr = str("G1Y"+NewYCoordinate_Str_Hidden+"\n")
                    
                    ser.write(ShortBeepSoundBytes)
                    time.sleep(0.25)
                    ser.write(ShortBeepSoundBytes) #double beep to alert user an X row is complete
                    #logic to move up one Y-node
                    NewYCoordinateBytes = bytes(NewYCoordinateStr, 'UTF-8')
                    ser.write(NewYCoordinateBytes) #move to the new Y-coordinate
                    time.sleep(5)
            
            
            print("Scan completed.")
            ser.write(bytes("G28\n", 'UTF-8'))  #Scanning Logic: First home, pi waits to hear from the arduino that it has reached home.
            print("Returning to home position.")
            while read_ser != (b'X:0.00 Y:150.00 Z:430.00 E:0.00 Count X:0 Y:60000 Z:172000\n'): #this while loop makes the pi listen for the arduino's signal that it has completed homing.
                read_ser=ser.readline()
                #print(read_ser)
                ser.flush()
            ser.write(ShortBeepSoundBytes) #play the victory song! This song signals the completion of automated camera scanning
            time.sleep(0.10)   
            ser.write(ShortBeepSoundBytes)
            time.sleep(0.10)
            ser.write(ShortBeepSoundBytes)
            time.sleep(0.10)
            ser.write(ShortBeepSoundBytes)
            time.sleep(0.10)
            ser.write(ShortBeepSoundBytes)
            time.sleep(0.10)
            #and return to the main menu
            
            
     #------------------------------------------------------------#      
        elif ConfirmAutomatedCameraScanning == "N": #if the user chooses not to start the automated camera scan.
            print("Returning to main menu.")
        
       
            

    #------------------------------------------------------------#
        
    elif UserMenuInput == "3": #this is the spindle stretching section
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
            print("You entered "+UserManualGCodeInput + ". " + ArduinoChangeLine)
            ManualCommandInBytes = bytes((UserManualGCodeInput + " " + ArduinoChangeLine), 'UTF-8')
            ser.write(ManualCommandInBytes)     
            
        if UserManualGCodeInput in ["Continue", "continue"]:
            print("")
            print("------------------------------------------------------------")
            print("")
            print("Hook in position, continuing to stretch settings. ")
            print("")
            PullsPerCycle_Str = input("How many pulls per cycle? (Maximum 8) ") #maximum of 8 because the standard buffer size for queued moves in marlin is 16. if there are 8 pulls there also need to be 8 returns to starting position, hence 8 is max.
            PullsPerCycle_Int = int(PullsPerCycle_Str)
            print("")
            TotalNumberofCycles_Str = input("How many cycles to carry out? ")
            TotalNumberofCycles_Int = int(TotalNumberofCycles_Str)
            print("")
            TravelDistancePerPull_Str = input("How far should the hook travel during one pull? (value in millimeters) ")
                                    
            #some declaration of variables before tugging!
            
            if StretchTravelDirection_Str == "Left":
                PullCommand_Str = str("G1X-"+TravelDistancePerPull_Str+" \n")
                PullCommand_Bytes = bytes(PullCommand_Str, 'UTF-8')
                RestCommand_Str = str("G1X+"+TravelDistancePerPull_Str+" \n")
                RestCommand_Bytes = bytes(RestCommand_Str, 'UTF-8')    
                
                
            if StretchTravelDirection_Str == "Right":
                PullCommand_Str = str("G1X+"+TravelDistancePerPull_Str+" \n")
                PullCommand_Bytes = bytes(PullCommand_Str, 'UTF-8')
                RestCommand_Str = str("G1X-"+TravelDistancePerPull_Str+" \n")
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
            
            #logic to pull and relax the lumbrical in cycles
            ser.write(ConvertToRelativeCoordinates_Bytes) #swap to relative coordinates is G91
            while CurrentCycle_Int < (MaximumCycle+1):
                
                while CurrentPull < MaximumPull:
                    CurrentPull = (CurrentPull +1)
                    ser.write(PullCommand_Bytes)
                    GPIO.output(18,1) #TTL output high
                    GPIO.output(18,0) #TTL output low
                    ser.write(RestCommand_Bytes)
                CurrentPull = (0) #resets the current pull back to zero
                
                RemainingCycles_Int = int(MaximumCycle-CurrentCycle_Int)
                RemainingCycles_Str = str(RemainingCycles_Int)
                CurrentCycle_Str = str(CurrentCycle_Int)
                print("Cycle " + CurrentCycle_Str + " complete. " + RemainingCycles_Str + " cycles remaining.")
                CurrentCycle_Int = (CurrentCycle_Int+1) #having completed a cycle of pulls, increases cycle by one
                time.sleep(1.0)
                ser.write(ShortBeepSoundBytes)
                time.sleep(1.0)
            
            ser.write(ConvertToAbsoluteCoordinates_Bytes) #swap back to absolute coordinates = G90
            print("Maximum travel speed has been reset to 100mm/s. ")
            ChangeSpeedTo100_Str = str("M203 X100 \n")
            ChangeSpeedTo100_Bytes = bytes(ChangeSpeedTo100_Str, 'UTF-8')
            ser.write(ChangeSpeedTo100_Bytes)
            print("Acceleration has been reset to 1000mm/s^2. ")
            ChangeAccelTo1000_Str = str("M204 T1000 \n")
            ChangeAccelTo1000_Bytes = bytes(ChangeAccelTo1000_Str, 'UTF-8')
            ser.write(ChangeAccelTo1000_Bytes)
            print("All Cycles completed. Returning to Main Menu.")
            #exit to main menu
            
            
            #Change acceleration for travel moves = M204 TVALUE, check current settings with M503
            #G1X-1, G1X1
            
        
        
        
            
        elif UserManualGCodeInput in ["Main Menu", "main menu"]:
            print("You chose to return to the main menu. Returning to main menu. ")
            
        
        
    
    elif UserMenuInput == "4":
        print("------------------------------------------------------------")
        print("")
        print("Welcome to the Ramping Dynamic Threshold Assessment Section for Distance, Speed & Acceleration. ")
        print("This section allows the user to gradually vary travel distance, maximum travel speed or acceleration")
        print("of the hook. ")
        print("")
        print("------------------------------------------------------------")
        
        ListofPositiveResponses = ["Y", "y", "Yes", "yes"]
        ListofNegativeResponses = ["N", "n", "No", "no"]
        
        print("Perform an auto home before starting? (Y/N) ")
        UserManualGCodeInput = input("")
        if UserManualGCodeInput in ListofPositiveResponses:
            HomingCommandInBytes = bytes(("G28" + " \n"), 'UTF-8')
            ser.write(HomingCommandInBytes)
            print("Homing. This will take approximately 2 minutes. ")
            time.sleep(140)
            
        print("Move to the default starting position of X150.0 Y90.0 Z70.0? (Y/N)  ")
        UserManualGCodeInput = input("")
        if UserManualGCodeInput in ListofPositiveResponses:
            MoveToSpindleStartingPositionInBytes = bytes(("G1X140Y95Z10" + " \n"), 'UTF-8')
            ser.write(MoveToSpindleStartingPositionInBytes)
            print("Moving to spindle starting position. This will take approximately 1 minutes. ")
            time.sleep(60)
            
        print("")
        print("------------------------------------------------------------")
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
            print("You entered "+UserManualGCodeInput + ". " + ArduinoChangeLine)
            ManualCommandInBytes = bytes((UserManualGCodeInput + " " + ArduinoChangeLine), 'UTF-8')
            ser.write(ManualCommandInBytes)     
            
        if UserManualGCodeInput in ["Continue", "continue"]:
            print("")
            print("------------------------------------------------------------")
            print("")
            print("Hook in position, continuing to advanced stretch settings. ")
            print("")
            print("------------------------------------------------------------")
            print("")
                        
            UserChoice = input("Would you like to vary distance, speed or acceleration? Enter D, S or A. ")
            
            #----------------------------------------------------------------------------------------------------------------------------#  
            if UserChoice in ["D", "d", "Distance", "distance"]:
                print("You have chosen to vary distance. ")
                
                print("Maximum travel speed will remain constant at 30mm/s. ")
                ChangeSpeedTo30_Str = str("M203 X30 \n")
                ChangeSpeedTo30_Bytes = bytes(ChangeSpeedTo30_Str, 'UTF-8')
                ser.write(ChangeSpeedTo30_Bytes)
                print("and acceleration will constant remain at 100mm/s^2. ")
                ChangeAccelTo100_Str = str("M204 T100 \n")
                ChangeAccelTo100_Bytes = bytes(ChangeAccelTo100_Str, 'UTF-8')
                ser.write(ChangeAccelTo100_Bytes)
                
                print("")
                MinimumPullDistance_Str = input("What should the minimum pull distance be? (mm). ")
                print("")
                MaximumPullDistance_Str = input("What should the maximum pull distance be? (mm). ")
                print("")
                IncrementValue_Str = input("How much should the system increase the travel distance (mm) by after completing each cycle of 10 pulls? ")
                print("")
                
                #convert the user specified values to round
                MinimumPullDistance_Float = float(MinimumPullDistance_Str)
                MinimumPullDistance_Round = round(MinimumPullDistance_Float,3)
                MaximumPullDistance_Float = float(MaximumPullDistance_Str)
                MaximumPullDistance_Round = round(MaximumPullDistance_Float,3)
                IncrementValue_Float = float(IncrementValue_Str)
                IncrementValue_Round = round(IncrementValue_Float,3)
                
                #control the number of pulls per cycle, cycles per incremement group
                CurrentPull = int(0)
                MaximumPull = int(1)
                PullsPerCycle_Int = int(1)
                CurrentCycle_Int = int(1)
                
                IncrementGroupNumber_Int = int(0)
                TotalNumberofCyclesPerIncrementGroup_Int = int(10)
                TotalIncrementGroups_Int = int(((MaximumPullDistance_Round-MinimumPullDistance_Round)/IncrementValue_Round))
                
                #some string conversions
                PullsPerCycle_Str = str(PullsPerCycle_Int)
                TotalNumberofCyclesPerIncrementGroup_Str = str(TotalNumberofCyclesPerIncrementGroup_Int)
                
                #User review and confirmation
                print("Minimum travel distance = "+MinimumPullDistance_Str)
                print("Maximum travel distance = "+MaximumPullDistance_Str)
                print("Travel distance increments = "+IncrementValue_Str)
                print("The system will perform "+PullsPerCycle_Str+" pulls per cycle and "+TotalNumberofCyclesPerIncrementGroup_Str+" cycles before increasing travel distance.")
                print("After reaching maximum travel distance the system will gradually reduce travel distance back to the minimum travel distance.")
                print("Please confirm the above settings. Enter Y or N.")
                UserChoice_Str = input("")
                ListofPositiveResponses = ["Y", "y", "Yes", "yes"]
                if UserChoice_Str in ListofPositiveResponses:
                    #some declaration of variables before tugging!
                    
                    VariableTravelDistance_Round = round(MinimumPullDistance_Round+(IncrementValue_Round*(CurrentCycle_Int-1)),3)
                    VariableTravelDistance_Str = str(VariableTravelDistance_Round)
                    PullCommand_Str = str("G1X-"+VariableTravelDistance_Str+" \n")
                    PullCommand_Bytes = bytes(PullCommand_Str, 'UTF-8')
                    RestCommand_Str = str("G1X+"+VariableTravelDistance_Str+" \n")
                    RestCommand_Bytes = bytes(RestCommand_Str, 'UTF-8') 
                    
                    #if StretchTravelDirection_Str == "Left":
                    #if StretchTravelDirection_Str == "Right":
                                        
                    ConvertToRelativeCoordinates_Str = str("G91 \n")
                    ConvertToRelativeCoordinates_Bytes = bytes(ConvertToRelativeCoordinates_Str, 'UTF-8')
                    ConvertToAbsoluteCoordinates_Str = str("G90 \n")
                    ConvertToAbsoluteCoordinates_Bytes = bytes(ConvertToAbsoluteCoordinates_Str, 'UTF-8')
                    
                    ShortBeepSound = str("M300 P10")
                    ShortBeepSoundBytes = bytes((ShortBeepSound + " \n"), 'UTF-8')
                    LongBeepSound = str("M300 P1000")
                    LongBeepSoundBytes = bytes((LongBeepSound + " \n"), 'UTF-8')
                    
                    
                    
                    
                    #logic to start the loop
                    ser.write(ConvertToRelativeCoordinates_Bytes) #first convert to relative coordinates
                    
                    #do it from minimum to maximum
                    while IncrementGroupNumber_Int < (TotalIncrementGroups_Int): #can replace the +1 here
                        print("Current travel distance per pull is " + VariableTravelDistance_Str + " mm. ")
                        CurrentCycle_Int = int(1) #set current cycle_it back to one
                        
                        while CurrentCycle_Int < (TotalNumberofCyclesPerIncrementGroup_Int+1): #this loop controls the number of cycles per Increment Group
                    
                            while CurrentPull < MaximumPull: #this loop controls the number of pulls per cycle
                                CurrentPull = (CurrentPull +1)
                                ser.write(PullCommand_Bytes)
                                GPIO.output(18,1) #TTL output high
                                GPIO.output(18,0) #TTL output low
                                ser.write(RestCommand_Bytes)
                                #time.sleep(0.5)
                                    
                            CurrentPull = (0) #resets the current pull back to zero so that the pull loop will recur
                            RemainingCycles_Int = int(TotalNumberofCyclesPerIncrementGroup_Int-CurrentCycle_Int)
                            RemainingCycles_Str = str(RemainingCycles_Int)
                            CurrentCycle_Str = str(CurrentCycle_Int)
                            CurrentCycle_Int = (CurrentCycle_Int+1) #having completed a cycle of pulls, increases cycle counter by one
                            time.sleep(1.0)
                            ser.write(ShortBeepSoundBytes) #makes a single bleeping noise to alert the user that a cycle has completed
                            print(CurrentCycle_Str + " cycles completed. " + RemainingCycles_Str + " cycles remaining. ") # prints information to the user to say that  a cycle has completed and how many cycles remain.
                            time.sleep(1.0)
                
                        IncrementGroupNumber_Int = (IncrementGroupNumber_Int+1) #increment group number logic goes here
                        VariableTravelDistance_Round = round(MinimumPullDistance_Round+(IncrementValue_Round*(IncrementGroupNumber_Int)),3)
                        VariableTravelDistance_Str = str(VariableTravelDistance_Round)
                        PullCommand_Str = str("G1X-"+VariableTravelDistance_Str+" \n")#set the current travel distance pull command
                        PullCommand_Bytes = bytes(PullCommand_Str, 'UTF-8')
                        RestCommand_Str = str("G1X+"+VariableTravelDistance_Str+" \n") #set the current travel distance rest command
                        RestCommand_Bytes = bytes(RestCommand_Str, 'UTF-8')
                        
                    #this bit sets the variables for the max to min portion
                    IncrementGroupNumber_Int = (IncrementGroupNumber_Int+1) 
                                        
                    #do it from maximum to minimum
                    while (IncrementGroupNumber_Int+1) > 0:
                        print("Current travel distance per pull is " + VariableTravelDistance_Str + " mm. ")
                        CurrentCycle_Int = int(1) #set current cycle_it back to one
                        
                        while CurrentCycle_Int < (TotalNumberofCyclesPerIncrementGroup_Int+1): #this loop controls the number of cycles per Increment Group
                    
                            while CurrentPull < MaximumPull: #this loop controls the number of pulls per cycle
                                CurrentPull = (CurrentPull +1)
                                ser.write(PullCommand_Bytes)
                                GPIO.output(18,1) #TTL output high
                                GPIO.output(18,0) #TTL output low
                                ser.write(RestCommand_Bytes)
                                #time.sleep(0.5)
                                    
                            CurrentPull = (0) #resets the current pull back to zero so that the pull loop will recur
                            RemainingCycles_Int = int(TotalNumberofCyclesPerIncrementGroup_Int-CurrentCycle_Int)
                            RemainingCycles_Str = str(RemainingCycles_Int)
                            CurrentCycle_Str = str(CurrentCycle_Int)
                            CurrentCycle_Int = (CurrentCycle_Int+1) #having completed a cycle of pulls, increases cycle counter by one
                            time.sleep(1.0)
                            ser.write(ShortBeepSoundBytes) #makes a single bleeping noise to alert the user that a cycle has completed
                            print(CurrentCycle_Str + " cycles completed. " + RemainingCycles_Str + " cycles remaining. ") # prints information to the user to say that  a cycle has completed and how many cycles remain.
                            time.sleep(1.0)
                
                        IncrementGroupNumber_Int = (IncrementGroupNumber_Int-1) #increment group number logic goes here
                        VariableTravelDistance_Round = round(MinimumPullDistance_Round+(IncrementValue_Round*(IncrementGroupNumber_Int)),3)
                        VariableTravelDistance_Str = str(VariableTravelDistance_Round)
                        PullCommand_Str = str("G1X-"+VariableTravelDistance_Str+" \n")#set the current travel distance pull command
                        PullCommand_Bytes = bytes(PullCommand_Str, 'UTF-8')
                        RestCommand_Str = str("G1X+"+VariableTravelDistance_Str+" \n") #set the current travel distance rest command
                        RestCommand_Bytes = bytes(RestCommand_Str, 'UTF-8')
                         
                        
                print("Maximum travel speed will reset to 100mm/s. ")
                ChangeSpeedTo100_Str = str("M203 X100 \n")
                ChangeSpeedTo100_Bytes = bytes(ChangeSpeedTo100_Str, 'UTF-8')
                ser.write(ChangeSpeedTo100_Bytes)
                print("Acceleration reset to 1000mm/s^2. ")
                ChangeAccelTo1000_Str = str("M204 T1000 \n")
                ChangeAccelTo1000_Bytes = bytes(ChangeAccelTo1000_Str, 'UTF-8')
                ser.write(ChangeAccelTo1000_Bytes)
            #----------------------------------------------------------------------------------------------------------------------------#           
                
            #----------------------------------------------------------------------------------------------------------------------------#      
            if UserChoice in ["S", "s", "Speed", "speed"]:                
                print("You have chosen to vary speed. Default maximum travel speed = 100mm/s. ")
                print("Travel distance will remain constant at +/- 2.0mm")
                FixedTravelDistance_Str = str("2.0")
                print("and acceleration will constant remain at 100m/s^2.")
                ChangeAccelTo100_Str = str("M204 T100 \n")
                ChangeAccelTo100_Bytes = bytes(ChangeAccelTo100_Str, 'UTF-8')
                ser.write(ChangeAccelTo100_Bytes)
                print("")
                MinimumPullSpeed_Str = input("What should the minimum pull speed be? (mm/s). ")
                print("")
                MaximumPullSpeed_Str = input("What should the maximum pull speed be? (mm/s). ")
                print("")
                IncrementValue_Str = input("How much should the system increase the travel speed (mm/s) by after completing each cycle of 10 pulls? ")
                print("")
                
                #convert the user specified values to round
                MinimumPullSpeed_Float = float(MinimumPullSpeed_Str)
                MinimumPullSpeed_Round = round(MinimumPullSpeed_Float,3)
                MaximumPullSpeed_Float = float(MaximumPullSpeed_Str)
                MaximumPullSpeed_Round = round(MaximumPullSpeed_Float,3)
                IncrementValue_Float = float(IncrementValue_Str)
                IncrementValue_Round = round(IncrementValue_Float,3)
                
                #control the number of pulls per cycle, cycles per incremement group
                CurrentPull = int(0)
                MaximumPull = int(1)
                PullsPerCycle_Int = int(1)
                CurrentCycle_Int = int(1)
                
                IncrementGroupNumber_Int = int(0)
                TotalNumberofCyclesPerIncrementGroup_Int = int(10)
                TotalIncrementGroups_Int = int(((MaximumPullSpeed_Round-MinimumPullSpeed_Round)/IncrementValue_Round))
                
                #some string conversions
                PullsPerCycle_Str = str(PullsPerCycle_Int)
                TotalNumberofCyclesPerIncrementGroup_Str = str(TotalNumberofCyclesPerIncrementGroup_Int)
                
                #User review and confirmation
                print("Minimum pull speed = " + MinimumPullSpeed_Str + " mm/s.")
                print("Maximum pull speed = " + MaximumPullSpeed_Str + " mm/s.")
                print("Speed increments = " + IncrementValue_Str + " mm/s.")
                print("Fixed travel distance = " + FixedTravelDistance_Str + " mm/s.")
                print("The system will perform " + PullsPerCycle_Str + " pulls per cycle and " + TotalNumberofCyclesPerIncrementGroup_Str + " cycles before increasing pull speed.")
                print("After reaching maximum pull speed the system will gradually reduce pull speed back to the minimum travel distance.")
                print("Please confirm the above settings. Enter Y or N.")
                UserChoice_Str = input("")
                ListofPositiveResponses = ["Y", "y", "Yes", "yes"]
                
                if UserChoice_Str in ListofPositiveResponses:
                    #some declaration of variables before tugging!
                    
                    VariablePullSpeed_Round = round(MinimumPullSpeed_Round+(IncrementValue_Round*(CurrentCycle_Int-1)),3)
                    VariablePullSpeed_Str = str(VariablePullSpeed_Round)
                    CommandToChangePullSpeed_Str = str("M203 X" + VariablePullSpeed_Str + " \n")
                    CommandToChangePullSpeed_Bytes = bytes(CommandToChangePullSpeed_Str, 'UTF-8')
                    
                    PullCommand_Str = str("G1X-"+FixedTravelDistance_Str+" \n")
                    PullCommand_Bytes = bytes(PullCommand_Str, 'UTF-8')
                    RestCommand_Str = str("G1X+"+FixedTravelDistance_Str+" \n")
                    RestCommand_Bytes = bytes(RestCommand_Str, 'UTF-8')
            
                    ConvertToRelativeCoordinates_Str = str("G91 \n")
                    ConvertToRelativeCoordinates_Bytes = bytes(ConvertToRelativeCoordinates_Str, 'UTF-8')
                    ConvertToAbsoluteCoordinates_Str = str("G90 \n")
                    ConvertToAbsoluteCoordinates_Bytes = bytes(ConvertToAbsoluteCoordinates_Str, 'UTF-8')
                    
                    ShortBeepSound = str("M300 P10")
                    ShortBeepSoundBytes = bytes((ShortBeepSound + " \n"), 'UTF-8')
                    LongBeepSound = str("M300 P1000")
                    LongBeepSoundBytes = bytes((LongBeepSound + " \n"), 'UTF-8')
                    
                    
                    #logic to start the loop
                    ser.write(ConvertToRelativeCoordinates_Bytes) #first convert to relative coordinates
                    
                    #do it from minimum to maximum
                    while IncrementGroupNumber_Int < (TotalIncrementGroups_Int):
                        print("Current pull speed is " + VariablePullSpeed_Str + " mm/s. ")
                        CurrentCycle_Int = int(1) #set current cycle_it back to one
                        
                        ser.write(CommandToChangePullSpeed_Bytes)
                        
                        while CurrentCycle_Int < (TotalNumberofCyclesPerIncrementGroup_Int+1): #this loop controls the number of cycles per Increment Group
                    
                            while CurrentPull < MaximumPull: #this loop controls the number of pulls per cycle
                                CurrentPull = (CurrentPull +1)
                                ser.write(PullCommand_Bytes)
                                GPIO.output(18,1) #TTL output high
                                GPIO.output(18,0) #TTL output low
                                ser.write(RestCommand_Bytes)
                                #time.sleep(0.5)
                                    
                            CurrentPull = (0) #resets the current pull back to zero so that the pull loop will recur
                            RemainingCycles_Int = int(TotalNumberofCyclesPerIncrementGroup_Int-CurrentCycle_Int)
                            RemainingCycles_Str = str(RemainingCycles_Int)
                            CurrentCycle_Str = str(CurrentCycle_Int)
                            CurrentCycle_Int = (CurrentCycle_Int+1) #having completed a cycle of pulls, increases cycle counter by one
                            time.sleep(1.0)
                            ser.write(ShortBeepSoundBytes) #makes a single bleeping noise to alert the user that a cycle has completed
                            print(CurrentCycle_Str + " cycles completed. " + RemainingCycles_Str + " cycles remaining. ") # prints information to the user to say that  a cycle has completed and how many cycles remain.
                            time.sleep(1.0)
                
                        IncrementGroupNumber_Int = (IncrementGroupNumber_Int+1) #increase the increment group by 1
                        VariablePullSpeed_Round = round(MinimumPullSpeed_Round+(IncrementValue_Round*(IncrementGroupNumber_Int)),3)#define new pull speed
                        VariablePullSpeed_Str = str(VariablePullSpeed_Round)
                        CommandToChangePullSpeed_Str = str("M203 X" + VariablePullSpeed_Str + " \n")
                        CommandToChangePullSpeed_Bytes = bytes(CommandToChangePullSpeed_Str, 'UTF-8') #set new pull speed
                        
                    #this section prepares the variables for the gradual decrease in speed  
                    IncrementGroupNumber_Int = (IncrementGroupNumber_Int+1)
                                        
                    #do it from maximum to minimum
                    while (IncrementGroupNumber_Int+1) > 0:
                        print("Current pull speed is " + VariablePullSpeed_Str + " mm/s. ")
                        CurrentCycle_Int = int(1) #set current cycle_it back to one
                        
                        ser.write(CommandToChangePullSpeed_Bytes)
                        
                        while CurrentCycle_Int < (TotalNumberofCyclesPerIncrementGroup_Int+1): #this loop controls the number of cycles per Increment Group
                    
                            while CurrentPull < MaximumPull: #this loop controls the number of pulls per cycle
                                CurrentPull = (CurrentPull +1)
                                ser.write(PullCommand_Bytes)
                                GPIO.output(18,1) #TTL output high
                                GPIO.output(18,0) #TTL output low
                                ser.write(RestCommand_Bytes)
                                #time.sleep(0.5)
                                    
                            CurrentPull = (0) #resets the current pull back to zero so that the pull loop will recur
                            RemainingCycles_Int = int(TotalNumberofCyclesPerIncrementGroup_Int-CurrentCycle_Int)
                            RemainingCycles_Str = str(RemainingCycles_Int)
                            CurrentCycle_Str = str(CurrentCycle_Int)
                            CurrentCycle_Int = (CurrentCycle_Int+1) #having completed a cycle of pulls, increases cycle counter by one
                            time.sleep(1.0)
                            ser.write(ShortBeepSoundBytes) #makes a single bleeping noise to alert the user that a cycle has completed
                            print(CurrentCycle_Str + " cycles completed. " + RemainingCycles_Str + " cycles remaining. ") # prints information to the user to say that  a cycle has completed and how many cycles remain.
                            time.sleep(1.0)
                
                        IncrementGroupNumber_Int = (IncrementGroupNumber_Int-1) #increment group number logic goes here
                        VariablePullSpeed_Round = round(MinimumPullSpeed_Round+(IncrementValue_Round*(IncrementGroupNumber_Int)),3)
                        VariablePullSpeed_Str = str(VariablePullSpeed_Round)
                        CommandToChangePullSpeed_Str = str("M203 X" + VariablePullSpeed_Str + " \n")
                        CommandToChangePullSpeed_Bytes = bytes(CommandToChangePullSpeed_Str, 'UTF-8') #set new pull speed
                 
                 
                #this bit needs to reset the travel speed values back to default of 100mm/s (M203 X100)
                print("Maximum travel speed has reset to 100mm/s. ")
                CommandToChangePullSpeed_Str = str("M203 X100 \n")
                CommandToChangePullSpeed_Bytes = bytes(CommandToChangePullSpeed_Str, 'UTF-8') #set new pull speed
                ser.write(CommandToChangePullSpeed_Bytes)
                print("Acceleration reset to 1000mm/s^2. ")
                ChangeAccelTo1000_Str = str("M204 T1000 \n")
                ChangeAccelTo1000_Bytes = bytes(ChangeAccelTo1000_Str, 'UTF-8')
                ser.write(ChangeAccelTo1000_Bytes)
                print("Pull speed test now finished. Returning to main menu. ")
            #----------------------------------------------------------------------------------------------------------------------------#
            
            
            #----------------------------------------------------------------------------------------------------------------------------#  
            if UserChoice in ["A", "a", "Acceleration", "acceleration"]:
                print("You have chosen to vary acceleration. (Default acceleration = 1000mm/s^2). ")
                
                print("Travel distance will remain constant at +/- 2.0mm ")
                FixedTravelDistance_Str = str("2.0")
                
                print("Maximum travel speed will remain constant at 30mm/s. ")
                FixedMaxTravelSpeed_Str = str("30.0")
                ChangeSpeedTo30_Str = str("M203 X30 \n")
                ChangeSpeedTo30_Bytes = bytes(ChangeSpeedTo30_Str, 'UTF-8')
                ser.write(ChangeSpeedTo30_Bytes)
                
                
                print("")
                MinimumAcceleration_Str = input("What should the minimum acceleration be? (mm/s^2). ")
                print("")
                MaximumAcceleration_Str = input("What should the maximum acceleration be? (mm/s^2). ")
                print("")
                IncrementValue_Str = input("How much should the system increase acceleration (mm/s^2) by after completing each cycle of 10 pulls? ")
                print("")
                
                #convert the user specified values to round
                MinimumAcceleration_Float = float(MinimumAcceleration_Str)
                MinimumAcceleration_Round = round(MinimumAcceleration_Float,3)
                MaximumAcceleration_Float = float(MaximumAcceleration_Str)
                MaximumAcceleration_Round = round(MaximumAcceleration_Float,3)
                IncrementValue_Float = float(IncrementValue_Str)
                IncrementValue_Round = round(IncrementValue_Float,3)
                
                
                #control the number of pulls per cycle, cycles per incremement group
                CurrentPull = int(0)
                MaximumPull = int(1)
                PullsPerCycle_Int = int(1)
                CurrentCycle_Int = int(1)
                
                IncrementGroupNumber_Int = int(0)
                TotalNumberofCyclesPerIncrementGroup_Int = int(10)
                TotalIncrementGroups_Int = int(((MaximumAcceleration_Round-MinimumAcceleration_Round)/IncrementValue_Round))
                
                #some string conversions
                PullsPerCycle_Str = str(PullsPerCycle_Int)
                TotalNumberofCyclesPerIncrementGroup_Str = str(TotalNumberofCyclesPerIncrementGroup_Int)
                
                #User review and confirmation
                print("Minimum acceleration = " + MinimumAcceleration_Str + " mm/s^2. ")
                print("Maximum acceleration = " + MaximumAcceleration_Str + " mm/s^2. ")
                print("Acceleration increments = " + IncrementValue_Str + " mm/s^2. ")
                print("Fixed travel distance = " + FixedTravelDistance_Str + " mm/s. ")
                print("Fixed maximum tavel speed  = " + FixedMaxTravelSpeed_Str + " mm/s")
                print("The system will perform " + PullsPerCycle_Str + " pulls per cycle and " + TotalNumberofCyclesPerIncrementGroup_Str + " cycles before increasing pull speed.")
                print("After reaching maximum acceleration the system will gradually reduce acceleration back to the minimum travel distance.")
                print("Please confirm the above settings. Enter Y or N.")
                UserChoice_Str = input("")
                ListofPositiveResponses = ["Y", "y", "Yes", "yes"]
                
                if UserChoice_Str in ListofPositiveResponses:
                    #some declaration of variables before tugging!
                    
                    VariableAcceleration_Round = round(MinimumAcceleration_Round+(IncrementValue_Round*(CurrentCycle_Int-1)),3)
                    VariableAcceleration_Str = str(VariableAcceleration_Round)
                    CommandToChangeAcceleration_Str = str("M204 T" + VariableAcceleration_Str + " \n") #M204 T sets the acceleration for travel moves
                    CommandToChangeAcceleration_Bytes = bytes(CommandToChangeAcceleration_Str, 'UTF-8')
                    
                    PullCommand_Str = str("G1X-"+FixedTravelDistance_Str+" \n")
                    PullCommand_Bytes = bytes(PullCommand_Str, 'UTF-8')
                    RestCommand_Str = str("G1X+"+FixedTravelDistance_Str+" \n")
                    RestCommand_Bytes = bytes(RestCommand_Str, 'UTF-8')
            
                    ConvertToRelativeCoordinates_Str = str("G91 \n")
                    ConvertToRelativeCoordinates_Bytes = bytes(ConvertToRelativeCoordinates_Str, 'UTF-8')
                    ConvertToAbsoluteCoordinates_Str = str("G90 \n")
                    ConvertToAbsoluteCoordinates_Bytes = bytes(ConvertToAbsoluteCoordinates_Str, 'UTF-8')
                    
                    ShortBeepSound = str("M300 P10")
                    ShortBeepSoundBytes = bytes((ShortBeepSound + " \n"), 'UTF-8')
                    LongBeepSound = str("M300 P1000")
                    LongBeepSoundBytes = bytes((LongBeepSound + " \n"), 'UTF-8')
                    
                    
                    #logic to start the loop
                    ser.write(ConvertToRelativeCoordinates_Bytes) #first convert to relative coordinates
                    
                    #do it from minimum to maximum
                    while IncrementGroupNumber_Int < (TotalIncrementGroups_Int):
                        print("Current acceleration is " + VariableAcceleration_Str + " mm/s^2. ")
                        CurrentCycle_Int = int(1) #set current cycle_it back to one
                        
                        ser.write(CommandToChangeAcceleration_Bytes)
                        
                        while CurrentCycle_Int < (TotalNumberofCyclesPerIncrementGroup_Int+1): #this loop controls the number of cycles per Increment Group
                    
                            while CurrentPull < MaximumPull: #this loop controls the number of pulls per cycle
                                CurrentPull = (CurrentPull +1)
                                ser.write(PullCommand_Bytes)
                                GPIO.output(18,1) #TTL output high
                                GPIO.output(18,0) #TTL output low
                                ser.write(RestCommand_Bytes)
                                #time.sleep(0.5)
                                    
                            CurrentPull = (0) #resets the current pull back to zero so that the pull loop will recur
                            RemainingCycles_Int = int(TotalNumberofCyclesPerIncrementGroup_Int-CurrentCycle_Int)
                            RemainingCycles_Str = str(RemainingCycles_Int)
                            CurrentCycle_Str = str(CurrentCycle_Int)
                            CurrentCycle_Int = (CurrentCycle_Int+1) #having completed a cycle of pulls, increases cycle counter by one
                            time.sleep(1.0)
                            ser.write(ShortBeepSoundBytes) #makes a single bleeping noise to alert the user that a cycle has completed
                            print(CurrentCycle_Str + " cycles completed. " + RemainingCycles_Str + " cycles remaining. ") # prints information to the user to say that  a cycle has completed and how many cycles remain.
                            time.sleep(1.0)
                
                        IncrementGroupNumber_Int = (IncrementGroupNumber_Int+1) #increase the increment group by 1
                        VariableAcceleration_Round = round(MinimumAcceleration_Round+(IncrementValue_Round*(IncrementGroupNumber_Int)),3)#define new acceleration
                        VariableAcceleration_Str = str(VariableAcceleration_Round)
                        CommandToChangeAcceleration_Str = str("M204 T" + VariableAcceleration_Str + " \n")
                        CommandToChangeAcceleration_Bytes = bytes(CommandToChangeAcceleration_Str, 'UTF-8') #set new acceleration
                        
                    #this section prepares the variables for the gradual decrease in speed  
                    IncrementGroupNumber_Int = (IncrementGroupNumber_Int+1)
                                        
                    #do it from maximum to minimum
                    while (IncrementGroupNumber_Int+1) > 0:
                        print("Current acceleration is " + VariableAcceleration_Str + " mm/s^2. ")
                        CurrentCycle_Int = int(1) #set current cycle_it back to one
                        
                        ser.write(CommandToChangeAcceleration_Bytes)
                        
                        while CurrentCycle_Int < (TotalNumberofCyclesPerIncrementGroup_Int+1): #this loop controls the number of cycles per Increment Group
                    
                            while CurrentPull < MaximumPull: #this loop controls the number of pulls per cycle
                                CurrentPull = (CurrentPull +1)
                                ser.write(PullCommand_Bytes)
                                GPIO.output(18,1) #TTL output high
                                GPIO.output(18,0) #TTL output low
                                ser.write(RestCommand_Bytes)
                                #time.sleep(0.5)
                                    
                            CurrentPull = (0) #resets the current pull back to zero so that the pull loop will recur
                            RemainingCycles_Int = int(TotalNumberofCyclesPerIncrementGroup_Int-CurrentCycle_Int)
                            RemainingCycles_Str = str(RemainingCycles_Int)
                            CurrentCycle_Str = str(CurrentCycle_Int)
                            CurrentCycle_Int = (CurrentCycle_Int+1) #having completed a cycle of pulls, increases cycle counter by one
                            time.sleep(1.0)
                            ser.write(ShortBeepSoundBytes) #makes a single bleeping noise to alert the user that a cycle has completed
                            print(CurrentCycle_Str + " cycles completed. " + RemainingCycles_Str + " cycles remaining. ") # prints information to the user to say that  a cycle has completed and how many cycles remain.
                            time.sleep(1.0)
                
                        IncrementGroupNumber_Int = (IncrementGroupNumber_Int-1) #increment group number logic goes here
                        VariableAcceleration_Round = round(MinimumAcceleration_Round+(IncrementValue_Round*(IncrementGroupNumber_Int)),3)
                        VariableAcceleration_Str = str(VariableAcceleration_Round)
                        CommandToChangeAcceleration_Str = str("M204 T" + VariableAcceleration_Str + " \n")
                        CommandToChangeAcceleration_Bytes = bytes(CommandToChangeAcceleration_Str, 'UTF-8') #set new acceleration
                 
                 
                #this bit needs to reset acceleration back to default of 1000mm/s^2 (M204 T) and the speed back to 100mm/s
                CommandToChangeAcceleration_Str = str("M204 T1000 \n")
                CommandToChangeAcceleration_Bytes = bytes(CommandToChangeAcceleration_Str, 'UTF-8') #restore default acceleration
                ser.write(CommandToChangeAcceleration_Bytes)
                ChangeSpeedTo100_Str = str("M203 X100 \n")
                ChangeSpeedTo100_Bytes = bytes(ChangeSpeedTo100_Str, 'UTF-8')
                ser.write(ChangeSpeedTo100_Bytes)
                print("Acceleration test now finished. Acceleration reset to default (1000 mm/s^2). Max travel speed reset to 100mm/s. ")
                print("Returning to main menu. ")
                    
                    
            #----------------------------------------------------------------------------------------------------------------------------#          
           
            
    elif UserMenuInput == "5": #this is the hybrid dynamic / static spindle stretching section
        print("")
        print("------------------------------------------------------------")
        print("")
        print("Welcome to the Hybrid Dynamic & Static Spindle Stretching section.")
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
            print("Moving to default starting position. This will take approximately 1 minutes. ")
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
            print("You entered "+UserManualGCodeInput + ". " + ArduinoChangeLine)
            ManualCommandInBytes = bytes((UserManualGCodeInput + " " + ArduinoChangeLine), 'UTF-8')
            ser.write(ManualCommandInBytes)     
            
        if UserManualGCodeInput in ["Continue", "continue"]:
            print("")
            print("------------------------------------------------------------")
            print("")
            print("Hook in position, continuing to stretch settings. ")
            print("")
            print("")
            TotalNumberofCycles_Str = input("How many cycles to carry out? (Each cycle takes 20 seconds to complete) ")
            TotalNumberofCycles_Int = int(TotalNumberofCycles_Str)
            print("")
            TravelDistancePerPull_Str = input("How far should the hook travel during one pull? (value in millimeters) ")
            print("")
            UserChoice_Str = input("Enter Y to begin or N to return to the main menu. ")
            ListofPositiveResponses = ["Y", "y", "Yes", "yes"]
                
            if UserChoice_Str in ListofPositiveResponses:
                #some declaration of variables before tugging!
                if StretchTravelDirection_Str == "Left":
                    PullCommand_Str = str("G1X-"+TravelDistancePerPull_Str+" \n")
                    PullCommand_Bytes = bytes(PullCommand_Str, 'UTF-8')
                    RestCommand_Str = str("G1X+"+TravelDistancePerPull_Str+" \n")
                    RestCommand_Bytes = bytes(RestCommand_Str, 'UTF-8')
                if StretchTravelDirection_Str == "Right":
                    PullCommand_Str = str("G1X+"+TravelDistancePerPull_Str+" \n")
                    PullCommand_Bytes = bytes(PullCommand_Str, 'UTF-8')
                    RestCommand_Str = str("G1X-"+TravelDistancePerPull_Str+" \n")
                    RestCommand_Bytes = bytes(RestCommand_Str, 'UTF-8')
                    
                ConvertToRelativeCoordinates_Str = str("G91 \n")
                ConvertToRelativeCoordinates_Bytes = bytes(ConvertToRelativeCoordinates_Str, 'UTF-8')
                ConvertToAbsoluteCoordinates_Str = str("G90 \n")
                ConvertToAbsoluteCoordinates_Bytes = bytes(ConvertToAbsoluteCoordinates_Str, 'UTF-8')
                    
                ShortBeepSound = str("M300 P10")
                ShortBeepSoundBytes = bytes((ShortBeepSound + " \n"), 'UTF-8')
                LongBeepSound = str("M300 P1000")
                LongBeepSoundBytes = bytes((LongBeepSound + " \n"), 'UTF-8')
                    
                CurrentCycle_Int = int(1)
                MaximumCycle = int(TotalNumberofCycles_Int)
                    
                #logic to pull and relax the lumbrical in cycles
                ser.write(ConvertToRelativeCoordinates_Bytes) #swap to relative coordinates is G91
                while CurrentCycle_Int < (MaximumCycle+1):
                        
                    #dynamic stimulus
                    ser.write(PullCommand_Bytes)
                    GPIO.output(18,1) #TTL output high
                    GPIO.output(18,0) #TTL output low
                    ser.write(RestCommand_Bytes)
                    time.sleep(2.0)
                        
                    #dynamic stimulus
                    ser.write(PullCommand_Bytes)
                    GPIO.output(18,1) #TTL output high
                    GPIO.output(18,0) #TTL output low
                    ser.write(RestCommand_Bytes)
                    time.sleep(2.0)
                        
                    #dynamic stimulus
                    ser.write(PullCommand_Bytes)
                    GPIO.output(18,1) #TTL output high
                    GPIO.output(18,0) #TTL output low
                    ser.write(RestCommand_Bytes)
                    time.sleep(2.0)
                        
                    #static stimulus
                    ser.write(PullCommand_Bytes)
                    GPIO.output(18,1) #TTL output high
                    GPIO.output(18,0) #TTL output low
                    time.sleep(10.0)
                    ser.write(RestCommand_Bytes)
                    time.sleep(2.0)
                        
                        
                    RemainingCycles_Int = int(MaximumCycle-CurrentCycle_Int)
                    RemainingCycles_Str = str(RemainingCycles_Int)
                    CurrentCycle_Str = str(CurrentCycle_Int)
                    print("Cycle " + CurrentCycle_Str + " complete. " + RemainingCycles_Str + " cycles remaining.")
                    CurrentCycle_Int = (CurrentCycle_Int+1) #having completed a cycle of pulls, increases cycle by one
                    time.sleep(1.0)
                    ser.write(ShortBeepSoundBytes)
                    time.sleep(1.0)
                    
                ser.write(ConvertToAbsoluteCoordinates_Bytes) #swap back to absolute coordinates = G90
                print("Maximum travel speed has been reset to 100mm/s. ")
                ChangeSpeedTo100_Str = str("M203 X100 \n")
                ChangeSpeedTo100_Bytes = bytes(ChangeSpeedTo100_Str, 'UTF-8')
                ser.write(ChangeSpeedTo100_Bytes)
                print("Acceleration has been reset to 1000mm/s^2. ")
                ChangeAccelTo1000_Str = str("M204 T1000 \n")
                ChangeAccelTo1000_Bytes = bytes(ChangeAccelTo1000_Str, 'UTF-8')
                ser.write(ChangeAccelTo1000_Bytes)
                print("All Cycles completed. Returning to Main Menu.")
                #exit to main menu
            
        
            
        elif UserManualGCodeInput in ["Main Menu", "main menu"]:
            print("You chose to return to the main menu. Returning to main menu. ")
    
    
    
    
    #------------------------------------------------------------#
        
    elif UserMenuInput == "9":
        print("------------------------------------------------------------")
        print("")
        print("For dynamic and static stretches, the hook will travel to the", StretchTravelDirection_Str,".")
        print("")
        print("To change stretch direction please type 'Left' or 'Right' and press enter.")
        ListofPossibleStretchDirections = ["Left", "L", "left", "Right", "R", "right"]
        UserDefinedStretchDirection = input()
        if UserDefinedStretchDirection in ListofPossibleStretchDirections:
            if UserDefinedStretchDirection in ["Left", "L", "left"]:
                StretchTravelDirection_Str = str("Left")
                print("Hook stretch direction now set to Left.")
                print("Returning to the main menu.")
                
            if UserDefinedStretchDirection in ["Right", "R", "right"]:
                StretchTravelDirection_Str = str("Right")
                print("Hook stretch direction now set to Right.")
                print("Returning to the main menu.")
            
        elif UserDefinedStretchDirection not in ListofPossibleStretchDirections:
              print("Invalid input. Returning to main menu.")
            
        print("------------------------------------------------------------")
        print("")
    
    #------------------------------------------------------------#
        
    elif UserMenuInput == "10":
        print("Exiting script and returning to Terminal.")
        ser.close()
        quit()

    #------------------------------------------------------------#
        
    elif UserMenuInput != "1" and UserMenuInput != "2" and UserMenuInput != "3" and UserMenuInput != "4" and UserMenuInput != "5" and UserMenuInput != "10":
        print("You entered an invalid input. Please try again.")
             

    #------------------------------------------------------------#


    #UserInput = raw_input("Enter the desired G-Code command and press the enter key.")
    #print(UserInput)
    #serial.write(UserInput)



#now it is 500. Whoops 735 now
