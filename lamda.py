# lamda holo function ar shorcut form

# def double (x):
#     return x*2

double=lambda num:num*2

# print(double(44))

add = lambda a,b:a+b
# print(add(33,98))

numbers=[12 ,23,34,32,34,12,89,98,89]
double_numers=map(double,numbers)
print(numbers)
print(list(double_numers))