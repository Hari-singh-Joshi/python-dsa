class Sample:
    #this is class variable
    x=10
    #this is class method
    @classmethod#decorator
    def modify(cls):
        cls.x+=1
        
#create two instances
s1=Sample()
s2=Sample()

print(f's1={s1.x}')
print(f's12={s2.x}')
    
#modify x in s1
s1.modify()
print(f's1={s1.x}')
print(f's2={s2.x}')



# In Python, a decorator is a design pattern that allows you to extend or modify the behavior of functions or methods without directly modifying their code. Decorators are functions themselves that wrap another function or method, allowing you to execute code before and/or after the wrapped function runs, or to modify its arguments or return value.

# Decorators are commonly used for tasks such as logging, access control, memoization, and more. They are denoted by the @decorator_name syntax placed before the function or method definition.