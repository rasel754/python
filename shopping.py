class Shopping:
    shoppingMall="jamuna"

    def __init__(self,buyer):
        self.buyer=buyer
        self.cart=[] 
    
    def add_to_cart(self , item , price , quantity):
        product={'item':item , 'price':price , 'quantity':quantity}
        self.cart.append(product)

    def checkout(self , ammount):
        total=0
        for item in self.cart:
            total+=item['price']*item['quantity']
        print("total price is : ",total)
        if ammount<total:
            print(f"please provide {total-ammount} more")
        else:
            extra=ammount-total
            print(f"here is your product and {extra} money")


rasel=Shopping("rasel")
rasel.add_to_cart('alu',53,5)
rasel.add_to_cart('klu',63,6)
rasel.add_to_cart('jlu',73,54)
rasel.add_to_cart('ylu',93,59)

print(rasel.cart)
rasel.checkout(11000)