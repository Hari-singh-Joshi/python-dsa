class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


# data will be added after the given position
    def add_at_position(self, data, position):
        if position == 0:
            self.add_at_start(data)
            return
        new_node = Node(data)
        current = self.head
        for _ in range(position - 1):
            if current is None:
                print("Position out of bounds")
                return
            current = current.next
        if current is None:
            print("Position out of bounds")
            return
        new_node.next = current.next
        current.next = new_node

    
    def add_at_end(self, data):
        new_node = Node(data)
        #if there is no node it will add first new node
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

# data will be deleted after given position
    def remove_at_position(self, position):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        if position == 0:
            self.head = temp.next
            temp = None
            return
        for _ in range(position - 1):
            if temp is None or temp.next is None:
                print("Position out of bounds")
                return
            temp = temp.next
        if temp is None or temp.next is None:
            print("Position out of bounds")
            return
        next_node = temp.next.next
        temp.next = None
        temp.next = next_node

    def delete(self, key):
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp == None:
            print("Key not found")
            return
        prev.next = temp.next
        temp = None

    def search(self, key):
        current = self.head
        while current is not None:
            if current.data == key:
                print("Element found")
                return
            current = current.next
        print("Element not found")

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


if __name__ == "__main__":
    linked_list = LinkedList()

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
            linked_list.reverse()
        elif choice == 8:
            linked_list.display()
        elif choice == 9:
            break
        else:
            print("Invalid choice. Please enter a valid option.")
