import numpy as np

def dropout(
    x: list,
    p: float = 0.5,
    rng: np.random.Generator = None,
) -> tuple[np.ndarray, np.ndarray]:
    """
    Returns (output, dropout_pattern) as NumPy arrays matching the shape of x.
    """
    # Write code here
    #  step 1:  convert into  numpy  array
    x = np.asarray(x)

    # step 2  generate random  number 
    if rng is not None:
        random_values = rng.random(x.shape)
    else:
        random_values = np.random.random(x.shape)

    dropout_pattern = (random_values >= p)/(1-p)

    output = x*dropout_pattern
    return output , dropout_pattern
    pass