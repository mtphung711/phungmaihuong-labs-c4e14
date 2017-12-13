from random import *


def add(x, y): #no argument
    print(x + y)

def evaluate(x, y, op):
    if op == '+':
        result = x + y
    elif op == "-":
        result = x - y
    elif op == '*':
        result = (x * y)
    else:
        result = (x / y)
    return result #khong bao gio print trong function, result la de dua cho user

# x = randint(0,10)
# y = randint(1,10)
# op = choice(["+","-","*", "/"])
# z = evaluate(1, 2, '+')
# print(x, y, op)
# print(z)
# print (z + randint(-1, 1))

# print(__name__)


# add(3, 4) #passing argument
# add(6, 3)
#
# a = 7
# b = 5
# add(a,b)
# add(7, a)
