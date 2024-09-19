class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):  # Dog class inherits from Animal class
    def bark(self):
        print("Dog barks")

# Create an instance of the Dog class
my_dog = Dog()

# Call methods of the Dog class
my_dog.bark()   # Outputs: Dog barks
my_dog.speak()  # Outputs: Animal speaks
