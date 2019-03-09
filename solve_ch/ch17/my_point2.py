"""
Ejercicios del capitulo 17 de Allen Downey
"""

class Time:

    def __init__(self, hour=0, minute=0,second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return ('%.2d:%.2d:%.2d'%(self.hour, self.minute, self.second))
    
    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def __radd__(self, other):
        return self.__add__(other)

    def add_time(self, other):
        second = self.time_to_int() + other.time_to_int()
        return int_to_time(second)

    def print_time(self):
        print('%.2d:%.2d:%.2d'%(self.hour, self.minute, self.second))

    def time_to_int(self):
        minute = self.hour * 60 + self.minute
        second = minute * 60 + self.second
        return second

    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)

    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()


def int_to_time(second):
    time = Time()
    minute, time.second = divmod(second, 60)
    time.hour, time.minute = divmod(minute, 60)
    return time


class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return ("({0}, {1})".format(self.x, self.y))
       
    def __add__(self, other):
        if isinstance(other, Point):
            return self.add_point(other)
        else:
            return self.add_tuple(other)

    def __radd__(self, other):
        return self.__add__(other)

    def add_point(self, other):
        point = Point()
        point.x = self.x + other.x
        point.y = self.y + other.y
        return point

    def add_tuple(self, other):
        point = Point()
        xtuple, ytuple = other
        point.x = self.x + xtuple
        point.y = self.y + ytuple
        return point

    def print_ponit(self):
        print("({0}, {1})".format(self.x, self.y))


def main():
    start = Time()
    start.hour = 9
    start.minute = 45
    start.second = 0

    Time.print_time(start)
    start.print_time()
    print(start.time_to_int())
    t1 = start.increment(120)
    t1.print_time()
    print(t1.is_after(start))

    t2 = Time()
    t2.print_time()
    print(t2)

    t3 = Time(2, 32, 45)
    t3.print_time()
    print(t3)

    p1 = Point(-2, 1)
    p2 = Point(1, 2)

    p1.print_ponit()
    p2.print_ponit()
    print(p1)
    print(p2)

    duration = Time(1, 35)
    result_time = start + duration
    print(result_time)
    print(result_time + 3600)
    print(7200 + result_time)

    p = p1 + p2
    print(p + (3,3))
    print((-4, -5) + p)
    p4 = sum([p1, p2])
    print(p4)
    t4 = sum([t1, t2])
    print(t4)


if __name__ == "__main__":
    main()
