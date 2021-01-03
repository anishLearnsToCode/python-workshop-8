import random

a, b = -100, 100
# print(int(random.random() * (b - a) + a))
print(random.randint(a, b))

"""
(0, 1) * (b - a) + a
(0, b - a) + a
(a, b)
"""
