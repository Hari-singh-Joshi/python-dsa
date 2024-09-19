class Queue:
    import array
    
    def __init__(self):
        self.arr=array.array('i',[0]*5)
        
    def is_empty(self):
        return len(self.arr)==0 # if length of the string is equal to 0 it will return True otherwise false
    
    def is_full(self):
        return len(self.arr)==5       
            
    def enqueue(self,item):
        if not self.is_full():
            
            self.arr.append(item)
        else:
            print('list is full already')
        
    def dequeue(self):
        if self.is_empty():
            print('arr is empty')
        else:
            self.arr.pop(0)
        
    def peek(self):
        if not self.is_empty():
            return self.arr[0]
        else:
            print("arr is empty")
            
    def display(self):
        if not self.is_empty():
            print(self.arr)
            
        else:
            print('sorry! arr is empty')    
       
if __name__ == "__main__":
    queue=Queue()
    while(True):
        print('1. Enqueue')
        print('2. Dequeue')
        print('3. Peek')
        print('4. Display')
       
        print('5.exit')
        
        choice=int(input('Enter your choice: '))
        if choice==1:
            data=input('enter your data')
            queue.enqueue(data)
        elif choice==2:
            print('Dequeued item:', queue.dequeue())
        elif choice==3:
            print('Front item:', queue.peek())
        elif choice==4:
            print('Queue:', end=' ')
            queue.display()
     
        elif choice==5:
            break
        else:
            print('Invalid choice. Please enter a valid option.')
             
