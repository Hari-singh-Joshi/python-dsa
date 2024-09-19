list1=[2,3,4,5,6,7]
list2=[4,5,8,9,10]
intersection=[]
union=[]
for i in list1:
    for j in list2:
        if i==j:
            intersection.append(i)
for i in list1:
    if i not in union:
        union.append(i)
for i in list2:
    if i not in union:
        union.append(i)

print(union)    
print(intersection)
            