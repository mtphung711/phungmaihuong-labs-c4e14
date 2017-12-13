from random import *
from calc import *

def generate_quiz():
    x = randint(0,10)
    y =  randint(1,10)
    op = choice(['+', '-', '*', '/'])
    error = randint(-1,1)
    result = evaluate(x, y, op) + error
    # Hint: Return [x, y, op, result]
    return [x, y, op, result]

def check_answer(x, y, op, result, user_choice):
    true_result = evaluate(x, y, op)
    expected_choice = true_result == result
    return user_choice == expected_choice
