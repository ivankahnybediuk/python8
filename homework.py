"""
Write a function called oops that explicitly raises an IndexError exception when called. Then write another function that calls oops inside a try/except state­ment to catch the error. What happens if you change oops to raise KeyError instead of IndexError?
"""
def oops():
    raise IndexError


def get_error():
    try:
        oops()
    except IndexError:
        print("Its IndexError")
def get_an_error():
    try:
        oops()
    except KeyError:
        print("Its IndexError")

get_error()
get_an_error()

"""
Task 2

Write a function that takes in two numbers from the user via input(), call the numbers a and b, and then returns the 
value of squared a divided by b, construct a try-except block which raises an exception if the two values given by the 
input function were not numbers, and if value b was zero (cannot divide by zero).    
"""
def get_count (a, b):
    if type_check(a, b):
        a = int(a)
        b = int(b)
        try:
            print((a * a) / (b * b))
        except ZeroDivisionError:
            print("Нельзя делить на ноль!!")


def type_check(a, b):
    if a.isdigit() and b.isdigit():
        return True
    else:
        try:
            raise TypeError
        except TypeError:
            print ("Это не число!")

a = input("Первое число: \n")
b = input("Второе число: \n")

get_count(a, b)