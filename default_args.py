def sum(nm1 , nm2 ,nm3=0,nm4=0):
    result = nm1+nm2+nm3+nm4
    return result

total=sum(45 , 98 ,45)
# print(total)

# args
def all_sum(nm1 , nm2 , *numbers):
    print(numbers)
    sum=0
    for num in numbers:
        print(sum)
        sum=sum+num
    return sum

total = all_sum(20,40,50,60,10,90)
print("total: " , total)