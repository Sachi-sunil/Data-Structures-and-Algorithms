class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
        else:
            tail = self.head.prev
            tail.next = new_node
            new_node.prev = tail
            new_node.next = self.head
            self.head.prev = new_node

    def display(self):
        if not self.head:
            print("List is empty.")
            return
        current = self.head
        while True:
            print(current.data, end=" <-> ")
            current = current.next
            if current == self.head:
                break
        print("moving back to head.")

circular_doubly_linked_list = CircularDoublyLinkedList()

while True:
    choice = input("\n1. Add Node\n2. Display List\n3. Exit\nChoose an option: ")
    if choice == '1':
        data = input("Enter data for the node: ")
        circular_doubly_linked_list.add(data)
    elif choice == '2':
        circular_doubly_linked_list.display()
    elif choice == '3':
        print("EXITINGG!")
        break
    else:
        print("Invalid choice!")
