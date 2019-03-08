

import math
from copy import copy, deepcopy
from my_point1 import Point, Rectangle, print_circle, find_rect_corners


class Circle:
    """
    Represents a circle.

    attributes: radius, center.
    """


def point_in_circle(circle, point):
    """
    Determina si un punto dado,
    esta completamente dentro del circulo.
    """
    c_x = circle.center.x
    c_y = circle.center.y
    radius = circle.radius

    p_x = point.x
    p_y = point.y

    distance = math.sqrt((c_x - p_x) ** 2 + (c_y - p_y) ** 2)

    if distance <= radius:
        return True

    return False


def rect_in_circle(circle, rect):
    """
    Determina si el rectangulo proporcionado,
    se encuentra completamente dentro del circulo dado.
    """
    diagonal = math.sqrt(rect.width**2 + rect.height**2)
    if diagonal / 2 <= circle.radius:
        corners = find_rect_corners(rect)
        count = 0
        for point_i in corners:
            if point_in_circle(circle, point_i):
                count += 1
        if count == 4:
            return True
    return False


def rect_circle_overlap(circle, rect):
    corners = find_rect_corners(rect)
    for point_i in corners:
        if point_in_circle(circle, point_i):
            return True

    return False


def main():
    cir1 = Circle()
    cir1.center = Point()
    cir1.center.x = 150.0
    cir1.center.y = 100.0
    cir1.radius = 75.0

    print(cir1.center.x)
    print(cir1.center.y)
    print(cir1.radius)

    rect = Rectangle()
    rect.corner = Point()
    rect.corner.x = -50.0
    rect.corner.y = -150.0
    rect.width = 100.0
    rect.height = 200.0

    rect.corner.x += rect.height 
    print(point_in_circle(cir1, rect.corner))
    print(rect_in_circle(cir1, rect))
    print(rect_circle_overlap(cir1, rect))


if __name__ == '__main__':
    main()
