import numpy as np
A = [[1, 2, 3],
     [4, 5, 6]]

B = [[7, 8],
     [9, 10],
     [11, 12]]

def matmul(A, B):
    C = [[0 for j in range(len(B[0]))] for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            # sum of aik * bkj for k in range(len(A[0)
            C[i][j] = sum([A[i][k] * B[k][j] for k in range(len(B))])
    return C

print(matmul(A, B))

class Foo:
    def __str__(self):
        return "I'm a class!"

f = Foo()
print(f)