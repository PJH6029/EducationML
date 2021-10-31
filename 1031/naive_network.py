import numpy as np

def sigmoid(x_arr):
    y_arr = 1 / (1 + np.exp(-x_arr))
    return y_arr


def init_network():
    network = {}
    network['W1'] = np.array([[0.1, 0.3, 0.4],
                              [0.2, 0.4, 0.6]])
    network['b1'] = np.array([0.1, 0.2, 0.3])
    network['W2'] = np.array([[0.1, 0.4],
                              [0.2, 0.5],
                              [0.3, 0.6]])
    network['b2'] = np.array([0.1, 0.2])
    network['W3'] = np.array([[0.1, 0.3],
                              [0.2, 0.4]])
    network['b3'] = np.array([0.1, 0.2])

    return network


def forward(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    z1 = sigmoid(np.matmul(x, W1) + b1)
    z2 = sigmoid(np.matmul(z1, W2) + b2)
    z3 = (np.matmul(z2, W3) + b3)

    return z3


network = init_network()
output = forward(network, np.array([1.0, 0.5]))
print(output)