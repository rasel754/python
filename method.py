def call():
    print("calling someone i don't know")
    return "call done"

class Phone:
    name="samsung"
    color="black"
    price=20000
    fetures=["speaker" , "valo camera ", "nokia power"]

    def call(self):
        print("call one person")

    def send_sms(self,phn , sms):
        txt=f"sending meessage on {phn} text is : {sms}"
        return txt
    
myPhone=Phone()

myPhone.call()
res=myPhone.send_sms(43211,"hey there")
print(res)
