class Vertex:
    def __init__(self,adj_list,data):
        self.adjacency_list = adj_list
        self.data = data

    def __str__(self):
        return str(self.data)