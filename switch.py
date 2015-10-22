###
# A permutation generation algorithm.
# this algorithm is implemented by switching neighboring number.
#
# Under here is two implementation recursive and iterative
###


def recursive_PGA_with_switch(width):
    '''
    Recursive permutation generation algorithm with switch
    '''
    # condition
    assert width > 0
    assert type(width) is int

    # boundary
    if width == 1:
        yield '1'
        return

    # recursion
    left = True  # direction to move
    for sub_permutation in recursive_PGA_with_switch(width-1):
        # positions to insert new number
        positions = reversed(range(width)) if left else range(width)
        left = not left

        for i in positions:
            perm = [sub_permutation[:i], str(width), sub_permutation[i:]]
            #print(perm)
            yield(''.join(perm))


if __name__ == '__main__':
    for permutation in recursive_PGA_with_switch(3):
        print(permutation)
