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


def bfs(start):
    if start not in graph:
        print(f"Vertex '{start}' not found in the graph.")
        return

    visited = []
    queue = [start]

    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.append(vertex)
            print(vertex, end=" ")

            for neighbor in graph[vertex]:
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)


while True:
    print("\nOptions:")
    print("1. Add Vertex")
    print("2. Add Edge")
    print("3. Perform BFS")
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
        start_vertex = input("Enter the starting vertex for BFS: ")
        print("BFS Traversal:", end=" ")
        bfs(start_vertex)
        print()
    elif choice == '4':
        print("Exiting the program. Goodbyeeeeeeeeeeeeeeeeee!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 4.")
