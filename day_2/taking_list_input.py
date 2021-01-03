"""
2 3 5 7 11
[2, 3, 5, 7, 11]
"""

numbers = input()
print(numbers)
print(type(numbers))

numbers = numbers.split()
print(numbers)

for index in range(0, len(numbers)):
    numbers[index] = int(numbers[index])

print(numbers)
