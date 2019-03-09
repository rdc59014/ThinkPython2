import turtle
from mypolygon import polygon
import math


def one_piece(t, length):
    polygon(t, length, 3)
    t.lt(60)


def pie(t, m, length):
    length = 2 * math.pi * length / m
    for i in range(m):
        one_piece(t, length)


if __name__ == '__main__':
    bob = turtle.Turtle()

    pie(bob, 5, 100)

    turtle.mainloop()


