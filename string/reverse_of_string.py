import numpy as np

arr = np.array([1, 2, 3, 4, 5,6,7,8,9])
x = len(arr) - 1

for i in range(0, len(arr)//2):
    arr[i], arr[x] = arr[x], arr[i]
    x -= 1

print(arr)
