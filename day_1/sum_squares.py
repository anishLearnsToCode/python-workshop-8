"""
N: int
n: 1^2 + 2^2 + 3^2 + ... + n^2
0: 0
1: 1
"""

n = int(input())

i = 1
result = 0

while i <= n:
    result += i ** 2
    i += 1

print(result)

"""
n = 3
i = 4
result = 0 + 9 
"""
