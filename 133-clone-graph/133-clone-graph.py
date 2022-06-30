"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:

    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = {}
        def dfs(dps_node):
            if dps_node in visited:
                return visited[dps_node]
            new_node = Node(dps_node.val)
            visited[dps_node] = new_node
            for i in dps_node.neighbors:
                new_node.neighbors.append(dfs(i))
            return new_node
        return dfs(node) if node else None