from random import *



point = 0
loop = True

while True:
    point += 1
    if point <= 3:
        x = randint(0, 10)
        y = randint(0, 10)
        error  = randrange(-1,2)
        result = x + y + error
        print(x, '+', y, '=', result)

        answer = input ('Y/N').upper()
        if answer == "Y":
            if result == x + y:
                print ('Yay')
            else:
                print ('Nay')
                loop = False
        else:
            if result == x + y:
                print('Nay')
                loop = False
            else:
                print('Yay')
    else:
        print('Game over, your score is', point)
        break
