###
# A permutation generation algorithm.
# this algorithm will generate sequence by mapping index to
# variable system number, then mapping it to sequence.
#
# There are two types of variable system number, ascending and
# descending.
###
import math

from common import integer_to_ascending_system_number
from common import integer_to_descending_system_number

def PGA_with_ascending_system_number(width):
    '''
    permutation generation algorithm by mapping index to ascending
    system number and then mapping it to sequence.
    '''

    total_numbers = math.factorial(width)
    for i in range(total_numbers):
        asc_number = integer_to_ascending_system_number(i)
        asc_number += (width - len(asc_number)) * [0]  # align
        ret = [None, ] * width
        for index, n in enumerate(reversed(asc_number)):
            for pos in reversed(range(width)):
                if ret[pos] is None:
                    n -= 1
                if n < 0:
                    ret[pos] = width - index - 1
                    break
        yield ret

def PGA_with_descending_system_number(width):
    '''
    permutation generation algorithm by mapping index to descending
    system number and then mapping it to sequence.
    '''

    total_numbers = math.factorial(width)
    for i in range(total_numbers):
        desc_number = integer_to_descending_system_number(i, width)
        desc_number += (width - len(desc_number)) * [0]  # align
        ret = [None, ] * width
        for index, n in enumerate(desc_number):
            for pos in reversed(range(width)):
                if ret[pos] is None:
                    n -= 1
                if n < 0:
                    ret[pos] = width - index - 1
                    break
        yield ret


if __name__ == '__main__':
    # Verify
    for permutation in [PGA_with_ascending_system_number(4), PGA_with_descending_system_number(4)]:
        presence = set()
        for seq in permutation:
            seq = tuple(seq)
            if seq in presence:
                print('Bad permutation!')
                break
            presence.add(seq)
        else:
            print('Verified')

    # For profiler
    #list(PGA_with_ascending_system_number(4))
    #list(PGA_with_descending_system_number(4))
