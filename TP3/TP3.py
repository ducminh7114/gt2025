class Graph:
     def __init__(self, nodes):
         self.nodes = nodes
         self.adj_list = {node: [] for node in range(1, nodes + 1)}  # Dictionary to store adjacency list
 
     def add_edge(self, u, v):
         """Adds a directed edge from node u to node v"""
         self.adj_list[u].append(v)
 
     def inorder_traversal(self, node):
         """Performs an Inorder traversal from a given node"""
         if node not in self.adj_list:
             return
 
         children = sorted(self.adj_list[node])  # Sort children to mimic left-to-right order
         mid = len(children) // 2  # Find the middle for Inorder behavior
 
         # Visit left children first
         for i in range(mid):
             self.inorder_traversal(children[i])
 
         # Visit root (current node)
         print(node, end=" ")
 
         # Visit right children
         for i in range(mid, len(children)):
             self.inorder_traversal(children[i])
 
 
 # Create graph instance
graph = Graph(8)
 
 # Add directed edges (based on the given graph)
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(2, 4)
graph.add_edge(2, 5)
graph.add_edge(4, 8)
graph.add_edge(5, 6)
graph.add_edge(5, 7)
 
 # Input node for Inorder traversal
x = int(input("Enter the starting node: "))
print("Inorder Traversal from node", x, ":")
graph.inorder_traversal(x)