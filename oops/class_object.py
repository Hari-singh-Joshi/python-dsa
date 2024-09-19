class employee:
    def putdata(self):
        self.id=int(input('enter employee id'))
        self.name=input('enter name')
        self.salary=float(input('enter salary'))
    
    def display(self):
        print("employee id:",self.id)
        print("employee name:",self.name)
        print("employee salary",self.salary)
        
a=employee()
a.putdata()
a.display()