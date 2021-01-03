"""
{x | x in (-10, 10)}
{x^2 | x in (1, 10)}

[g(x) for x in iterable]
"""


def square(x: int) -> int:
    return x ** 2


# numbers = [square(x) for x in range(1, 21)]
# print(numbers)

# name = input()
# letters = [character for character in name]
# print(letters)


generator = [x ** 2 for x in range(-5, 5)]
print(generator)
print(type(generator))
