import numpy as np
from scipy import sparse
from sklearn.datasets import load_iris
x = np.array([[1, 2, 3], [4, 5, 6]])
print("x = \n {}".format(x))

eye = np.eye(4)
print("4x4 Identity matrix = \n {}".format(eye))