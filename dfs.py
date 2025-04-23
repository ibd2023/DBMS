'''
Depth-First Search (DFS) dives as deep as possible down one path before backtracking. 
Starting from a source node, it visits a neighbor, then a neighbor of that neighbor, 
and so on, using recursion (or an explicit stack) to backtrack when it hits a dead end.

'''
# “visit → recurse on neighbors.”

def dfs(graph, node, visited=None, order=None):
    if visited is None:
        visited = set()
        order   = []

    visited.add(node)        # mark current node visited
    order.append(node)       # record visit order

    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited, order)

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

# Run DFS starting from 'A'
print(dfs(graph, 'A'))  # Possible output: ['A', 'B', 'D', 'E', 'F', 'C']
