import numpy as np
arr=np.array([4,3,7,8,9,12,23])
x=int(len(arr)/2)
for i in range(len(arr)-1,x-1,-1):
    temp=arr[i]
    arr[i]=arr[len(arr)-1-i]
    arr[len(arr)-1-i]=temp
print(arr)

