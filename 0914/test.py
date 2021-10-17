import numpy as np

a = np.array([1, 2, 3])
print(a)
print(type(a))


a_list = [1, 2, 3]

b_list = [2, 3, 4]

a_arr = np.array(a_list)

c = 4

print(a_list)
print(c * a_arr)

a = np.array(
    [[1, 2],
     [3, 4]]
)

c = np.array(
    [[1, 2, 3, 4, 5],
     [6, 7, 8, 9, 10]]
)

img = np.array(
    [[[255, 0, 0], [0, 255, 0]],
     [[0, 0, 255], [255, 255, 0]]]
)

a = np.array(
    [[1, 2, 3],
     [4, 5, 6]]
)

d = np.arange(0, 600)
d = d.reshape(30, 20)

e = d[15:19, 5:8]


v = np.arange(10)
mask1 = np.array(
    [False, True] * 5
)
mask2 = v % 2 == 1
print(type(mask2))
w = v[mask2.astype(bool)]
print(w)

mask3 = d % 2 == 1
print(d[mask3])
print(d[d % 2 == 1])
