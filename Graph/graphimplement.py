graph = {}
def add_vertex(vertex):
    if vertex not in graph:
        graph[vertex] = []
        print(f"Vertex '{vertex}' has been added.")
    else:
        print(f"Vertex '{vertex}' already exists.")


def add_edge(u, v):
    if u in graph and v in graph:
        graph[u].append(v)
        print(f"Edge from '{u}' to '{v}' has been added.")
    else:
        print("One or both vertices not found. Please add them first.")


def display_graph():
    if not graph:
        print("The graph is currently empty.")
    else:
        print("Graph representation:")
        for vertex, edges in graph.items():
            print(f"  {vertex} -> {', '.join(edges) if edges else 'No edges'}")


while True:
    print("\nOptions:")
    print("1. Add Vertex")
    print("2. Add Edge")
    print("3. Display Graph")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == '1':
        vertex = input("Enter the vertex to add: ")
        add_vertex(vertex)
    elif choice == '2':
        u = input("Enter the starting vertex (u): ")
        v = input("Enter the ending vertex (v): ")
        add_edge(u, v)
    elif choice == '3':
        display_graph()
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 4.")
