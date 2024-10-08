graph = {}

def add_vertex(vertex):
    if vertex not in graph:
        graph[vertex] = []
        print(f"Vertex '{vertex}' added.")

def add_edge(u, v):
    if u in graph and v in graph:
        graph[u].append(v)
        print(f"Edge from '{u}' to '{v}' added.")

def dfs(vertex, visited):
    if vertex not in visited:
        visited.append(vertex)
        print(vertex, end=" ")
        for neighbor in graph[vertex]:
            dfs(neighbor, visited)

while True:
    choice = input("\n1. Add Vertex\n2. Add Edge\n3. Perform DFS\n4. Exit\nChoose an option: ")
    if choice == '1':
        add_vertex(input("Enter vertex: "))
    elif choice == '2':
        add_edge(input("Enter starting vertex (u): "), input("Enter ending vertex (v): "))
    elif choice == '3':
        start_vertex = input("Enter starting vertex for DFS: ")
        print("DFS Traversal:", end=" ")
        dfs(start_vertex, [])
        print()
    elif choice == '4':
        print("Goodbyeeeeeeee!")
        break
    else:
        print("Invalid choice!")
