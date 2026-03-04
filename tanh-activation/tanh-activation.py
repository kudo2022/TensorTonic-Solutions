import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    # Write code here
    x = np.array(x)
    return (1-np.exp(-2*x))/( 1 + np.exp(-2*x))
    