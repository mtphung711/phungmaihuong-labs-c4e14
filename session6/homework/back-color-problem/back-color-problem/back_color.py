from random import *
from srs_ex_11 import *

shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]


def get_shapes():
    return shapes


def generate_quiz():
    text = choice(["RED", "GREEN", "BLUE", "YELLOW"])
    color = choice(["#3F51B5", "#C62828", "#FFD600", "#4CAF50"])
    quiz_type = randint(0, 1)
    return [text, color, quiz_type]

def mouse_press(x, y, text, color, quiz_type):
    if quiz_type == 0:
        for shape in shapes:
            position = is_inside([x, y], shape['rect'])
            if text == shape['text'].upper():
                if position == True:
                    return True
                else:
                    return False
    if quiz_type == 1:
        for shape in shapes:
            position = is_inside([x, y], shape['rect'])
            if color == shape['color']:
                if position == True:
                    return True
                else:
                    return False
