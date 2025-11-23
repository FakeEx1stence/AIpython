import numpy as np    

A = np.random.randint(0,25,(5,5))

k = int(input("Enter a number(1-5)")) - 1

if k > 0 and k < 5:
    A_sorted = A[A[:, k].argsort()]
    print(A_sorted)
else:
    print("k is out of range")
