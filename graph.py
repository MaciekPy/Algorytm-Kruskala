from set import Set


class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w

    def __str__(self):
        return '({self.u},{self.v},{self.w})'.format(self=self)

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return self.u == other.u and self.v == other.v and self.w == other.w
        return False


class Graph:

    def __init__(self):
        self.graph = []

    def addEdge(self, u, v, w):
        if isinstance(u, int) & isinstance(v, int):
            edge = Edge(u, v, w)
            self.graph.append(edge)
        else:
            raise TypeError('Nieprawidlowy typ zmiennej u lub v')

    def display(self):
        for i in range(len(self.graph)):
            print(self.graph[i])

    def findInSet(self, subsets, vertex):
        for i in range(len(subsets)):
            if subsets[i].isMember(vertex):
                return subsets[i].set[0]
        return -1

    def Kruskal(self):
        mst = []
        subsets = list()

        for i in range(len(self.graph)):

            subsets.append(Set())
            subsets[i].add(i+1)

        # Posortować liste krawędzi rosnąco

        self.graph.sort(key=lambda Edge: Edge.w, reverse=False)

        for e in self.graph:

            x = self.findInSet(subsets, e.u)
            y = self.findInSet(subsets, e.v)

            # Sprawdzanie czy dwa wierzhołki należą do tego samego zbioru
            if x != y:

                mst.append(e)
                subsets[x-1].union(subsets[y-1])

        return mst
