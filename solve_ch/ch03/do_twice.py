def print_spam():
    print('spam')


def do_twice(function):
    function()
    function()


do_twice(print_spam)