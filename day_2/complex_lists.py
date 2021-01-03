def square(x: int) -> int:
    return x ** 2

complex_list = [True, 1, 3.14, 2.71828, 'hello world', print, range(1, 10, 2), [3, 4, 5], square]

# for element in complex_list:
#     print(type(element))

a = print
# a('this is print')
# print('this is also print')
# complex_list[5]('this is also also print')

# complex_list[5](square(10))
# complex_list[5](complex_list[-1](10))

# print(complex_list[-3])

complex_list[-2].append(100)
complex_list[-2].append(0)
complex_list[-2].append(-98)

print(complex_list)

# for number in complex_list[-3]:
#     print(number)
