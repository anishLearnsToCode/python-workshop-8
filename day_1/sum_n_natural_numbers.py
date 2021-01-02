"""
N: int
0: 0
1: 1
2: 1 + 2 = 3
n: 1 + 2 + 3 + ... + n
"""

n = int(input())
i = 1
result = 0

while i <= n:
    result += i
    i += 1

print(result)
