class Student:
    #this is constructor
    def __init__(self,n='.',m=0):
        self.name=n
        self.marks=m
    def display(self):
        print(f'my name is {self.name}')
        print(f'my mark is {self.marks}')
#constructor is called without any arguments
s=Student()
s.display()

#costrcutor with argument
s=Student('hari singh joshi',890)
s.display()