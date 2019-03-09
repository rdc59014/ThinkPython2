"""

Soluciones al ejercicio 2 del capitulo 16
Allen Downey, Think Python 2ed
"""

import datetime 


def main():
    day = datetime.datetime.now()
    print("Today is: {0}".format(day.strftime("%A")))
#    print("Enter the year of birth:")
#    age = int(input())
#    print("Enter the month of birth:")
#    month = int(input())
#    print("Enter the day of birth:")
#    day = int(input())


    birthday = datetime.datetime(1969, 2, 22)
    print("Birthday's Danilo: {0}".format(birthday))
    now = datetime.datetime.today()
    print("Today is: {0}".format(now))
    
    # Esto se puede hacer mas facil, usando el atributo year.
    diff = now.year - birthday.year
    print("Age of usser: %.2d" % diff)

#    diff = now - birthday
#    one_year = 365 * 24 * 3600
#    print("Age of usser: %.2d" % (diff.total_seconds() // one_year)) #diff // 365))

    # Tener cuidado con el caso de que el cumpleaños ya aya pasado,
    # por que daria fecha negativa.
    nex_birthday = birthday.replace(year=now.year)
    if nex_birthday < now:
        nex_birthday = nex_birthday.replace(year=now.year + 1)
    
    print("The next birthday's Danilo: {0}".format(nex_birthday))

    


if __name__ == "__main__":
    main()

    
