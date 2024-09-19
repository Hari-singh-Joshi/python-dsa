# A function to display group of strings.
def display(lst):
    for i in lst:
        print(i)

print('enter string separated by comma:')
#call
lst=[x for x in input().split()]
x,y=calculate(lst)
display(lst)
