# CACH 1
# import calc
#
# result = calc.evaluate(1, 2, '*')
#
# print(result)

# CACH 2
# from calc import evaluate
#
# result = evaluate(1, 2, '*')
# print(result)

#CACH 3
# from calc import *
#
# result = evaluate(1, 2, '*')
# print(result)

from calc import *
from random import *

x = randint(0,10)
y = randint(1, 10)
op = choice(["+"] * 50 + ['-'] * 25 + ['*'] * 10 + ['/'] * 15)
error = randint(-1,1)
result = evaluate(x, y, op) + error
print("{0} {1} {2} = {3}".format(x, op, y, result))

answer = input('Your answer: (Y/N)?').upper()
if 'Y' in answer:
    if error == 0:
        print('Yay')
    else:
        print('Nay')
else:
    if error == 0:
        print('Nay')
    else:
        print('Yay')
