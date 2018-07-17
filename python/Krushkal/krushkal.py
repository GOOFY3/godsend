class Vertex(object):
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
class DisjointSet(object):
    # def __init__(self, vertexList):
    #     self.vertexList = vertexList
    #     self.rootNodes = []
    #     self.nodeCount = 0
    #     self.setCount = 0
    #     self.makeSets(vertexList)
    # def makeSets(vertexList):
    #     for v in vertexList:
    #         self.makeSets(v)
    # def makeSet(self, vertex):
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
        self.rootNodes.append(node)
        self.nodeCount += 1
        self.setCount += 1
    def find(self, node):
        currentNode = node
        while currentNode.parentNode is not None:
            currentNode = currentNode.parentNode
        root = currentNode
        currentNode = node
        while currentNode is not root:
            # path compression
            temp = currentNode.parentNode
            currentNode.parentNode = root
            currentNode = temp
        return root.nodeId
    def union(self, node1, node2):
            index1 = self.find(node1)
            index2 = self.find(node2)
            if index1 == index2:
                return
            root1 = self.rootNodes[index1]
            root2 = self.rootNodes[index2]
            if root1.height < root2.height:
                root1.parentNode = root2
            elif root1.height > root2.height:
                root2.parentNode = root1
            else:
                root2.parentNode = root1
                root1.height += 1
            self.setCount -= 1
class Algorithm(object):
    def constructSpanningTree(self, vartexList, edgeList):
        disjointSet = DisjointSet(vertexList)
        spanningTree = []
        edgeList.sort()
        for edge in edgeList:
            u = edge.startVertex
            v = edge.targetVertex
            if disjointSet.find(u.parentNode) is not disjointSet.find(v.parentNode):
                spanningTree.append(edge)
                disjointSet.union(u.parentNode, v.parentNode)
        for edge in spanningTree:
            print(edge.startVertex.name, "--" , edge.targetVertex.name)
vertex1 = Vertex("a")
vertex2 = Vertex("b")
vertex3 = Vertex("c")
vertex4 = Vertex("d")
vertex5 = Vertex("e")
vertex6 = Vertex("f")

edge1 = Edge(2, vertex1, vertex2)
edge2 = Edge(4, vertex1, vertex4)
edge3 = Edge(4, vertex2, vertex3)
edge4 = Edge(4, vertex2, vertex4)
edge5 = Edge(3, vertex2, vertex5)
edge6 = Edge(1, vertex2, vertex6)
edge7 = Edge(5, vertex3, vertex6)
edge8 = Edge(2, vertex4, vertex5)
edge9 = Edge(5, vertex5, vertex6)

vertexList = []
vertexList.append(vertex1)
vertexList.append(vertex2)
vertexList.append(vertex3)
vertexList.append(vertex4)
vertexList.append(vertex5)
vertexList.append(vertex6)

edgeList = []
edgeList.append(edge1)
edgeList.append(edge2)
edgeList.append(edge3)
edgeList.append(edge4)
edgeList.append(edge5)
edgeList.append(edge6)
edgeList.append(edge7)
edgeList.append(edge8)
edgeList.append(edge9)

algorithm = Algorithm()
algorithm.constructSpanningTree(vertexList, edgeList)
