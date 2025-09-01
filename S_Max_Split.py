s = input().strip()

balance = 0
start = 0
parts = []

for i in range(len(s)):
    if s[i] == 'L':
        balance += 1
    else:  
        balance -= 1

    if balance == 0:
        parts.append(s[start:i+1])
        start = i + 1

print(len(parts))
for p in parts:
    print(p)
