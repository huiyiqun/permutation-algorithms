###
# Common functions to be used by other script
###

def integer_to_ascending_system_number(integer):
    '''
    covert number integer to this kind of number,
    whose system is ascending.
    '''
    assert type(integer) is int

    def _itasn(integer):
        system = 2
        while integer:
            yield integer % system
            integer //= system
            system += 1
    return list(_itasn(integer))

if __name__ == '__main__':
    for i in [1, 3, 10, 100]:
        print(integer_to_ascending_system_number(i))
