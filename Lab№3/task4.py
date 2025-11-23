import numpy as np

def swap_rows(arr, row1, row2):
    temp = arr[row1,:].copy()
    arr[row1,:] = arr[row2, :]
    arr[row2,:] = temp

arr = np.random.randint(0,25,(5,4))

print(arr)

swap_rows(arr,0,1)

print(arr)
