def linear_layer_forward(X, W, b):
    """
    Compute the forward pass of a linear (fully connected) layer.
    """
    # Write code here
    
    result = np.matmul(X, W) +b
    return result.tolist()