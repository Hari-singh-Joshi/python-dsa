arr1=[2,3,4,5,]
arr2=[6,7,8,9,]
arr3=[]
for ele1,ele2 in zip(arr1,arr2):
   arr3.append(ele1)
   arr3.append(ele2)
print(type(arr3))