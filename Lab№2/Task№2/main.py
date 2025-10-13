import numpy as np       

arr = np.random.randint(0,10,(10,10))

lowest = np.min(arr, axis=1)
highest = np.max(arr, axis=1)

plus = np.sum(lowest)
mult = np.prod(highest)

print("PLUS = ",plus)
print("MULT = ",mult)

print(arr)
