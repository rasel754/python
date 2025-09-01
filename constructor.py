class Phone:
    manufacture ="Bangladesh"

    def __init__(self,owner,brand,price):
        self.owner=owner
        self.brand=brand
        self.price=price

    def send_sms(self,phn , sms):
        txt=f"sending meessage on {phn} text is : {sms}"
        return txt
    
myPhone=Phone("rasel" , "xiomi",45000)
print(myPhone.brand,myPhone.owner,myPhone.price)

herPhone=Phone("she is" , "iphone",985000)
print(herPhone.brand,herPhone.owner,herPhone.price)