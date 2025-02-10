class Graph():

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = set()
        self.graph[u].add(v)
        if v not in self.graph:
            self.graph[v] = set()
        self.graph[v].add(u)