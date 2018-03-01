# pythran export bench(float, float)

import numpy as np

def bench(a, b):
    c = 0
    t = 1
    while c != 1000:
        t = (a * b) ** (a / b) * np.sin(a)

