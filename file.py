# with open("message.txt","w") as file:
#     file.write("i love my self not you")

# with open("message.txt","a") as file:
#     file.write("i love my self not you")

with open("message.txt","r") as file:
    text=file.read()
    print(text)