import numpy as np

# Define the dataset
X = np.array([1400, 1600, 1700, 1875, 1100, 1550, 2350, 2450, 1425, 1700])
y = np.array([245000, 312000, 279000, 308000, 199000,
             219000, 405000, 324000, 319000, 255000])

# Initialize the parameters
b0 = 0
b1 = 0
alpha = 0.0000009
m = len(X)

# Define the cost function


def cost_function(X, y, b0, b1):
    y_pred = b0 + b1 * X
    cost = (1/2*m) * (np.sum(np.square(y_pred - y)) + 300000000*b1*b1)
    return cost


# Perform gradient descent
for i in range(100):
    y_pred = b0 + b1 * X
    b0 = b0 - alpha * (1/m) * np.sum(y_pred - y)
    b1 = b1 - alpha * (1/m) * (np.sum((y_pred - y) * X) + 300000000*b1)
    cost = cost_function(X, y, b0, b1)
    print("Iteration {}: b0 = {}, b1 = {}, cost = {}".format(i, b0, b1, cost))
