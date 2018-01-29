import numpy as np
import cudamat as cm
import time

'''Please tune matrix size in order not to get an out of memory error.'''
'''The following setup runs fine on 32GB of RAM and a GTX 1080Ti'''




H1 = 5000
W1 = 8000
W2 = 9000
H2 = W1


def start():

    print("CPU Benchmark starting..")

    print("Generating matrix A %dx%d with all values = to 5.5.." % (H1, W1))

    A = np.matrix(np.full((H1, W1), 5.5))

    print("Generating matrix B %dx%d with all values = to 5.5.." % (H2, W2))

    B = np.matrix(np.full((H2, W2), 7.5))

    print("Performing A * B")

    begin = time.time()

    np.dot(A, B)

    end = time.time()

    cpu = end - begin;

    print("CPU Benchmark done >>> %.10f seconds" % (end - begin))

    print("GPU Benchmark starting..")

    print("Generating matrix A %dx%d with all values = to 5.5.." % (H1, W1))

    A = cm.CUDAMatrix(np.full((H1, H2), 5.5))

    print("Generating matrix B %dx%d with all values = to 5.5.." % (H2, W2))

    print("Performing A * B")

    B = cm.CUDAMatrix(np.full((H2, W2), 7.5))

    begin = time.time()

    cm.dot(A, B)

    end = time.time()

    gpu = end - begin

    print("GPU Benchmark done >>> %.10f seconds" % (end - begin))

    print("Benchmark done >>> GPU was %d times faster than CPU" % ((cpu / gpu) * 100))

start()