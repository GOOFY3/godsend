ttclass Vertex(object):
    def __init__(self, name):
        self.name = name
        self.node = None
class Node(object):
    def __init__(self, height, nodeId, parentNode):
        self.height = height
        self.nodeId = nodeId
        self.parentNode = parentNode
class Edge(object):
    def __init__(self, weight, startVertex, targetVertex):
        self.weight = weight
        self.startVertex = startVertex
        self.targetVertex = targetVertex
    def __cmp__(self, other):
        return cmp(self.weight, other.weight)
class DisjointSets(object):
    # def __init__(self, vertexList):
    #     self.vertexList = vertexList
    #     self.rootNodes = []
    #     self.nodeCount = 0
    #     self.setCount = 0
    #     self.makeSets(vertexList)
    # def makeSets(vertexList):
    #     for v in vertexList:
    #         self.makeSets(v)
    # def makeSets(self, vertex):
    #     node = Node(0, len(self.rootNodes), None)
    def __init__(self, vertexList):
        self.vertexList = vertexList
        self.rootNodes = []
        self.nodeCount = 0
        self.setCount = 0
        self.makeSets(vertexList)
    def makeSets(self, vertexList):
        for v in vertexList:
            self.makeSet(v)
    def makeSet(self, vertex):
        node = Node(0, len(self.rootNodes), None)
        vertex.parentNode = node
        self.nodeCount += 1
        self.setCount += 1
