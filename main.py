from graph import Graph
from graph import Edge
from set import Set
import unittest

grr = Graph()

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


class TestSet(unittest.TestCase):

    def setUp(self):
        self.set1 = Set()
        self.set1.add(1)
        self.set1.add(2)
        self.set1.add(3)
        self.set1.add(4)

        self.set2 = Set()
        self.set2.add(5)
        self.set2.add(6)
        self.set2.add(7)

    def test_add(self):
        self.assertEqual(self.set1.set, [1, 2, 3, 4])
        self.assertEqual(self.set2.set, [5, 6, 7])

    def test_size(self):
        self.assertEqual(self.set1.size(), 4)
        self.assertEqual(self.set2.size(), 3)

    def test_isMember(self):
        self.assertTrue(self.set1.isMember(3))
        self.assertFalse(self.set1.isMember(5))

    def test_isEmpty(self):
        self.assertFalse(self.set1.isEmpty())

    def test_union(self):
        self.set1.union(self.set2)
        self.assertEqual(self.set1.set, [1, 2, 3, 4, 5, 6, 7])


class TestGraph(unittest.TestCase):

    def setUp(self):
        self.grr = Graph()
        self.grr.addEdge(1, 2, 3)
        self.grr.addEdge(1, 2, 4)
        self.grr.addEdge(1, 8, 8)
        self.grr.addEdge(2, 3, 8)
        self.grr.addEdge(2, 8, 11)
        self.grr.addEdge(3, 4, 7)
        self.grr.addEdge(3, 6, 4)
        self.grr.addEdge(3, 9, 2)
        self.grr.addEdge(4, 5, 9)
        self.grr.addEdge(4, 6, 14)
        self.grr.addEdge(5, 6, 10)
        self.grr.addEdge(6, 7, 2)
        self.grr.addEdge(7, 8, 1)
        self.grr.addEdge(8, 9, 7)
        self.grr.addEdge(9, 7, 6)

        self.A = Graph()
        self.A.addEdge(7, 8, 1)
        self.A.addEdge(3, 9, 2)
        self.A.addEdge(6, 7, 2)
        self.A.addEdge(1, 2, 3)
        self.A.addEdge(3, 6, 4)
        self.A.addEdge(3, 4, 7)
        self.A.addEdge(1, 8, 8)
        self.A.addEdge(4, 5, 9)

    def test_Kruskal(self):
        mst = []
        mst = self.grr.Kruskal()

        for i in range(len(mst)):
            assert mst[i] == self.A.graph[i]


if __name__ == '__main__':
    unittest.main()
