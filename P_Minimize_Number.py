n = int(input())
arr = list(map(int, input().split()))
count = 0
while all(num % 2 == 0 for num in arr):
    arr = [num // 2 for num in arr]
    count += 1
print(count)