import numpy as np
arr=np.array([1,2,3,4,5,6,-1,-2,-3])
current=0
max=-10000
for i in range(0,len(arr)):
    current+=arr[i]
    if current<max:
        current=0
    elif current>max:
        max=current
print(max)
