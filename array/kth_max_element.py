import numpy as np
def kth_largest(arr,key):
    
    return arr[key-1]

arr=np.array([7,6,2,9,4,11])
key=2

print(kth_largest(arr,key))