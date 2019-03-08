"""
Ejemplos del Libro: Think Python 2ed.
de Allen Downey

Capitulo 16
"""

class Time:
    """
    Representa la hora del dia.

    atributos: horas, minuto, segundo
    """


def print_time(t):
    """
    Imprime la hora usando dos digitos, con el formato:
    t: es el objeto Time.

    hora:minuto:segundo
    """
    print("%.2d:%.2d:%.2d"%
          (t.hora, t.minuto, t.segundo))


def add_time(t1, t2):
    suma = Time()
    suma.hora = t1.hora + t2.hora
    suma.minuto = t1.minuto + t2.minuto
    suma.segundo = t1.segundo + t2.segundo

#    if suma.segundo >= 60:
#        suma.segundo -= 60
#        suma.minuto += 1
#    if suma.minuto >= 60:
#        suma.minuto -= 60
#        suma.hora += 1

    suma.minuto += suma.segundo // 60
    suma.segundo %= 60
    suma.hora += suma.minuto // 60
    suma.minuto %= 60
    return suma


def increment(t1, nseg):
    t1.segundo += nseg
    t1.minuto += t1.segundo // 60
    t1.segundo %= 60
    t1.hora += t1.minuto // 60
    t1.minuto %= 60
    return t1


def pure(t1, nseg):
    t2 = Time()
    t2.hora = 0
    t2.minuto = 0
    t2.segundo = nseg
    t2 = add_time(t1, t2)
    return t2


def time_to_int(t1):
    minuto = t1.minuto + t1.hora * 60
    segundo = minuto * 60 + t1.segundo
    return segundo


def int_to_time(seg):
    time = Time()
    minuto, time.segundo = divmod(seg, 60)
    Time.hora, time.minuto = divmod(minuto, 60)
    return time


def add_time2(t1, t2):
    segundo = time_to_int(t1) + time_to_int(t2)
    return int_to_time(segundo)


def increment1(t1, nseg):
    segundo = time_to_int(t1) + nseg
    return int_to_time(segundo)


def main():
    start = Time()
    start.hora = 9
    start.minuto = 45
    start.segundo = 0

    duracion = Time()
    duracion.hora = 1
    duracion.minuto = 35
    duracion.segundo = 0

    hecho = add_time2(start, duracion)
    print_time(hecho)

    hecho = pure(start, 98)
    print_time(hecho)
    print_time(start)
    t3 = increment1(start, 75)
    print_time(t3)


if __name__=="__main__":
    main()




