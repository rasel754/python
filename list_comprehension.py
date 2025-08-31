numbers =[45 , 87 , 96 , 65 , 43 , 90 , 85 , 14 ,26 ,61 ,70]
odd_num=[]
for num in numbers:
    if num%2==1 and num%5==0:
        odd_num.append(num)

print(odd_num)

# uporer same kaj ta ek line a kora jay
oddNum =[num for num in numbers if num%2==1 if num%5==0]
print(oddNum)