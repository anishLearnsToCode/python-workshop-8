"""
Functions
def function_name(parameter_1, parameter_2....):
    code
    code
    return value_1, value_2 ...
"""


def hello():
    print('hello world')


def helloWorld(message):
    print('hello ' + message)


def sumNumbers(a, b):
    return a + b


def full_name(first_name, last_name, middle_name=''):
    if len(middle_name) == 0:
        return first_name + ' ' + last_name
    else:
        return first_name + ' ' + middle_name + ' ' + last_name


print(full_name('anish', 'sachdeva'))
print(full_name('wolfgang', 'mozart', middle_name='amadeus'))
print(full_name('lady', 'lovelace', 'ada'))
print(full_name(last_name='bach', first_name='johannas'))

print('message', end=' ** ')
