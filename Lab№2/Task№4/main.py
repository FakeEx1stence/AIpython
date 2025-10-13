import numpy as np        

arr = np.zeros((5, 5), dtype=int)
arr[np.arange(1, 5), np.arange(4)] = [1, 2, 3, 4]

print(arr)
