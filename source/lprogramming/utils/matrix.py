import numpy as np


def build(**elements):
    if len(elements.keys()) == 1:
        k, v = elements.popitem()
        return np.array(v)
    else:
        o = {}
        for key, value in elements.items():
            o[key] = np.array(value)
        return o
