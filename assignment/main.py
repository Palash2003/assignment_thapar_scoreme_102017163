from collections import deque

def longest_path(graph: list) -> int:
    topo_order = topological_sort(graph)
    
    return calculate_longest_path(graph, topo_order)

def topological_sort(graph):
    n = len(graph)
    indegree = [0] * n
    for u in range(n):
        for v, w in graph[u]:
            indegree[v] += 1
            
    queue = deque([u for u in range(n) if indegree[u] == 0])
    topo_order = []
    
    while queue:
        u = queue.popleft()
        topo_order.append(u)
        for v, w in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)
    
    return topo_order

def calculate_longest_path(graph, topo_order):
    n = len(graph)
    distance = [0] * n    
    longest_path_length = 0
    
    for u in topo_order:
        for v, w in graph[u]:
            if distance[v] < distance[u] + w:
                distance[v] = distance[u] + w
                longest_path_length = max(longest_path_length, distance[v])
    
    return longest_path_length