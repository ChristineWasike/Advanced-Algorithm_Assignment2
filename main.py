# Problem: Find the cost of the min spanning tree in a giving graph using Prim's Algorithm
class Graph:
    def __init__(self, nodes):
        self.N = nodes
        self.graph = [[1 for col in range(nodes + 1)] for row in range(nodes + 1)]

    def print_mst(self, parent):
        print("Edge  \tWeight")
        for node in range(1, self.N):
            print(parent[node] + 1, "->", node + 1, "\t:", self.graph[node][parent[node]])

    def min_key(self, node_dict, mst_set):
        min_value = float('inf')
        min_index = 0
        for n in range(self.N):
            if node_dict[n] < min_value and mst_set[n] is False:
                min_value = node_dict[n]
                min_index = n
        return min_index

    def min_spanning_tree(self):
        # Create a set to track nodes already in MST
        mst_set = [False] * self.N

        # Create a dictionary of all nodes and initialise values as INF apart from starting node set to 0
        node_dict = [float('inf')] * self.N
        parent = [None] * self.N

        # Set the value of the starting node to 0
        node_dict[0] = 0

        # Tracking the root's parent which has no parent.
        parent[0] = -1

        # As long as the set doesn’t contain all nodes run the code in it
        for node in range(self.N):  # Time complexity = T(v2)
            # pick the minimum valued key in mst_set
            m = self.min_key(node_dict, mst_set)

            # add selected node to mst_set
            mst_set[m] = True

            # iteratively update all of u’s adjacent node values in the dictionary
            for n in range(self.N):
                # check for adjacent nodes to u and that the nodes aren’t in mst_set and that the established
                # weight is less than the value of what is in the dictionary’s respective key
                if 0 < self.graph[m][n] < node_dict[n] and mst_set[n] is False:
                    # updating the key-value pair with the new weight
                    node_dict[n] = self.graph[m][n]
                    parent[n] = m
        self.print_mst(parent)


if __name__ == '__main__':
    input_graph = Graph(7)
    input_graph.graph = [[0, 28, 0, 0, 0, 10, 0],
                         [28, 0, 16, 0, 0, 0, 14],
                         [0, 16, 0, 12, 0, 0, 0],
                         [0, 0, 12, 0, 22, 0, 18],
                         [0, 0, 0, 22, 0, 25, 24],
                         [10, 0, 0, 0, 25, 0, 0],
                         [0, 14, 0, 18, 24, 0, 0]]
    input_graph.min_spanning_tree()
