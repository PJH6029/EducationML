from matplotlib import pyplot as plt
import numpy as np

xrange = np.arange(-5, 5, 0.05)


def f(x_arr):
    # y_arr = np.abs(x_arr)
    y_arr = x_arr * (x_arr - 1)
    return y_arr

yrange = f(xrange)
# yrange = xrange * (xrange - 1)

plt.plot(xrange, yrange)

plt.show()


