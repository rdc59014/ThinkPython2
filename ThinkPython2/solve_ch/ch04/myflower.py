import turtle
import math
from mypolygon import arc


def one_petal(t, r, angle):
    '''
    Input
    t: turtle
    r: radius
    angle:entre segmentos
    '''
    for i in range(2):
        arc(t, r, angle)
        t.lt(180 - angle)


def flower(t, r, m, angle):
    '''
    Input
    t: objeto turtle
    r: radio del petalo
    m: numero de petalos
    '''
    for i in range(m):
        one_petal(t, r, angle)
        t.lt(360.0 / m)


if __name__ == '__main__':
    tess = turtle.Turtle()

    #one_petal(tess, 150, 90)
    flower(tess, 150, 10, 90)

    turtle.mainloop()
