import qrcode

#customer Class
class custQLADZ:

    totalCust = 0
    
    def __init__(self,first,last,email):
        self.first = first
        self.last = last
        self.email = email
        self.userID = self.idFunc()
        custQLADZ.totalCust += 1 #increment customers
        
        
    def idFunc(self):
        newID = self.first[:3] +  self.last[:3].lower()
        return newID
        
#generate QR and save, takes in obj                
def generateQR(userObj):

    #QRCode class
    qr = qrcode.QRCode(
        version= 1,
        error_correction=qrcode.constants.ERROR_CORRECT_M, #default, if not provide it is set
        box_size = 25,
        border = 10
    )
    
    data = userObj.userID
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black',back_color='white')
    img.save(data+'.png')

def createCust():
    first = input('Enter your first name: ')
    last = input('Enter your last name: ')
    email = input('Enter your email: ')
    cust1 = custQLADZ(first,last,email)
    generateQR(cust1)
    print('Welcome to QLADZ community, ' + first)


createCust()