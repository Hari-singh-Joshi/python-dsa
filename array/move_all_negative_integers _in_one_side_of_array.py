list=[2,3,4,5,-1,-4,-6,10]
list1=[]
list2=[]
for i in list:
    if i>0:
        list1.append(i)
    elif i<0:
        list2.append(i)
print(list2+list1)