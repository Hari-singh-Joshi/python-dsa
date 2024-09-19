arr=[1,3,5,6]
target=2
l=-1
for i in range(0,len(arr)):
    l+=1
    if(arr[i]==target):
        print(i)
    elif (target<arr[i]):
        print(l)
        break
        
        
    
        