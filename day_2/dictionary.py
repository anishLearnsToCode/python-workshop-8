"""
Dictionary
index --> value
int (0, n) --> anything

anything --> anything
hashmap / map/ dictionary

{}

- mutable
- iterable

key: value
unique --> non unique
"""

words = {
    'i': 350,
    'am': 350,
    'batman': 20
}

# print(type(words))
# print(words)
# print(len(words))

# checking key present in dict
# print('Hello' in words)

# accessing elements
# print(words['am'])
print(words.get('hello', 0))

# Updating Values
words['batman'] = 100
print(words)

# insert a new value inside my dictionary
words['hello'] = 98
print(words)

# removing value from dictionary
del words['i']
print(words)
