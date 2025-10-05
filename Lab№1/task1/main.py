arr = []
num = None

for i in range (8):
    arr.append(float(input(f"Enter element {i}: ")))
    
    
for i in range (len(arr)):
    print(arr[i])
    
D = (float(input("Enter D")))

for i in range (len(arr)-1):
    print(arr[i], "+", arr[i+1], "= ", (arr[i]+arr[i+1]))
    if (arr[i] + arr[i+1]) < D:
        print(i)
        exit(0)
    elif (i == len(arr)-2 and arr[i]+arr[i+1] > D):
        print(0)
    else:
        print("nothing")
