import numpy as np
import heapq
 
class DisjointSet:                          # Implements Disjoint Set (Union-Find) with Path Compression and Union by rank
     def __init__(self, n):
         self.parent = list(range(n))        # Each node is its own parent initially
         self.rank = [0] * n                 # Track tree height for optimization
 
     # Find the root of node u with path compression
     def find(self, u):
         if self.parent[u] != u:
             self.parent[u] = self.find(self.parent[u])
         return self.parent[u]
 
     """
         Merge two sets containing u and v
         Returns True if merged, False if already in the same set
     """
     def union(self, u, v):
         root_u = self.find(u)
         root_v = self.find(v)
         
         if root_u != root_v:
             if self.rank[root_u] > self.rank[root_v]:
                 self.parent[root_v] = root_u
             elif self.rank[root_u] < self.rank[root_v]:
                 self.parent[root_u] = root_v
             else:
                 self.parent[root_v] = root_u
                 self.rank[root_u] += 1
             return True
         return False
 
 # Implement Prim's algo to find the Minimum Spanning Tree (MST)
def prim_mst(graph, start):
     N = len(graph)              # Number of nodes
     visited = [False] * N       # Keep track of visited nodes
     min_heap = [(0, start)]     # Priority queue storing (weight, node)
     mst_edges = []              # List to store MST edges
     total_weight = 0            # Sum of weights in MST
 
     while len(mst_edges) < N - 1:
         weight, node = heapq.heappop(min_heap)      # Get the smallest edge
         if visited[node]:                       # Skip if node is already visited
             continue
         
         visited[node] = True            # Mark node as visited
         total_weight += weight          # Add weight to MST total
         
         # Explore the neighbors
         for neighbor, w in enumerate(graph[node]):
             if w > 0 and not visited[neighbor]:                 # If edge exists and has not been visited
                 heapq.heappush(min_heap, (w, neighbor))         # Push to heap
                 mst_edges.append((node + 1, neighbor + 1, w))   # Store edge (1-based)
 
     return mst_edges, total_weight
 
 # Implement the Kruskal's algorithm to find the MST
def kruskal_mst(edges, n):
     edges.sort(key=lambda x: x[2])          # Sort edge by weight
     ds = DisjointSet(n)                     # Initialize disjoint set
     mst_edges, total_weight = [], 0
     
     for u, v, w in edges:
         if ds.union(u - 1, v - 1):          # Convert 1-based to 0-based index
             mst_edges.append((u, v, w))
             total_weight += w
         if len(mst_edges) == n - 1:         # MST contains (N-1) edges
             break
     
     return mst_edges, total_weight
 
 # Construct the Adjacent matrix
N = 9  # Number of nodes
adj_matrix = np.zeros((N, N))
 
edges = [
     (1, 2, 4), (1, 5, 1), (1, 6, 2), (2, 3, 7), (2, 5, 5), (3, 4, 1), (3, 6, 8),
     (4, 6, 6), (4, 7, 4), (4, 8, 3), (5, 6, 9), (5, 7, 10), (6, 7, 2), (7, 8, 8), (8, 9, 1)
 ]
 
 # Fill the adjacency matrix based on edge connections
for u, v, w in edges:
     adj_matrix[u - 1][v - 1] = w  # Subtract 1 to convert 1-based index to 0-based
     adj_matrix[v - 1][u - 1] = w  # Since the graph is undirected, mirror the values
 
 # Print out the matrix
print("Adjacency matrix:")
print(adj_matrix)
 
 # Run Prim's algorithm
start_node = 0  # Start from node 0 (1-based index would be node 1)
prim_result, prim_weight = prim_mst(adj_matrix, start_node)
 
print("\nPrim’s algorithm result (MST edges):")
for u, v, w in prim_result:
     print(f"{u} - {v} (Weight: {w})")
print(f"Total weight of MST (Prim's): {prim_weight}")
 
 # Run Kruskal's algorithm
kruskal_result, kruskal_weight = kruskal_mst(edges, N)
 
print("\nKruskal’s algorithm result (MST edges):")
for u, v, w in kruskal_result:
     print(f"{u} - {v} (Weight: {w})")
print(f"Total weight of MST (Kruskal's): {kruskal_weight}")