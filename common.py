###
# Common functions to be used by other script
###
import math

def integer_to_ascending_system_number(integer):
    '''
    covert number integer to this kind of number,
    whose system is ascending.
    '''
    assert type(integer) is int

    def _itasn(integer):
        system = 1
        while integer:
            yield integer % system
            integer //= system
            system += 1
    return list(_itasn(integer))

def integer_to_descending_system_number(integer, width):
    '''
    covert number integer to this kind of number,
    whose system is ascending.
    '''
    assert type(integer) is int
    assert type(width) is int
    assert integer < math.factorial(width)

    def _itasn(integer):
        system = width
        while integer:
            yield integer % system
            integer //= system
            system -= 1
    return list(_itasn(integer))

if __name__ == '__main__':
    for i in range(24):
        print(integer_to_descending_system_number(i, 4))
