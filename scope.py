balance=3000

def buy_things(item,price):
    wantPhone="iphone"#
    global balance
    print(f"before buy : ",balance)
    balance=balance-price
    print(f"after buying {item} :",balance)

buy_things("iphone" , 1000)
print("global balance after buy : ",balance)