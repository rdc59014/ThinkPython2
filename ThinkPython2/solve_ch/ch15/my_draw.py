

import math
import turtle
import tkinter
from my_circle import Circle
from my_point1 import Rectangle, Point


def draw_rect(turt, rect):
    width = rect.width
    height = rect.height
    turt.pu()
    turt.setx(rect.corner.x)
    turt.sety(rect.corner.y)
    turt.pd()
    for i in range(4):
        if i % 2 == 0:
            turt.fd(width)
            turt.lt(90)
        else:
            turt.fd(height)
            turt.lt(90)


def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)


def circle(t, r):
    t.pu()
    t.setx(r)
    t.lt(90)
    t.sety(0)
    t.pd()
    arc(t, r, 360)


def draw_circle(turt, circ):
    circle(turt, circ.radius)



def main():
    turtle.setup(800, 600)   # establecer el tamaño de la ventana
                             # de 800 por 600 píxeles
    wn = turtle.Screen()     # establecer wn al objeto de la ventana
    wn.bgcolor("lightgreen")  # establecer el color de fondo de la ventana
    wn.title("Hola, turt!")  # establecer el título de la ventana
    turt = turtle.Turtle()
    turt.color("blue")  # hacer turt azul
    turt.pensize(3)  # establecer el ancho de la pluma
#    turt = turtle.Turtle()

    box = Rectangle()
    box.corner = Point()
    box.corner.x = -30.0
    box.corner.y = -40.0
    box.width = 60.0
    box.height = 80.0
    
    circ = Circle()
    circ.radius = 50.0
    circ.center = Point()
    circ.center.x = 0.0
    circ.center.y = 0.0

    draw_rect(turt, box)
    draw_circle(turt, circ)
    print(turt)
    wn.exitonclick()
#    turt.mainloop()


if __name__ == "__main__":
    main()




