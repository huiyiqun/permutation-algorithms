###
# A permutation generation algorithm.
# this algorithm will generate sequence according as 
# dict order.
#
# Under here is two implementation recursive and iterative
###
import math
from common import integer_to_ascending_system_number


def recursive_PGA_with_dict(width):
    '''
    Recursive permutation generation algorithm according
    to dict order.
    '''

    def _recursive_PGA_with_dict(sequence):
        '''
        Note:
            `sequence` must be dict-ordered.
        '''
        # boundary
        if not len(sequence):
            # Empty
            yield sequence
            return

        # recursion
        for i, first_index in enumerate(sequence):
            seq_copy = sequence.copy()
            del seq_copy[i]
            for sub_permutation in _recursive_PGA_with_dict(seq_copy):
                yield [first_index, ] + sub_permutation


    # condition
    assert width >= 0
    assert type(width) is int

    return _recursive_PGA_with_dict(list(range(width)))


def iterative_PGA_with_dict(width):
    '''
    Iterative permutation generation algorithm according
    to dict order.
    '''

    total_numbers = math.factorial(width)
    for i in range(total_numbers):
        asc_number = integer_to_ascending_system_number(i)
        asc_number += (width - len(asc_number)) * [0]  # align
        ret = []
        ordered_index = list(range(width))
        for n in reversed(asc_number):
            ret.append(ordered_index[n])
            del ordered_index[n]
        yield list(ret)


if __name__ == '__main__':
    # Verify results
    #for i_result, r_result in zip(iterative_PGA_with_dict(9), recursive_PGA_with_dict(9)):
    #    if i_result != r_result:
    #        # print(i_result, r_result)
    #        print('Failed!')

    # For profiler
    # python -m cProfile dict.py
    #for r_result in recursive_PGA_with_dict(9):
    #   print(r_result)

    # For profiler
    # python -m cProfile dict.py
    #for i_result in iterative_PGA_with_dict(9):
    #    print(i_result)
    pass
