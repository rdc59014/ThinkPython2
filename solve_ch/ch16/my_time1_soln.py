"""
Soluciones a los ejercicios del capitulo 16
de Allen Downey, Think Python 2 ed
"""

from my_time1 import Time, print_time, time_to_int, int_to_time


def is_after(t1, t2):
    """
    Toma dos objetos Time, t1 y t2
    determina si t1 es posterior a t2.
    """
    result = ((t1.hora >= t2.hora) and 
              (t1.minutos >= t2.minutos) and
              (t1.segundos > t2.segundos))

    return result


def mul_time(t1, num):
    segundo = time_to_int(t1)
    segundo *= num
    return int_to_time(segundo)


def averange_pace(t1, milla):
    return mul_time(t1, 1.0/milla)


def main():
    time = Time()
    time.hora = 0
    time.minuto = 0
    time.segundo = 10

    t1 = averange_pace(time, 10)
    print_time(t1)


if __name__ == "__main__":
    main()
