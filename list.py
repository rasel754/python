# index  0   1  2  3  4  5  6  7  8  9
numbers=[10,20,30,40,50,60,70,80,90,100]
# index -10 -9 -8 -7 -6 -5 -4 -3 -2  -1
print(numbers[3] , numbers[-3])
# divided list (star , end )
print(numbers[2:7])

# list(star , end , step)
print(numbers[2:7:1])
print(numbers[2:7:2])

# reverse way 
print(numbers[7:2:-1])
print(numbers[7:2:-2])#2 step kore jabe
print(numbers[7:])#7 theke last a jabe
print(numbers[:4])#first theke 4th age porjnto jabe
print(numbers[:])#puro ta print hobe
print(numbers[::-1])#reverse print hobe