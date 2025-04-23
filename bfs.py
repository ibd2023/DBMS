# “dequeue → visit → enqueue neighbors.”
''' 
Breadth-First Search (BFS) explores a graph level by level. 
Starting from a source node, it visits all its immediate neighbors 
before moving on to nodes at distance 2, distance 3, and so on. 
Internally it uses a FIFO queue to keep track of the “frontier” of nodes to visit next.

'''
from collections import deque

def bfs(graph, start):
    visited = set([start])       # mark the start vertex as visited
    queue = deque([start])       # initialize queue with the start vertex
    order = []                   # to record traversal order

    while queue:
        node = queue.popleft()   # dequeue next node
        order.append(node)

        # enqueue all unvisited neighbors
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order

# Example dataset as an adjacency list:
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Run BFS starting from 'A'
print(bfs(graph, 'A'))   # Output: ['A', 'B', 'C', 'D', 'E', 'F']
