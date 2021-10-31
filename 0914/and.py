import numpy as np

def AND(x1, x2):
    w1, w2, theta = 1, 1, 1.5
    y = x1 * w1 + x2 * w2
    if y <= theta:
        return 0
    else:
        return 1

def AND2(x1, x2):
    W = np.array([1, 1])
    X = np.array([x1, x2])
    b = -1.5
    y = sum(X * W) + b
    y = np.dot(X, W) + b
    if y <= 0:
        return 0
    else:
        return 1

def NAND(x1, x2):
    W = np.array([-1, -1])
    X = np.array([x1, x2])
    b = 1.5
    y = sum(X * W) + b
    if y <= 0:
        return 0
    else:
        return 1


def OR(x1, x2):
    W = np.array([1, 1])
    X = np.array([x1, x2])
    b = -0.5
    y = sum(X * W) + b
    if y <= 0:
        return 0
    else:
        return 1


def NOR(x1, x2):
    W = np.array([-1, -1])
    X = np.array([x1, x2])
    b = 0.5
    y = sum(X * W) + b
    if y <= 0:
        return 0
    else:
        return 1

def NOT(x):
    return NAND(x, x)

def pt(x1, x2):
    and1 = AND(x1, x2)
    and2 = AND(x1, x2)
    y = OR(and1, and2)
    return y


def XOR(x1, x2):
    not_x1 = NOT(x1)
    not_x2 = NOT(x2)
    and1 = AND(x1, not_x2)
    and2 = AND(not_x1, x2)
    y = OR(and1, and2)
    return y

def print_gate(f):
    for i in range(2):
        for j in range(2):
            print(f(i, j), end=" ")
    print()



print_gate(AND)
print_gate(NAND)
print_gate(OR)
print_gate(NOR)
print_gate(XOR)