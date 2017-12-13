from turtle import *

def draw_star(x, y, length):
    goto(x, y)
    for i in range(5):
        right(144)
        forward(length)

draw_star(2, 3, 100)

mainloop()
