###
# A permutation generation algorithm.
# this algorithm will generate sequence according as 
# dict order.
#
# Under here is two implementation recursive and iterative
###
import math
import pyopencl as cl
import numpy as np

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


def opencl_PGA_with_dict(width):
    total_numbers = math.factorial(width)

    ctx = cl.create_some_context()
    queue = cl.CommandQueue(ctx)

    program = cl.Program(ctx, """
        __kernel void PGA_with_dict(__global short* result) {{
            int input = get_global_id(0);
            int i, j;

            short asc_number[{width}];

            for (i = 0; i < {width}; i++) {{
                asc_number[i] = input % (i+1);
                input /= (i+1);
            }}

            int global_addr = get_global_id(0) * {width};
            int unpicked[{width}];
            short passby;
            for (i = 0; i < {width}; i++)
                unpicked[i] = 1;

            for (i = {width}-1; i >= 0; i--) {{
                passby = 0;
                for (j = 0; j < {width}; j++) {{
                    passby += unpicked[j];
                    if (passby > asc_number[i]) {{
                        unpicked[j] = 0;
                        result[global_addr+{width}-1-i] = j;
                        break;
                    }}
                }}
            }}
        }}
    """.format(width=width)).build()

    result = np.zeros((total_numbers, width), np.short)
    result_buf = cl.Buffer(ctx, cl.mem_flags.WRITE_ONLY, result.nbytes)

    program.PGA_with_dict(queue, (total_numbers,), None, result_buf)

    cl.enqueue_copy(queue, result, result_buf)
    for res in result:
        yield list(res)


if __name__ == '__main__':
    # Verify results
    #for i_result, r_result, cl_result in zip(iterative_PGA_with_dict(8),
    #                                         recursive_PGA_with_dict(8),
    #                                         opencl_PGA_with_dict(8)):
    #    if i_result != r_result or \
    #            r_result != list(cl_result):
    #        print(i_result, r_result, cl_result)
    #        print('Failed!')

    # For profiler
    # python -m cProfile dict.py
    #for r_result in recursive_PGA_with_dict(10):
    #   pass

    # For profiler
    # python -m cProfile dict.py
    #for i_result in iterative_PGA_with_dict(9):
    #    pass

    # For profiler
    # python -m cProfile dict.py
    for cl_result in opencl_PGA_with_dict(11):
        pass
    pass
