import numpy as np
import lprogramming.model.lproblem as lp


def __apply_method(obj, m):
    return np.array(obj) if m is None else m(np.array(obj))


# Returns a dictionary. Each key is one of the elements
def build(raw_c, raw_A, raw_b, cudamat=None):
    out = {
        lp.kCostRef: __apply_method(raw_c, cudamat),
        lp.kConstraintsRef: __apply_method(raw_A, cudamat),
        lp.kConstantRef: __apply_method(raw_b, cudamat)
    }

    return out
