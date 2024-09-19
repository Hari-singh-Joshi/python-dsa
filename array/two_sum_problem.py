import numpy as np
arr=np.array([2,4,6,7])
sum=10
for i in range(0,len(arr)-1):
    if arr[i]+arr[i+1]==sum:
        print(i,i+1)
