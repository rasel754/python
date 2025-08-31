# value in pair or object call dictionary 
# {key:value}pair
person={"name":"rasel","address":"chandpur","age":24,"work":"student"}
print(person)
print(person["address"])
print(person.keys())
print(person.values())


# special dictionary loop
for key , value in person.items():
    print(key,value)