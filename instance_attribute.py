class Shop:
    shoppingMall="jamuna"

    def __init__(self,buyer):
        self.buyer=buyer
        self.cart=[] #cart is a instance attribute
    
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

mahi=Shop("mahi")
mahi.add_to_cart("ssd")
mahi.add_to_cart("gamming display")
print(mahi.cart)
