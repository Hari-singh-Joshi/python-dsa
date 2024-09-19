list = [6,7,8,9,-8,-9]
sum = -100000
x = 0

for i in range(0, len(list)):
    x += list[i]
    if x>sum:
        sum=x
    elif x<0:
         x=0
   

print(sum)


# -2,1,-3,4,-1,2,1,-5