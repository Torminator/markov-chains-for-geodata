import collections
from scc_algorithm import StronglyConnectedComponentFinder


class Graph:

    def __init__(self, vertices, edges):
        """
        The standard constructor with a list of vertices and a dictionary with represent the edges.
        The edges should be arranged the following way:
            vertex : list of vertices which are neighbors
        """
        self.vertices = list(vertices)
        self.edges = dict(edges)

    @classmethod
    def construct_from_matrix(cls, matrix, vertices=None):
        """
        Instead of creating the graph with a list of vertices and a dictionary of edges. We can construct
        a graph by using a distance/transiton matrix.
        """
        size = len(matrix)
        if vertices is None:
            vertices = [num for num in range(size)]

        edges = collections.defaultdict(list)
        for i, key in enumerate(vertices):
            edges[key] = [vertices[j] for j in range(size) if matrix[i][j] != 0]

        return cls(vertices, edges)

    def __str__(self):
        """
        With the help of this special function, we can print out the graph like this
        >>> print(g)
        Returns:
             a string
        """
        return '\n'.join(["{} -> {}".format(key, ",".join(val)) for key, val in self.edges.items()])

    def is_irreducible(self):
        """
        A simple auxiliary function creates a StronglyConnectedComponentFinder object. If the number of
        strongly connected components is equal to 1 then our graph is irreducible.
        Returns:
            bool: if the graph is irreducible
        """
        return len(StronglyConnectedComponentFinder(self).findcc()) == 1


if __name__ == "__main__":

    g = Graph.construct_from_matrix([[0.9, 0.1],[0.3, 0.7]], vertices=["A", "B"])
    print(g)

    g2 = Graph(list(range(4)), {0: [1], 1: [2], 2: [3], 3: [0, 1]})
    scc_finder = StronglyConnectedComponentFinder(g2)
    print(scc_finder.findcc())