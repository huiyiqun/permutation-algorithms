###
# A permutation generation algorithm.
# this algorithm is implemented by switching neighboring number.
#
# Under here is two implementation recursive and iterative
###


def recursive_PGA_with_switch(width):
    '''
    Recursive permutation generation algorithm through switching
    neighboring elements.
    '''
    # condition
    assert width >= 0
    assert type(width) is int

    # boundary
    if width == 0:
        yield list()
        return

    # recursion
    left = True  # direction to move
    for sub_permutation in recursive_PGA_with_switch(width-1):
        # positions to insert new number
        positions = reversed(range(width)) if left else range(width)
        left = not left

        for i in positions:
            yield sub_permutation[:i] + [width-1, ] + sub_permutation[i:]

def iterative_PGA_with_switch(width):
    '''
    Iterative permutation generation algorithm through switching
    neighboring elements.
    '''
    # initial state
    indexes = list(range(width))
    left = [True] * width

    def neighbor(i):
        '''
        Get index neighbor of `i` according to `left`
        '''
        return (i - 1) if left[i] else (i + 1)

    def search_largest_movable_index():
        '''
        Search for largest movable index.

        Return:
            position of largest movable index.
        '''
        max_index = max_i = -1
        for i in range(width):
            if 0 <= neighbor(i) < width and \
                    indexes[i] > indexes[neighbor(i)] and \
                    indexes[i] > max_index:
                max_i, max_index = i, indexes[i]
        return max_i

    def reverse_larger_than(index):
        '''
        Reverse directory of all index which is larger than `index`
        '''
        for i in range(width):
            if indexes[i] > index:
                left[i] = not left[i]

    while True:
        yield indexes
        max_i = search_largest_movable_index()
        if max_i == -1:
            break

        reverse_larger_than(indexes[max_i])

        # Switch largest movable index with its neighbor
        max_i_neighbor = neighbor(max_i)
        indexes[max_i], indexes[max_i_neighbor], left[max_i], left[max_i_neighbor] = \
                indexes[max_i_neighbor], indexes[max_i], left[max_i_neighbor], left[max_i]



if __name__ == '__main__':
    # Verify results
    #for i_result, r_result in zip(iterative_PGA_with_switch(9), recursive_PGA_with_switch(9)):
    #    if i_result != r_result:
    #        print('Failed!')

    # For profiler
    # python -m cProfile switch.py
    #for i_result in iterative_PGA_with_switch(9):
    #   pass

    # For profiler
    # python -m cProfile switch.py
    #for r_result in recursive_PGA_with_switch(9):
    #   pass
