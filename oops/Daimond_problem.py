class A:
    def method(self):
        print("Method from class A")

class B(A):
    def method(self):
        print("Method from class B")

class C(A):
    def method(self):
        print("Method from class C")

class D(B, C):
    pass

# Create an instance of class D
obj = D()

# Call method from class D
obj.method()
print(D.mro())


