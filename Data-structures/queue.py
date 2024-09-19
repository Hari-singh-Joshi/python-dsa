
class Queue:
    
    def __init__(self):
        self.items=[]
        
    def is_empty(self):
        return len(self.items)==0
    
    def enqueue(self,item):
        self.items.append(item)
        
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print('list is empty')
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print('list is empty')
            
    def display(self):
        if self.is_empty():
            print('list is empty')
            return
        else:
            
            print(self.items)
    def size(self):
        return len(self.items)
    
    def reverse(self):
        self.items.reverse()    
if __name__ == "__main__":
    queue=Queue()
    while(True):
        print('1. Enqueue')
        print('2. Dequeue')
        print('3. Peek')
        print('4. Display')
        print('5. size')
        print('6. reverse')
        print('7.exit')
        
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
            print('Queue size:', queue.size())
        elif choice==6:
            
            queue.reverse()
        elif choice==7:
            break
        else:
            print('Invalid choice. Please enter a valid option.')
        
                
                    