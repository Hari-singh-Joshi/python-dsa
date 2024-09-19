#best time complexity is o(n)
#worst time complexity is o(n^2)

def bubble(arr):
    n=len(arr)
    count=0
    for i in range(n):
        swapped=False
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
                count=count+1
            if not swapped:
                break
        if count==0:
            break
arr=[60,40,30,10,50]
bubble(arr)
print("sorted array is:",arr)

















