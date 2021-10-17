from matplotlib import pyplot as plt

def lst():
    a = []
    for i in range(-100, 100):
        a.append(i / 20)
    return a

# xrange = lst()

# list comprehension
xrange = [i / 20 for i in range(-100, 100)]

def f(x):
    return x * (x - 1)

def f2(x_arr):
    y_arr = [f(x) for x in x_arr]
    return y_arr

# yrange = [f(x) for x in xrange]
yrange = f2(xrange)

plt.plot(xrange, yrange)
plt.show()

