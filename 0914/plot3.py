from matplotlib import pyplot as plt
import numpy as np

xrange = np.arange(-10, 10, 0.5)

yrange1 = xrange * (xrange - 1)
yrange2 = np.abs(xrange)

yrange3 = np.sin(xrange)

yrange4 = (xrange + 5) * (xrange) * (xrange - 5)

f, axes = plt.subplots(2, 2)

axes[0][0].plot(xrange, yrange1, label="square")
axes[0][1].plot(xrange, yrange2, label="abs")
axes[1][0].plot(xrange, yrange3, label="x^3")
axes[1][1].plot(xrange, yrange4, label="x(x-1)(x-2)")

for i in range(2):
    for j in range(2):
        axes[i][j].grid()
        axes[i][j].legend()

plt.show()