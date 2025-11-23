import numpy as np  

vector = np.array([1,2,3,4,5])
new_one = np.zeros(len(vector)*4)
j = 0

for i in range(len(vector)):
    new_one[j] = vector[i]
    j+=4

print(new_one)
