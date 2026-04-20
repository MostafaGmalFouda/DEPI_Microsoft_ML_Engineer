import numpy as np

def sigmoid(x):
    """
    Sigmoid activation function.
    Parameters:
    x (Net value): The input to the activation function.
    Returns:
    The output of the sigmoid function, which is a value between 0 and 1.
    """
    return 1 / (1 + np.exp(-x))

def train():
    """
    Train a simple feedforward neural network using backpropagation.
    The network has 2 input neurons, 2 hidden neurons, and 2 output neurons.
    Returns:
    The final output of the network, the final weights, the final biases, and the final mean squared error.
    """
    x = np.array([0.05, 0.10])
    y = np.array([0.01, 0.99])

    w = np.array([
        [0.15, 0.20],
        [0.25, 0.30],
        [0.40, 0.45],
        [0.50, 0.55]
    ])

    b1 = 0.35
    b2 = 0.60
    lr = 0.5

    for _ in range(10000):

        # Forward pass
        h = sigmoid(np.dot(x, w[:2]) + b1)
        o = sigmoid(np.dot(h, w[2:]) + b2)

        # Calculate error
        error = y - o

        # Calculate Mean Squared Error
        mse = np.mean(0.5 * (error ** 2))

        # backpropagation
        d_o = error * o * (1 - o)
        d_h = h * (1 - h) * np.dot(d_o, w[2:].T)

        # Update weights
        w[2:] += lr * np.outer(h, d_o)
        w[:2] += lr * np.outer(x, d_h)

        # Update biases
        b2 += lr * np.sum(d_o)
        b1 += lr * np.sum(d_h)

    return o, w, b1, b2, mse


output, weights, b1, b2, mse = train()

print("Final Output:", output)
print("\nFinal Weights:\n", weights)
print("\nFinal Bias b1:", b1)
print("Final Bias b2:", b2)
print("\nFinal MSE:", mse)