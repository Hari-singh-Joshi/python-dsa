class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self) -> None:
        self.head=None
    
    def insert(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            return
            
        temp=self.head
        while temp.next:
            temp=temp.next
        
        temp.next=new_node
        
    def deletes(self):
        if self.head:
            temp=self.head
            while temp.next.next:
                temp=temp.next
            print(f'{temp.next.data} is deleted')
            temp.next=None
    def display(self):
        if self.head:
            temp=self.head
            while temp:
                print(f'{temp.data}->',end="")
                temp=temp.next
            print("None")

                
        
    
        
    
    
    

if __name__ == "__main__":
    linkedlist=Linkedlist()
    
    linkedlist.insert(20)
    linkedlist.insert(30)
    linkedlist.insert(80)
    linkedlist.deletes()
    linkedlist.display()