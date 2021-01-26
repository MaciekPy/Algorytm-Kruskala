from set import Set


class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w


class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        edge = Edge(u, v, w)
        self.graph.append(edge)

    def display(self):
        for i in range(len(self.graph)):
            print(str(self.graph[i].u) + ", " + str(self.graph[i].v)
                  + ", " + str(self.graph[i].w))

    def findInSet(self, subsets, vertex):
        for i in range(len(subsets)):
            if subsets[i].isMember(vertex):
                return subsets[i].set[0]
        return -1

    def Kruskal(self):
        A = []
        subsets = list()

        # Dla każdego wierzchołka stwórz zbiór
        for i in range(self.V):

            subsets.append(Set())
            subsets[i].add(i+1)

        # Posortować liste krawędzi rosnąco
        sortedEdges = []
        sortedEdges = sorted(
            self.graph, key=lambda Edge: Edge.w, reverse=False)

        for i in range(len(sortedEdges)):

            x = self.findInSet(subsets, sortedEdges[i].u)
            y = self.findInSet(subsets, sortedEdges[i].v)

            # Sprawdzanie czy dwa wierzhołki należą do tego samego zbioru
            if x != y:

                A.append(sortedEdges[i])

                subsets[x-1].union(subsets[y-1])

        return A
