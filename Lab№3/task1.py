import numpy as np            
import random

arr = np.zeros(5, dtype=int)
for i in range(len(arr)):
    arr[i] = random.randint(1, 50)

num = int(input("Enter a number"))
closest = float('inf')
close = 0

for i in range(len(arr)):
    diff = abs(pow(arr[i], 2) - pow(num, 2))
    if diff < closest:
        closest = diff
        close= arr[i]

print(close)

print(arr)
