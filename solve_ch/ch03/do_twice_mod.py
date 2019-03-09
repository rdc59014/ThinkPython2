def do_twice_mod(func, value):
    '''
    Input
    func: Un objeto funcion.
    value: valor que se le pasa al objeto funcion.
    '''
    func(value)
    func(value)


def print_twice(arg):
    '''
    Input
    arg: argumento a imprimir.
    '''
    print(arg)
    print(arg)


#do_twice_mod(print_twice, 'spam')

def do_four(func, value):
    '''
    Input
    func: Un objeto funcion.
    value: valor que se le pasa al objeto funcion.
    '''
    do_twice_mod(func,value)
    do_twice_mod(func, value)


do_four(print_twice, 'spam')
