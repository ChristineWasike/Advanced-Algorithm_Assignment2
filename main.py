class Graph():
    def __init__(self, nodes):
        self.N = nodes
        self.graph = [[1 for column in range(nodes + 1)] for row in range(nodes + 1)]

    def min_key(self, node_dict, mst_set):
        min_value = float('inf')
        min_index = 0
        for n in range(self.N):
            if node_dict[n] < min_value and n not in mst_set:
                min_value = node_dict[n]
                min_index = n
        return min_index

    def print_mst(self, parent):
        print("Edge  \tWeight")
        for node in range(1, self.N):
            print(parent[node], "->", node, "\t", self.graph[node][parent[node]])


def function(graph):
    node_dict = dict(zip(range(1, 8), [float('inf')] * len(graph)))
    return node_dict


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    input_graph = [[0, 28, 0, 0, 0, 10, 0],
                   [28, 0, 16, 0, 0, 0, 14],
                   [0, 16, 0, 12, 0, 0, 0],
                   [0, 0, 12, 0, 22, 0, 18],
                   [0, 0, 0, 22, 0, 25, 24],
                   [10, 0, 0, 0, 25, 0, 0],
                   [0, 14, 0, 18, 24, 0, 0]]
    # print(function(input_graph))

    for i in range(1, 6 + 1):
        print(i)
