"""
map(func, iterable)
item_1 --> func(item_1)
item_2 --> func(item_2)
item_3 --> func(item_3)
item_4 --> func(item_4)

"""

result = list(map(int, input().split()))
print(type(result))
print(result)


# for element in result:
#     print(element)
