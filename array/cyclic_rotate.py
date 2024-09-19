import numpy as np
arr=np.array([4,3,7,8,9,12])
x=1
temp=arr[len(arr)-1]




for i in range(len(arr)-1,-1,-1):
    arr[i]=arr[i-1]
    
        
arr[0]=temp
print(arr)
        
    
#note
# len(arr)-1 is the last index of array

    