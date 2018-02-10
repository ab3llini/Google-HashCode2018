import lprogramming.model.lproblem as lp
import numpy as np


def __apply_method(obj, m):
    if type(obj) is not np.ndarray:
        return np.array(obj) if m is None else m(np.array(obj))
    else:
        return obj if m is None else m(obj)


# Try not to abuse this method. Could be very slow due to transfers between CPU ad GPU
def to_array(obj):
    return obj.asarray() if type(obj) is not np.ndarray else obj


def build(method=None, **elements):
    if len(elements.keys()) == 1:
        k, v = elements.popitem()
        return __apply_method(v, method)
    else:
        o = {}
        for key, value in elements.items():
            o[key] = __apply_method(value, method)
        return o
