import numpy as np
arr=np.zeros(7)
class Stack:
    def __init__(self) -> None:
        self.top=-1
        
    def isEmpty(self):
        return (self.top==-1)
    
    def isFull(self):
        return (self.top==len(arr)-1)
    
    def push(self,data):
        if self.isFull():
            print("the stack is overflow")
            return
        else:
            self.top+=1
            arr[self.top]=data
            print(f'pushed in stack {data}')
    
    def pop(self):
        if self.isEmpty():
            print('stack is underflow')
            return
        else:
            
            print(f'poped from stack{arr[self.top]}')  
            self.top-=1  
    def peek(self):
        if self.isEmpty():
            print('stack is underflow')
            return
        else:
            return arr[self.top]
        
if __name__ == "__main__":
    stack= Stack()
    
    while(True):
        print('1 for push')
        print('2 for pop')
        print('3 for display')
        print('4 for exit')
        
        choice=int(input('Enter your choice:'))
        if choice>0 and choice<5:
            if choice==1:
                data=input('enter your data')
                stack.push(data)
            elif choice==2:
                stack.pop()
            elif choice==3:
                print(arr[:stack.top+1])
            elif choice==4:
                break
        else:
            print('Kindly!enter the right choice')
            