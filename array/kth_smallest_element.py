import numpy as np
def kth_smallest(arr,key):
    arr.sort()
    return arr[key-1]

arr=np.array([7,6,2,9,4,11])
key=3

print(kth_smallest(arr,key))