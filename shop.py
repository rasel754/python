class Shop:
    cart=[]#cart is a class attribute

    def __init__(self,buyer):
        self.buyer=buyer
    
    def add_to_cart(self , item):
        self.cart.append(item)
         
rasel=Shop("rasel ahmed")
rasel.add_to_cart("phone")
rasel.add_to_cart("laptop")
print(rasel.cart)


milon=Shop('milon')
milon.add_to_cart("mouse")
milon.add_to_cart("keyboard")
print(milon.cart)

