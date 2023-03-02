# This python file is for the Learn Python Intermediate course on Udemy
# DO NOT RUN AS A PROGRAM
# this file is for notes only

# Fundamental Data Types
# int and float
# Arithmetic Operators
print(type(2 + 4))
print(type(2 - 4))
print(type(2 * 4))
print(type(2 / 4))  # 0.5

# exponentiation
print(2 ** 3)  # 2 * 2 * 2 = 8

# floor division
print(5 // 4)  # 1

# modulo operator
print(6 % 4)  # 2

# math functions
print(round(3.9))
print(abs(-20))

# operator precedence
print((20 - 3) + 2 ** 2)


# PEMDAS
# () first
# ** second
# * / // % third
# + - fourth


# bin() and complex() functions
# bin functions
print(bin(5))

# complex functions
print(int('0b101', 2))


# variables

user_iq = 190
user_age = user_iq / 4

print(user_iq)
print(user_age)

# constants
PI = 3.14

# do not use __ notation with variables

a, b, c = 1, 2, 3

a = 1

print(a)
print(b)
print(c)


# expressions and statements

iq = 100
user_age = iq / 5


# augmented assignment operator
some_value = 5
some_value *= 2
print(some_value)

# strings
# strings are immutable
# strings are ordered
# strings can be indexed
# strings can be sliced
# strings can be concatenated
# strings can be repeated
# strings can be escaped
# strings can be formatted
# strings can be raw
print(type('hi hello there 24'))
username = 'supercoder'
password = 'supersecret'

# long strings
long_string = '''
WOW
0 0
___
'''
print(long_string)
first_name = 'John'
last_name = 'Smith'
full_name = first_name + ' ' + last_name
print(full_name)

# string concatenation
print('hello' + ' ' + 'world')

# type conversion
print(type(int(str(100))))
# or
a = str(100)
b = int(a)
c = type(b)
print(c)


# escape sequences
weather = '\t It\'s \"kind of\" sunny \n hope you have a good day'
print(weather)

# formatted strings
name = 'John'
age = 55
print(f'hi {name}. You are {age} years old.')

# string indexes
selfish = '01234567'
# [start:stop:stepover]
print(selfish[0:8:2])
# [start:stop:stepover]
print(selfish[0:])
# [start:stop:stepover]
print(selfish[:8])
# [start:stop:stepover]
print(selfish[::2])
# [start:stop:stepover]
print(selfish[::-1])

# immutability
# selfish[0] = '9'
# print(selfish)

# built in functions + methods
quote = 'to be or not to be'
print(len(quote))
print(quote.upper())
print(quote.capitalize())
print(quote.find('be'))
print(quote.replace('be', 'me'))

# booleans
# True
# False
# None
name = 'John Smith'
is_cool = False
is_cool = True

# bool function
print(bool(0))
print(bool(1))
print(bool(''))
print(bool('hello'))
print(bool([]))
print(bool([0, 1, 2]))
print(bool({}))
print(bool({1: 'a'}))
print(bool(None))

# type conversion
name = 'John Smith'
age = 20
relationship_status = 'single'
relationship_status = 'it\'s complicated'
print(relationship_status)

birth_year = input('What year were you born? ')
age = 2023 - int(birth_year)
print(f'Your age is: {age}')

# password checker

username = input('Enter your username: ')
password = input('Enter your password: ')
passwordlength = len(password)

print(f'{username}, your password {"*" * passwordlength} is {passwordlength} characters long')

# lists
# ordered
# iterable
# mutable
# can contain different data types
# can contain duplicates
# can be indexed and sliced
# can be concatenated and repeated
# can be sorted     .sort()
# can be reversed   .reverse()
# can be joined     .join()
# can be appended   .append()
# can be popped     .pop()
# can be removed    .remove()
# can be inserted   .insert()
# can be cleared    .clear()
# can be reversed   .reverse()
# can be copied     .copy()
# can be extended   .extend()
# can be counted    .count()
# can be indexed    .index()
# can be sliced     [start:stop:stepover]

# list

amazon_cart = ['notebooks', 'sunglasses']
print(amazon_cart[2])

# list slicing

amazon_cart = ['notebooks',
               'sunglasses',
               'toys',
               'grapes'
               ]

amazon_cart[0] = 'laptop'
new_cart = amazon_cart[:]
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)

# matrix
matrix = [
    [1, 5, 1],
    [0, 1, 0],
    [1, 0, 1]
]

print(matrix[0][1])

# list methods
basket = [1, 2, 3, 4, 5]
print(len(basket))

# list methods
basket = [1, 2, 3, 4, 5]

