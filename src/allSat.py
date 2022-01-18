# Function for enumerative model counting.
# Courtesy of Lucas Bang.

from z3 import *
import time

result = {}
count = 0

def get_models(F, timeout):
    """
    Do model counting by enumerating each model.
    Uses Z3Py.

    Args:
        F (<class 'z3.z3.AstVector'>): SMT-LIB formula
        timeout (int): timeout (sec)

    Raises:
        Z3Exception: uninterpreted functions are not supported
        Z3Exception: arrays and uninterpreted sorts are not supported

    Returns:
        dict: counts per minute
        int: count at timeout
    """

    result = {}
    count = 0

    s = Solver()
    s.add(F)

    start = time.time()
    t = time.time()
    minute = 1

    while s.check() == sat and t - start < timeout:
        prev_count = count
        m = s.model()
        count += 1
        # Create a new constraint the blocks the current model
        block = []
        for d in m:
            # d is a declaration
            if d.arity() > 0:
                raise Z3Exception("uninterpreted functions are not supported") 
            # create a constant from declaration
            c = d()
            if is_array(c) or c.sort().kind() == Z3_UNINTERPRETED_SORT:
                raise Z3Exception("arrays and uninterpreted sorts are not supported")
            block.append(c != m[d])
        s.push()
        s.add(Or(block))
        t = time.time()
        if t - start > minute * 60:
            result[minute] = prev_count
            minute += 1
    
    return result, count