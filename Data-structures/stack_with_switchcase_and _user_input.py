class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
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
            raise IndexError("peek from empty stack")

    def size(self):
        return len(self.items)


def switch_case(args, stack):
    if args == 1:
        n = input("Enter the element you want to insert: ")
        stack.push(n)
        print(f"'{n}' is inserted")
    elif args == 2:
        if not stack.is_empty():
            print(f"'{stack.pop()}' is popped")
            print("Stack after pop:", stack.items)
        else:
            print("Stack is empty")
    elif args == 3:
        try:
            print("Peek:", stack.peek())
        except IndexError as e:
            print(e)
    elif args == 4:
        exit()


stack = Stack()
while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    switch_case(choice, stack)
