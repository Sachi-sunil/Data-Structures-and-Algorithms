stack = []
def push(item):
    stack.append(item)
    print(f"{item} pushed to stack.")

def pop():
    if not is_empty():
        return stack.pop()
    else:
        return "Stack is empty."

def is_empty():
    return len(stack) == 0

def display():
    if not is_empty():
        print("Stack elements:", stack)
    else:
        print("Stack is empty.")

while True:
    print("\n1. Push\n2. Pop\n3. Display\n4. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        item = input("Enter the item to push: ")
        push(item)
    elif choice == '2':
        print("Popped item:", pop())
    elif choice == '3':
        display()
    elif choice == '4':
        break
    else:
        print("Invalid choice! Please try again.")
