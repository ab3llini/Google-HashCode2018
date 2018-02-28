from tqdm import tqdm

# pythran export pi_approximate(int)
def pi_approximate(n):
    step = 1.0 / n
    result = 0
    # omp parallel for reduction(+:result)
    for i in range(n):
        x = (i + 0.5) * step
        result += 4.0 / (1.0 + x * x)
    return step * result


# pythran export foo2(int)
def foo2(n):
    i = 0
    while i < n:
        a = i**2
        i += 1

