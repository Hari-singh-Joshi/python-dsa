class Stack:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.items)==0
    
    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("list is empty")
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peak from empty stack")
        
    def size(self):
        return len(self.items)
    
#making constructor
stack=Stack()
stack.push(1)
stack.push(2)
print("Stack:", stack.items)

print("Peek:", stack.peek())

print("Pop:", stack.pop())
print("Stack after pop:", stack.items)

print("Size of stack:", stack.size())

        