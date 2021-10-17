import numpy as np

'''
- review perceptron
- activation function
    - sigmoid
    - step
    - ReLU
    - Leaky ReLU


'''

def step_function(x_arr):
    return (x_arr > 0).astype(int)

def sigmoid(x_arr):
    y_arr = 1 / (1 + np.exp(-x_arr))
    return y_arr

def relu(x_arr):
    return np.maximum(0, x_arr)

activation_funcion = relu

print(activation_funcion(np.array([2, 1, 0, -1])))
