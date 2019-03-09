import turtle
import math


'''
1. Escribe una función llamada cuadrado que tome un parámetro llamado t, que es una tortuga. Debe usar la tortuga para dibujar un cuadrado. Escriba una llamada
a la función que pase un objeto tortuga como un argumento al cuadrado, y luego ejecute el programa nuevamente.
'''

def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)

'''
2. Agregue otro parámetro, llamado longitud, al cuadrado. Modifique el cuerpo
para que la longitud de los lados sea la longitud y luego modifique la llamada
a la función para proporcionar un segundo argumento. Ejecutar el programa de nuevo. Pruebe su programa con un rango de valores de longitud.
'''

def square2(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

rango = [100, 150, 200]
colores = ["blue", "red", "green"]

#for (i, j) in zip(colores, rango):
#    alex.color(i)
#   square2(alex, j)

'''
3. Haga una copia del cuadrado y cambie el nombre a polígono. Agregue otro parámetro llamado n y modifique el cuerpo para que dibuje un polígono regular
de n lados. Sugerencia: los ángulos exteriores de un polígono regular de n
lados son 360/n grados.
'''

def polygon(t, length, n):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

'''
4. Escriba una función llamada círculo que tome una tortuga t, y radio r, como parámetros y que dibuje un círculo aproximado llamando al polígono con la
longitud y el número de lados apropiados. Prueba tu función con un rango de valores de r. Sugerencia: calcule la circunferencia del círculo y asegúrese de
que la longitud * n = circunferencia.
'''
import math

def circulo(t, r):
    circunference = 2 * math.pi * r
    n = int(circunference / 3 ) + 3
    length = circunference / n
    polygon(t, length, n)


rango = [50, 100, 150]
colores = ["blue", "red", "green", "cyan", "gold"]

#for (i, j) in zip(colores, rango):
#    alex.color(i)
#    circulo(alex, j)

#circulo(alex, 10)


def arc(t, r, angle):
    arc_length = (2 * math.pi * r * angle) / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n

    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)


#for i in range(18):
#    arc(alex,150, 90)
#    alex.up()
#    alex.left(130)
#    alex.pd()

#tess.lt(180)

if __name__ == '__main__':
    bob = turtle.Turtle()

    polygon(bob, 50, 3)
    bob.lt(60)
    polygon(bob, 50, 3)
    turtle.mainloop()