# adding to the end of a list
basket.append(100)
new_list = basket
print(new_list)  # [1, 2, 3, 4, 5, 100]

# adding to the beginning of a list
basket.insert(5, 100)
new_list = basket
print(new_list)  # [1, 2, 3, 4, 5, 100, 100]

# extending a list
basket.extend([100, 101])
new_list = basket
print(new_list)  # [1, 2, 3, 4, 5, 100, 100, 100, 101]

# popping from a list
basket.pop()
basket.pop(0)
new_list = basket
print(new_list)  # [2, 3, 4, 5, 100, 100, 100]

# removing from a list
basket.remove(5)
new_list = basket
print(new_list)  # [2, 3, 4, 100, 100, 100]

# clearing a list
basket.clear()
new_list = basket
print(new_list)  # []

# index of an item in a list
basket = ['a', 'b', 'c', 'd', 'e']

print(basket.index('d'))  # 3

# is an item in a list

print('d' in basket)  # True
print('x' in basket)  # False

# count of an item in a list
basket = ['a', 'b', 'c', 'd', 'e', 'd']
print(basket.count('d'))  # 2

# sorting a list
basket = ['a', 'x', 'b', 'c', 'd', 'e', 'd']
# basket.sort()
new_basket = basket[:]
new_basket.sort()
print(new_basket)  # ['a', 'b', 'c', 'd', 'd', 'e', 'x']
print(sorted(basket))  # ['a', 'b', 'c', 'd', 'd', 'e', 'x']
print(basket)  # ['a', 'x', 'b', 'c', 'd', 'e', 'd']

# copying a list
basket = ['a', 'x', 'b', 'c', 'd', 'e', 'd']
new_basket = basket.copy()
print(new_basket)  # ['a', 'x', 'b', 'c', 'd', 'e', 'd']

# reversing a list
basket = ['a', 'x', 'b', 'c', 'd', 'e', 'd']
basket.sort()
basket.reverse()
print(basket)  # ['x', 'e', 'd', 'd', 'c', 'b', 'a']

# range
print(list(range(1, 100)))

# joining lists
new_sentence = ' '.join(['hi', 'my', 'name', 'is', 'Sarah'])

print(new_sentence)

# list unpacking
a, b, c, *other = [1, 2, 3]

print(a)
print(b)
print(c)
print(other)

# None - absence of value or data

# Dictionary
dictionary = {
    'a': 1,
    'b': 2,
    'c': 3
}

print(dictionary['b'])

# Dictionary
# unordered key value pairs

# dictionary = {key: value for key, value in dictionary.items()}

dictionary = {
    'weapons': [1, 2, 3],
    'greeting': 'hello',
    'is_Magic': True
}


print(dictionary.keys())  # ['123', 'b', 'c', 'x']
print(dictionary.values())  # [1, 2, 3, True]
# [('123', [1, 2, 3]), ('b', 'hello'), ('c', 3), ('x', True)]
print(dictionary.items())

user = {
    'basket': [1, 2, 3],
    'greet': 'hello',
    'age': 20
}

print(user.get('age'))  # 20

print('basket' in user)  # True

print('age' in user.keys())  # True
print('hello' in user.values())  # True
user.clear()
print(user)  # None

user2 = dict(name='JohnJohn')
print(user2)  # {'name': 'JohnJohn'}

user.update()  # updates the dictionary values with the new values

# Tuples
# immutable

my_tuple = (1, 2, 3, 4, 5)
print(5 in my_tuple)  # True

# why tuples vs lists?
# tuples are immutable
# lists are mutable
# faster than lists
# when we don't want to modify the list, we can use tuples

# sets
# immutable
# unordered collection of unique objects
# no duplicate values
# no indexing in sets

my_list = [1, 2, 3, 4, 5, 5]
# convert to set
set(my_list)  # {1, 2, 3, 4, 5}

my_set = {1, 2, 3, 4, 5}
# convert to list
list(my_set)  # [1, 2, 3, 4, 5]

my_set = {1, 2, 3, 4, 5}
# 4 through 10
your_set = {4, 5, 6, 7, 8, 9, 10}

# .difference
# .discard
# .difference_update
# .difference_update()
# .intersection()
# .isdisjoint()
# .issubset()
# .issuperset()
# .union()

# Conditional Logic

if condition:
    return result
elif condition:
    return result
# else
else:
    return else_result

is_old = input('Are you 18 or over?')
is_licensed = input('Are you licensed?')

if is_old == 'yes' and is_licensed == 'yes':
    print('You meet the requirements!')
else:
    print('Sorry, you do not meet the requirements!')
