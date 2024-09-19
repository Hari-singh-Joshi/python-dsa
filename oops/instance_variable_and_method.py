class Student:
    def __init__(self):
        self.name="hairsh"
        self.id=44
        self.age=22
        self.marks=82
    #this is an instance method
    def talk(self):
        print(f'hi i am {self.name}')
        print(f'my id is{self.age}')
        print(f'my age is {self.age}')
        print(f'my mark in science {self.marks}')
#creating object of student class
s=Student()
s.talk()