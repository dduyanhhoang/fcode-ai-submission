import queue

MAX_N = 100005
inf = 1000000007

adj = [[] for _ in range(MAX_N)]  # Adjacency list
dist = [inf] * MAX_N  # Distances initialized to infinity
pred = [-1] * MAX_N  # Predecessors for path reconstruction

class Node:
    def __init__(self, vertex, w):
        self.vertex = vertex
        self.w = w

    def __lt__(self, other):
        return self.w < other.w

def Dijkstra(start):
    pq = queue.PriorityQueue()
    pq.put(Node(start, 0))
    dist[start] = 0
    while not pq.empty():
        tmp = pq.get()
        u = tmp.vertex
        if dist[u] < tmp.w:
            continue
        for edge in adj[u]:
            v = edge.vertex
            new_dist = dist[u] + edge.w
            if new_dist < dist[v]:
                dist[v] = new_dist
                pred[v] = u  # Update the predecessor for v
                pq.put(Node(v, dist[v]))

def reconstruct_path(start, end):
    if dist[end] == inf:
        return []
    path = []
    at = end
    while at != -1:
        path.append(at + 1)  # Convert to 1-indexed
        at = pred[at]
    path.reverse()
    return path

# Read graph
V, E = map(int, input().strip().split())
for _ in range(E):
    u, v, w = map(int, input().strip().split())
    u, v = u - 1, v - 1  # Convert to 0-indexed
    adj[u].append(Node(v, w))
    adj[v].append(Node(u, w))  # For undirected graph

# Dijkstra algorithm
start, end = map(int, input().strip().split())
start, end = start - 1, end - 1  # Convert to 0-indexed
Dijkstra(start)

# Output
if dist[end] != inf:
    print(f"The minimum cost is {dist[end]}")
    path = reconstruct_path(start, end)
    print(f"The optimal path is: {' -> '.join(map(str, path))}")
else:
    print("There is no path from {} to {}".format(start+1, end+1))  # Convert to 1-indexed for output
