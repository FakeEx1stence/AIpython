import numpy as np

arr = np.zeros((10, 10), dtype=int)
arr[::2, ::2] = 1
arr[1::2, 1::2] = 1

print(arr)
