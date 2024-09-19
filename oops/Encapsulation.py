# Encapsulation is mechanism where the data(variables) and the code (methods) that act on the data will bind together. for example, if we write a class, we wrtie the variables and methods inside the class. thus, class is binding them together. so class is an example of ensapulation. 
class Car:
    def __init__(self,make,model,year):
        self._make=make#protected attribute
        self._model=model#protected attribute
        self._year=year
        self._odometer_reading=0
        
    def get_description(self):
        return f"{self._year} {self._make} {self._model}"
    
    def get_odometer_reading(self):
        return self._odometer_reading
    
    def update_odometer(self,mileage):
        if mileage>=self._odometer_reading:
            self._odometer_reading=mileage
        else:
            print("you cant roll back an odometer")
            
    def increment_odometer(self,miles):
        if miles>=0:
            self._odometer_reading+=miles
        else:
            print('you cannot decrement the odometer')
            
mycar=Car('toyata','camry',2021)
print(mycar.get_description())

# Trying to access and modify protected attributes directly
# This won't work due to encapsulation
print(mycar._make)  # Output: Toyota (This will work but it's against encapsulation principles)
mycar._odometer_reading = 10000  # Direct modification is not recommended
print(mycar.get_odometer_reading()) 
# Output: 10000 (This is why encapsulation is important)

# Using methods to update the odometer reading
myc9-='ar.update_odometer(15000)
print(mycar.get_odometer_reading())  # Output: 15000
mycar.increment_odometer(500)
print(mycar.get_odometer_reading())  # Output: 15500