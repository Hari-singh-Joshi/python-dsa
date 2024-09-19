# a program to create a static method that counts the number of instances created for a class
class Myclass:
    n=0
    #constructor that increment n when an instance is created
    def __init__(self) -> None:
        Myclass.n+=1
        pass
    #this is static method with decorator to display no. of instances
    @staticmethod
    def noobject():
        print(f'number of instances created:{Myclass.n}')
        
#create 3 instaces
obj1=Myclass()
obj2=Myclass()
obj2=Myclass()
Myclass.noobject()