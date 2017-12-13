from random import *

point = 0
loop = True

ops = ['+', '-', '*', '/']

while True:
    point += 1
    if point <= 10:
        x = randint(0, 10)
        y = randint(1, 10)
        error  = randrange(-1,2)
        op = choice(ops)
        if op == '+':
            result = x + y + error
            print(x, '+', y, '=', result)
        elif op == '-':
            result = (x - y) + error
            print(x, '-', y, '=', result)
        elif op == '*':
            result = (x * y) + error
            print(x, '*', y, '=', result)
        else:
            result = (x / y) + error
            print(x, '/', y, '=', result)

        answer = input ('Y/N').upper()
        if answer == "Y":
            if error == 0:
                print ('Yay')
            else:
                print ('Nay')
                loop = False
        else:
            if error == 0:
                print('Nay')
                loop = False
            else:
                print('Yay')
    else:
        print('Game over, your score is', point)
        break
