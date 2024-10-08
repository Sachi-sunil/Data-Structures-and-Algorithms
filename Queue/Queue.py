queue = []

def enqueue(item):
    queue.append(item)
    print(f"Enqueued: {item}")

def dequeue():
    if not is_empty():
        removed_item = queue.pop(0)
        print(f"Dequeued: {removed_item}")
        return removed_item
    else:
        print("Queue is empty!")

def is_empty():
    return len(queue) == 0

def display():
    if not is_empty():
        print("Queue:", " -> ".join(str(item) for item in queue))
    else:
        print("Queue is empty.")

while True:
    choice = input("\n1. Enqueue\n2. Dequeue\n3. Display Queue\n4. Exit\nChoose an option: ")
    if choice == '1':
        item = input("Enter item to enqueue: ")
        enqueue(item)
    elif choice == '2':
        dequeue()
    elif choice == '3':
        display()
    elif choice == '4':
        print("BYE BYE !")
        break
    else:
        print("Invalid choice!")
