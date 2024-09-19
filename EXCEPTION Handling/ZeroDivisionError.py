# a program to handle the Zero Division Error Exception
try:
    f=open('myfile','w')
    a,b=[int(x) for x in input("enter two numbers: ").split()]
    c=a/b
    f.write(f'writing {c} into myfile')
except ZeroDivisionError:
    print('Division by Zero happened')
    
