import collections


class StronglyConnectedComponentFinder:
    """
    The class implements the path-based strong components algorithm. The algorithm is recursive and needs
    to access to some global variables.
    Attrs:
        graph: the graph to calculate the strong connected components
        counter:  an help number to determine how many vertices have been reached and to compute the preOrder number
        preOrderNumbers: a dict to save the preOrder number of the vertices
        notAssignedVertices: a bookkeeper list to know which vertices have not been assigned to a component
        stackP: a deque
        stackS: a deque
        scComponents: a list of the strongly connected components aka. the solution
    """
    def __init__(self, graph):
        self.graph = graph
        self.counter = 0
        self.preOrderNumbers = dict()
        self.notAssignedVertices = list(self.graph.vertices)
        self.stackP = collections.deque()
        self.stackS = collections.deque()
        self.scComponents = list()

    def findcc(self):
        """
        We run over all vertices of the graph and call the function dfs. After we finished we return the solution.
        """
        for vertex in self.graph.vertices:
            if vertex not in self.preOrderNumbers:
                self.dfs(vertex)
        return self.scComponents

    def dfs(self, node):
        """
        Here is the real meat of the algorithm
        """
        self.preOrderNumbers[node] = self.counter
        self.counter = self.counter + 1
        self.stackP.append(node)
        self.stackS.append(node)
        for neighbor_vertex in self.graph.edges[node]:
            if neighbor_vertex not in self.preOrderNumbers:
                self.dfs(neighbor_vertex)
            elif neighbor_vertex in self.notAssignedVertices:
                while self.preOrderNumbers[self.stackP[-1]] > self.preOrderNumbers[neighbor_vertex]:
                    self.stackP.pop()

        if node == self.stackP[-1]:
            self.stackP.pop()
            component = []
            while node in self.stackS:
                vertex = self.stackS.pop()
                component.append(vertex)
                self.notAssignedVertices.remove(vertex)
            self.scComponents.append(component)

