import lprogramming.model.lproblem as lp
import numpy as np

def __apply_method(obj, m):
    return np.array(obj) if m is None else m(np.array(obj))


# Returns a dictionary. Each key is one of the elements
def build(raw_c, raw_A, raw_b, raw_start, method=None):
    out = {
        lp.kCostRef: __apply_method(raw_c, method),
        lp.kConstraintsRef: __apply_method(raw_A, method),
        lp.kConstantRef: __apply_method(raw_b, method),
        lp.kStartRef: __apply_method(raw_start, method)
    }

    return out
