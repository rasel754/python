import sys
from collections import defaultdict

def solve():
    data = sys.stdin.read().split()
    n = int(data[0])
    a = list(map(int, data[1:1+n]))
    
    freq = defaultdict(int)
    for num in a:
        freq[num] += 1
        
    removals = 0
    for num, count in freq.items():
        if count < num:
            removals += count
        elif count > num:
            removals += (count - num)
            
    print(removals)

solve()