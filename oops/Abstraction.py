class MyClass:
    #this is constructor
    def __init__(self):
        self.x=1#public variable
        self.__y=2#private variable
    #instance method to access variables
    def display(self):
        print(self.x)
        print(self._MyClass__y)
    
print('Accessing variables through method:')
m=MyClass()
m.display()

print('Accessing variables throuogh methods')
print(m.x)
print(m._MyClass__y)
               