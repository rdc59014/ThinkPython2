

"""This module contains a code example related to

    Think Python, 2nd Edition
    by Allen Downey
    http://thinkpython2.com

    Copyright 2015 Allen Downey

    License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division


class Point:
    """Representa un punto en el espacio 2-D."""


class Rectangle:
    """
    Representa un rectangulo en 2-D.
    """


def find_rect_corners(rect):
    """
    Retorna las cuatro esquinas de un rectangulo,
    como una 4-tupla.
    """
    corner1 = Point()
    corner2 = Point()
    corner3 = Point()
    corner4 = Point()
    
    corner1.x = rect.corner.x
    corner1.y = rect.corner.y

    corner2.x = rect.corner.x + rect.width
    corner2.y = rect.corner.y

    corner3.x = rect.corner.x
    corner3.y = rect.corner.y + rect.height

    corner4.x = rect.corner.x + rect.width
    corner4.y = rect.corner.y + rect.height
    return (corner1, corner2, corner3, corner4)


def print_circle(circle):
    print("Centro del circulo: ({0}, {1})\nRadio: {2}"
          .format(circle.center.x, circle.center.y, circle.radius))


def print_rectangle(rect):
    print("Corner: ({0}, {1})\nWidth: {2}, Height: {3}"
          .format(rect.corner.x, rect.corner.y,
                  rect.width, rect.height))

