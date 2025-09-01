class Bank:
    def __init__(self,balance):
        self.balance=balance
        self.min_withdraw=100
        self.max_withdraw=10000

    def get_blance(self):
        return self.balance
    
    def deposit(self ,ammount):
        if ammount >0:
            self.balance+=ammount

    def withdraw(self , ammount ):
        if ammount<self.min_withdraw:
            print ( f"you can't withdraw under this {self.min_withdraw} ammonunt")
        elif ammount>self.max_withdraw:
            print( f"bank fokir hoy jabe")
        else :
            self.balance -=ammount
            print( "here is you money")
            print(f"you blance after withdraw {self.balance}")

dbbl=Bank(30000)
dbbl.withdraw(24)
dbbl.withdraw(300000)
dbbl.withdraw(4000)

