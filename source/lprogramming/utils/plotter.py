import matplotlib.pyplot as plt
import numpy as np


def plot(problem, history=None):

    plt.clf()

    x = np.linspace(0, 16, 2000)

    if problem.a.shape[1] == 2:
        for i in range(0, problem.a.shape[0]):
            b = problem.b[i][0]
            v = problem.a[i][0] * x
            d = problem.a[i][1]

            if d > 0:
                plt.plot(x, (b - v) / d)
            else:
                plt.axvline(x=(b/problem.a[i][0]))
    else:
        print("Unable to print problem")

    plt.title("Problem")
    plt.xlim((0, 16))
    plt.ylim((0, 16))
    plt.xlabel(r'$%s_1$' % problem.var_names)
    plt.ylabel(r'$%s_2$' % problem.var_names)

    if history is not None:
        for i in range(0, len(history) - 1):

            dx = history[i + 1][0][0] - history[i][0][0]
            dy = history[i + 1][1][0] - history[i][1][0]

            plt.arrow(
                history[i][0][0],
                history[i][1][0],
                dx,
                dy,
                head_width=0.5, head_length=0.5, fc='k', color='r', zorder=problem.a.shape[0] + i)

    plt.show()
