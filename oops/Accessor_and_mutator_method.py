#without using constructor
class Student:
    #mutator method
    def setName(self,name):
        self.name=name
    
    #accessor method
    def getName(self):
        return self.name
    #mutator method
    def setMarks(self,marks):
        self.marks=marks
        
    #accessor method
    def getMarks(self):
        return self.marks
    
n=int(input('how many stuents?:'))
i=0
while(i<n):
    s=Student()
    name=input('Enter student name...')
    s.setName(name)
    marks=int(input('Enter the marks..'))
    s.setMarks(marks)
    
    #retreive data from student class instance
    print('hi' ,s.getName())
    print('your marks',s.getMarks())
    i+=1
    print('--------------') 