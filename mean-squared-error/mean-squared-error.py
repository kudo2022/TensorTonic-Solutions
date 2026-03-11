import numpy as np
def mean_squared_error(y_pred , y_true):
  y_pred = np.array(y_pred)
  y_true = np.array(y_true)

  result = y_pred - y_true
  res =result**2

  error = np.mean(res)

  return error
