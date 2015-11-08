###
# A permutation generation algorithm.
# this algorithm will generate sequence according as 
# dict order.
#
# Under here is two implementation recursive and iterative
###


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


def recursive_PGA_with_dict(width):
    '''
    Recursive permutation generation algorithm according
    to dict order.
    '''
    # condition
    assert width >= 0
    assert type(width) is int

    return _recursive_PGA_with_dict(list(range(width)))


if __name__ == '__main__':
    # For profiler
    # python -m cProfile switch.py
    for r_result in recursive_PGA_with_dict(9):
        print(r_result)
