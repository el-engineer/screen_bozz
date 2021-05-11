#!/usr/bin/env/ python3


#interface
import tkinter as tk
from tkinter import font as tkfont
from PIL import ImageTk,Image

#qrcode
import cv2
import numpy as np
from pyzbar.pyzbar import decode
import csv

import RPi.GPIO as GPIO
class custQLADZ:

    
    def __init__(self,first='NaN',last='NaN',email='NaN',userID='NaN'):
        self.first = first
        self.last = last
        self.email = email
        self.userID = userID
        self.exists = False



class webcam:
    def __init__(self,src=0):
        self.cam = cv2.VideoCapture(src)
        if not self.cam.isOpened():
            print("Unable to open the camera")
        self.cam.set(3,640)
        self.cam.set(4,480)
          
        
    def start(self):
        global currCust
        
        
        while self.stop:
                
            #reading using cam if not QR it is empty list
            success,img = self.cam.read()
            
            #decode scanned img and it has QR (this will start when it gets a QR or it wont)
            for barcode in decode(img):
                #get the userID from barcode var
                userID = barcode.data.decode('utf-8')
                
                #check if this userID exists in data base
                for cust in data:

                    #assign user data to the currect customer
                    currCust.first = cust[0]
                    currCust.last = cust[1]
                    currCust.email = cust[2]
                    currCust.userID = cust[3]

                    
                    #if QR matched data then exit this data loop
                    if userID == currCust.userID:
                        self.stop = False
                        currCust.exists = True
                        break
                        
                #if the detected barcode matched break this cam loop
                if currCust.exists:
                    break
                    
            cv2.imshow('Result',img)
            cv2.waitKey(1)
            
    def stopF(self):
        self.cam.release()
        cv2.destroyAllWindows()
        


class interQLADZ(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        #rasp resolution
        self.geometry('800x480')
        
        #program text
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        
        for F in (HomePage,ScanPage,InfoPage,confirmPage,loadingPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage")

    def getUserData(self,currCust):
        strr ='Name: ' + str(currCust.first) + ' ' + str(currCust.last) + '\nEmail: ' + str(currCust.email) + '\nUserID: ' + str(currCust.userID)
        return strr
    

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
        global cam
        global currCust
        flag = 1 
        
        if page_name == 'loadingPage':
            self.after(10000, self.show_frame, 'HomePage')
  
            #hardware turn on LED
            GPIO.output(40,GPIO.HIGH)
            
        if page_name == 'HomePage':
           
            #initialize(reset)
            currCust.exists = False
            

            #hardware turn off LED
            GPIO.output(40,GPIO.LOW)
     
        if page_name == 'ScanPage':
            cam.stop = True 
            cam.start()
            #turn off camera when getting user data and send it to infopage
            if currCust.exists:
                cam.stopF()
                self.after(0, self.show_frame, 'InfoPage')
                
                
class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Welcome to Screen-Bozz",font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        qrButton = tk.Button(self,text="Scan your QR code",
                            command=lambda: controller.show_frame("ScanPage"))
        
        payButton = tk.Button(self,text="Pay with cash")
        qrButton.pack()
        payButton.pack()
        

class ScanPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Please Scan your QR code",font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        

        backButton = tk.Button(self,text="Go back",
                            command=lambda: controller.show_frame("HomePage"))
        backButton.pack()
        print('scan')
        

class InfoPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Confirm your information",font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        global currCust
        
        #show user data
        strr = controller.getUserData(currCust)
        userLabel = tk.Label(self, text=strr,font=controller.title_font)
        userLabel.pack()

        confirmButton = tk.Button(self,text="Confirm",
                                command=lambda: controller.show_frame("confirmPage"))
        confirmButton.pack()
        
        backButton = tk.Button(self,text="Start Over",
                                command=lambda: controller.show_frame("HomePage"))
        backButton.pack()
        
class confirmPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Select your phone then start",font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        
        #implement hardware when confirmButtom is clicked (required self because of garbage collection)
        self.phone1 = ImageTk.PhotoImage(Image.open('./images/phone1.png'))
        self.phoneClick1 = ImageTk.PhotoImage(Image.open('./images/phone1-2.png'))
        self.phone2 = ImageTk.PhotoImage(Image.open('./images/phone2.png'))
        self.phoneClick2 = ImageTk.PhotoImage(Image.open('./images/phone2-2.png'))
        self.phoneButt1 = tk.Button(self,image=self.phone1,command=lambda *args: self.setSize(1))
        self.phoneButt2 = tk.Button(self,image=self.phone2,command=lambda *args: self.setSize(2))
        self.phoneButt1.pack()
        self.phoneButt2.pack()
        
        confirmButton = tk.Button(self,text="Start Screen Chaning",
                                command=lambda: [controller.show_frame("loadingPage"),self.resetButtons()])
        confirmButton.pack()
        
        backButton = tk.Button(self,text="Go back",
                                command=lambda: [controller.show_frame("InfoPage"),self.resetButtons()])
                                                     
        backButton.pack()
        print('confirm')
        
    def setSize(self,size):
        global phoneSize
        #make sure the other one is not display as selected
        self.resetButtons()
        
        if size == 1:
            phoneSize = 10
            self.phoneButt1["image"] = self.phoneClick1
            
        elif size == 2:
            phoneSize = 12
            self.phoneButt2["image"] = self.phoneClick2
    
    def resetButtons(self):
        self.phoneButt1["image"] = self.phone1
        self.phoneButt2["image"] = self.phone2
        
class loadingPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Processing",font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)


        
#global values
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)
GPIO.output(40, GPIO.LOW)
phoneSize = 0
cam = webcam()
currCust = custQLADZ()
data = []

with open('fdata.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        data.append(row)


  
if __name__ == "__main__":
    app = interQLADZ()
    app.mainloop()