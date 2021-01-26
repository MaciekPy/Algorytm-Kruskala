from graph import Graph
from graph import Edge


grr = Graph(9)


grr.addEdge(1, 2, 4)
grr.addEdge(1, 8, 8)
grr.addEdge(2, 3, 8)
grr.addEdge(2, 8, 11)
grr.addEdge(3, 4, 7)
grr.addEdge(3, 6, 4)
grr.addEdge(3, 9, 2)
grr.addEdge(4, 5, 9)
grr.addEdge(4, 6, 14)
grr.addEdge(5, 6, 10)
grr.addEdge(6, 7, 2)
grr.addEdge(7, 8, 1)
grr.addEdge(8, 9, 7)
grr.addEdge(9, 7, 6)

print("Wszystkie krawedzie grafu : ")
grr.display()

A = []
A = grr.Kruskal()

print("\nKrawedzie tworzace minimalne drzewo rozpinajece : ")

for i in range(len(A)):
    print(str(i+1) + ". " + str(A[i].u) + ", " + str(A[i].v)
          + ", " + str(A[i].w))
