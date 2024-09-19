#abstract class works like interface
from abc import *
class MyClass(ABC):
    @abstractmethod
    def connect(self):
        pass
    @abstractmethod
    def disconnect(self):
        pass
    
#this is a subclass
class oracle(MyClass):
    def connect(self):
        print('connecting to the oracle database......')
        
    def disconnect(self):
        print('disconnected from oracle.')
        
#this is another subclass
class sybase(MyClass):
    def connect(self):
        print('connecting to the sybase database......')
        
    def disconnect(self):
        print('disconnected from sybase.')
        
class Database:
    #accept database name as string
    str=input('Enter database name')
    classname=globals()[str]
    
    #create an object to that class
    x=classname()
    
    #call the connect and disconnect methods
    x.connect()
    x.disconnect()