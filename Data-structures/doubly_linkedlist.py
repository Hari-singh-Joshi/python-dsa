class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
 #linkedlist started here       
class Linkedlist:
    def __init__(self):
        self.head=None
        
    #addition of element at first node
    def add_at_start(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        
        
        
        new_node.next=self.head
        self.head.prev=new_node.data
        self.head=new_node
        
    #addition of element at given position. element will be added after a given position
    def add_at_position(self,data,position):
        if position==0:
            self.add_at_start(data) #calling function directly
            return 
        new_node=Node(data)
        current=self.head
        for _ in range(position-1):
            if current is None:
                print('position is out of bounds')
                return
            current=current.next
        if current is None:
            print('position is out of bound')
            return
        new_node.next=current.next
        if current.next:
            current.next.prev=new_node
                 
        
        new_node.prev=current
       
        current.next=new_node
        
    def add_at_end(self,data):
        new_node=Node(data)
        #if there is no node it will add node at first position
        if self.head is None:
            self.add_at_start(data)
            return
        current=self.head
        while current.next:
            current=current.next
        new_node.prev=current.data
        current.next=new_node
        
    def remove_at_position(self,position):
        if self.head is None:
            print('list is empty')
            return
        temp=self.head
        
        if position==0:
            if self.head.next is not None:  # Check if there's a next node
                self.head.next.prev=None
            self.head=temp.next
            temp.next=None
            return
        for _ in range(position - 1):
            if temp is None or temp.next is None:
                print("Position out of bounds")
                return
            temp = temp.next
        if temp is None or temp.next is None:
                print("Position out of bounds")
                return
            
        next_node=temp.next.next
           
        next_node.prev=temp
        temp.next=next_node
            
        
    def display(self):
        current=self.head
        while current:
            print(current.data,end='->')
            current=current.next
            
        print('None')
        
    def delete(self, key):
        temp = self.head

        # Case when the key is found at the head
        if temp is not None and temp.data == key:
            self.head = temp.next
            if temp.next is not None:
                temp.next.prev = None
            temp = None
            return

        # Traverse the list to find the key
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        # If the key is not found
        if temp is None:
            print('Key is not found')
            return

        # Remove the node containing the key
        prev.next = temp.next
        if temp.next is not None:
            temp.next.prev = prev


                
    def search(self,key):
        
        current=self.head
        while(current.next):
            
            if current.data==key:
                
                print('element found')
                return
            
            current=current.next
        print('not found')
            
    
    def reverse(self):
        if self.head is None:
            return
        current=self.head
        while current:
            temp=current.prev
            current.prev=current.next
            current.next=temp
            current=current.prev
        if temp is not None:
            self.head=temp.prev
            

            
            
        
        




if __name__ == "__main__":
    linked_list = Linkedlist()

    while True:
        print("\n1. Add at start")
        print("2. Add at position")
        print("3. Add at end")
        print("4. Remove at position")
        print("5. Delete")
        print("6. Search")
        print("7. Reverse")
        print("8. Display")
        print("9. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = input("Enter data: ")
            linked_list.add_at_start(data)
        elif choice == 2:
            data = input("Enter data: ")
            position = int(input("Enter position: "))
            linked_list.add_at_position(data, position)
        elif choice == 3:
            data = input("Enter data: ")
            linked_list.add_at_end(data)
        elif choice == 4:
            position = int(input("Enter position: "))
            linked_list.remove_at_position(position)
        elif choice == 5:
            key = input("Enter element to delete: ")
            linked_list.delete(key)
        elif choice == 6:
            key = input("Enter element to search: ")
            linked_list.search(key)
        elif choice == 7:
        #     linked_list.reverse()
        elif choice == 8:
            
            linked_list.display()
        elif choice == 9:
            break
        else:
            print("Invalid choice. Please enter a valid option.")
