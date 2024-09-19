def duplicate(arr):
    n=len(arr)
    dup=[]
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]==arr[j]:
                dup.append(arr[j])
                
    return dup if dup else False
list=[1,2,3,4,3,5,6,7,8,7]
dupli=duplicate(list)
if dupli:
    print("duplicate found",dupli)
else:
    print("there is no duplicate element")
    
    
#note
#return dup if dup else fase- if dup contains any element then dup will be returned otherwise false will be returned.