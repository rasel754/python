def full_name(first , second):
    name = f"full name is : {first} {second}"
    return name
# take perameters in order(je perameter age asbe se age bosbe)
# name =full_name("rasel","ahmed")
name = full_name(second="ahmed" , first= "rasel")
# print(name)


# def famous(**kargs)
def famous_name(frist , last , **aditional):
    name=f"{frist} {last}"
    # print(aditional["title"])
    for key , value in aditional.items():
        print(key , value)
    return name

name=famous_name(frist="rasel" , last="ahmed" ,title="shoel" , aditional="rana")
# print(name)