class Father:
    def height(self):
        print('Height is 6 fit')
        
class Mother:
    def color(self):
        print('color is brown')
        
class Child(Father,Mother): #passing class father and mother as argument
    pass
c=Child()
c.height()
c.color() 