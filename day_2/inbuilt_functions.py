def abs(x: str) -> float:
    return x if x > 0 else -x


# print(abs(10))
# print(abs(-10))

x = set()
# print(type(x))

x.add(10)
x.add(10)
x.add(10)

# print(x)
# print(len(x))

# print([ord(character) for character in input()])

# print(x.__repr__())
# var = map(int, input().split())
# print(var)

n = int(input())
print(sum(x ** 2 for x in range(1, n + 1)))
