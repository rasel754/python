numbers=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
numbers.append(56)
print(numbers)

numbers.insert(3,71)
print(numbers)

numbers.remove(100)
print(numbers)

if 90 in numbers:
    numbers.remove(90)
print(numbers)

last =numbers.pop()
print(last)
sort_list =numbers.sort()
print(numbers)