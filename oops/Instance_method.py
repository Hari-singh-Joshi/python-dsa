#Instance method to process the data of the objects
#Python program using a student class with instance methods to process the data of several students.
class Student:
    #This is a constructor
    def __init__(self,n='',m=0) -> None:
        self.name=n
        self.marks=m
        pass
    #this is an instance method
    def display(self):
        print(f'hi, {self.name}')
        print(f'your marks,{self.marks}')
    
    #to calculate grades based on marks
    def calculate(self):
        if(self.marks>=600):
            print('You got First Grade')
        elif(500<=self.marks<=600):
            print('Your Grade is Second')
        elif(350<=self.marks<500):
            print('You got Third Grade ')
        
#create instances with some data from keywords
n=int(input('How Many Students?'))
i=0
while(i<n):
    name=input('Enter Name..')
    marks=int(input('enter your marks..'))
    #create student class instance and store data
    s=Student(name,marks)
    s.display()
    s.calculate()
    i+=1
    print('---------------------')
            