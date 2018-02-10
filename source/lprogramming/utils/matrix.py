import lprogramming.model.lproblem as lp
import numpy as np


def __apply_method(obj, m):
    return np.array(obj) if m is None else m(np.array(obj))


# Try not to abuse this method. Could be very slow due to transfers between CPU ad GPU
def to_array(obj):
    return obj.asarray() if type(obj) is not np.ndarray else obj


def build(method=None, **elements):
    o = {}
    for key, value in elements.items():
        if type(value) is not np.ndarray:
            o[key] = __apply_method(value, method)
        else:
            o[key] = value
    return o
