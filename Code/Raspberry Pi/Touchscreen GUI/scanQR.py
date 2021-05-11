#decode the QR and check if match the data base
import cv2
import numpy as np
from pyzbar.pyzbar import decode

def runScanner():
    #img = cv2.imread('Suptha.png')
    cap = cv2.VideoCapture(0)
    #screen size
    cap.set(3,640)
    cap.set(4,480)

    #while cam is on and scanning
    while True:

        #reading using cam if not QR it is empty list
        success,img = cap.read()
        
        #decode scanned img and it has QR
        for barcode in decode(img):
            #get the userID from barcode var
            userID = barcode.data.decode('utf-8')
            
            #check if this userID exists in data base 
            if(userID == 'Suptha'):
                print('Scanning success')
                break
                
        # same thing but only works with a picture not cam
        # code = decode(img)
        # userID = code[0].data.decode('utf-8')
        
            
        cv2.imshow('Result',img)
        #cv2.waitKey() is a keyboard binding function. Its argument is the time in milliseconds. 
        #The function waits for specified milliseconds for any keyboard event.
        cv2.waitKey(1)

    #leasing the handle to the webcam
    cap.release()
    cv2.destroyAllWindows()