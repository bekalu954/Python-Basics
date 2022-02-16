#Assignment 4-1
#Coding Exercise 8:

# 1.Create a function func() which prints a text ‘Hello World’
from multiprocessing.sharedctypes import Value


def my_func():
    print("Hello World")
my_func()
# 2.Create a function which func1(name)  
# which takes a value name and prints the output “Hi My name is Google’
def my_func1(name:str):
    print('Hi My name is', name)
my_func1 ('Google')
# 3.Define a function func3(x,y,z) that takes three arguments x,y,z 
# where z is true it will return x and when z is false it should return y . 
# func3(‘hello’goodbye’,false)

def my_func3(x,y,z):
    if z:
        return x
    else:
        return y
my_func3('hello','goodbye',False)


# 4.define a function func4(x,y) which returns the product of both the values.

def my_func4(x,y,):
    return x * y
print (my_func4(4,5))

# 5.define a function called as is_even that takes one argument , 
# which returns true when even values is passed and false if it is not.

def my_func5(x):
    if x % 2 == 0:
        return "Even"
    else:
        return "Odd"
x = int(input("Enter a number:"))
print(my_func5(int(x)))

# 6.define a function that takes two arguments ,and 
# returns true if the first value is greater than the second value and 
# returns false if it is less than or equal to the second.
def my_func6(x,y):
    if x > y:
        return True
    else:
        return False
print(my_func6(9, 8))
print(my_func6(8, 9))

# 7.Define a function which takes arbitrary number of arguments and returns the sum of the arguments.

def my_func7(*num):
    total = 0
    for i in num:
        total += i
    return total
print(my_func7(1,2,3,4,5))

# 8.Define a function which takes arbitrary number of arguments and 
# returns a list containing only the arguments that are even.

def my_func8(*args):
    return [nums for nums in args if nums % 2 == 0]
print(my_func8(1,2,3,4,5,6,7,8))

# 9.Define a function that takes a string and returns a matching string 
# where every even letter is uppercase and every odd letter is lowercase 

def my_func9(value):
    letters = ''
    for i in range(0,len(value)):
        if i % 2 == 0:
            letters += value[i].upper()
        else:
            letters += value[i].lower()
    return letters
print(my_func9('python'))

# 10.Write a function which gives lesser than a given number if both the numbers are even, 
# but returns greater if one or both or odd.

def my_func10(x,y):
    if x % 2 == 0 and y % 2 == 0:
        return min(x,y)
    else:
        return max(x,y)
print(my_func10(4,6))
print(my_func10(1,2))

# 11.Write a function which takes  two-strings and 
# returns true if both the strings start with the same letter.

def my_func11(x,y):
    if x[0] == y[0]:
        return True
    else:
        return False
print(my_func11('string', 'st-ring'))

# 12.Given a value,return a value which is twice as far as other side of 7

def my_func12(x):
    return x ** 2
print(my_func12(7))

# 13.A function that capitalizes first and fourth character of a word in a string.

def my_func13(value):
    if value == '':
        return None
    elif len(value) == 1:
        return value.upper()
    elif len(value) < 4:
        return value[0].upper() + value[1:]
    else:
        return value[0].upper() + value[1:3] + value[3].upper() + value[4:]
print(my_func13(''))
print(my_func13('tem'))
print(my_func13('common'))

#Assignment 4-2
#Coding Exercise 9:

# 1.Imagine an accounting routine used in a book shop. 
# It works on a list with sublists, which look like this: 
'''
Order Number	Book Title and Author	        Quantity	Price per Item
34587	        Learning Python, Mark Lutz	        4	    40.95
98762	        Programming Python, Mark Lutz	    5	    56.80
77226	        Head First Python, Paul Barry	    3	    32.95
88112	        Einführung in Python3, Bernd Klein	3	    24.99
'''

# 2.Write a Python program, which returns a list with 2-tuples. 
# Each tuple consists of a the order number and the product of the price per items and the quantity. 
# The product should be increased by 10,- € if the value of the order is smaller than 100,00 €. 
# Write a Python program using lambda and map.

orders =[[34587, "Learning Python, Mark Lutz", 4, 40.95],
        [98762, "Programming Python, Mark Lutz", 5, 56.80],
        [77226, "Head First Python, Paul Barry", 3,32.95],
        [88112, "Einführung in Python3, Bernd Klein", 3, 24.99]]

#using lambda and map
output = list(map(lambda x: (x[0], x[2] * x[3] + 10) if (x[2] * x[3] < 100) else x[0] * x[2] * x[3], orders))
print(output)

# 3.The same bookshop, but this time we work on a different list. 
# The sublists of our lists look like this: 
# [ordernumber, (article number, quantity, price per unit), ... (article number, quantity, price per unit) ] 
# Write a program which returns a list of two tuples with (order number, total amount of order).

orders =[[34587, ("Learning Python, Mark Lutz", 4, 40.95)],
        [98762, ("Programming Python, Mark Lutz", 5, 56.80)],
        [77226, ("Head First Python, Paul Barry", 3,32.95)],
        [88112, ("Einführung in Python3, Bernd Klein", 3, 24.99)]]

output = list(map(lambda x: (x[0], x[1][1] * x[1][2] + 10) if (x[1][1] * x[1][2] < 100) else (x[0], x[1][1] * x[1][2]), orders))
print(output)