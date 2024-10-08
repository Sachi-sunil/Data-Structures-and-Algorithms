class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

doubly_linked_list = DoublyLinkedList()

while True:
    choice = input("\n1. Add Node\n2. Display List\n3. Exit\nChoose an option: ")
    if choice == '1':
        data = input("Enter data for the node: ")
        doubly_linked_list.add(data)
    elif choice == '2':
        doubly_linked_list.display()
    elif choice == '3':
        print("EXITING!")
        break
    else:
        print("Invalid choice!")
