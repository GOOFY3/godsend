import sys
import heapq

class Vertex(object):
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.adjacentList = []
        self.predecessor = None
        self.minDistance = sys.maxsize
    # # def __cmp__(self, otherVertex):
    # #     return cmp(self.minDistance, otherVertex.minDistance);
    # def __lt__(self, otherVertex):
    #     selfPriority = self.minDistance
    #     otherPriority = otherVertex.minDistance
    #     return selfPriority < otherPriority
class Edge(object):
    def __init__(self, weight, startVertex, targetVertex):
        self.weight = weight
        self.startVertex = startVertex
        self.targetVertex = targetVertex
class Algorithm(object):
    def calculateShortestPath(self, vertexList, startVertex):
        queue = [];
        startVertex.minDistance = 0
        heapq.heappush(queue, startVertex)
        while len(queue) > 0:
            actualVertex = heapq.heappop(queue);
            for edge in actualVertex.adjacentList:
                u = edge.startVertex
                v = edge.targetVertex
                newDistance = u.minDistance + edge.weight
                if newDistance < v.minDistance:
                    v.minDistance = newDistance
                    v.predecessor = u
                    heapq.heappush(queue, v)
    def getShortestPathTo(self, targetVertex):
        print("shortest path to target is: ", targetVertex.minDistance)
        node = targetVertex
        while node is not None:
            print("%s -->" %node.name)
            node = node.predecessor
node1 = Vertex("A")
node2 = Vertex("B")
node3 = Vertex("C")

edge1 = Edge(1,node1, node2)
edge2 = Edge(1,node2, node3)
edge3 = Edge(0.3, node1, node3)

node1.adjacentList.append(edge1)
node1.adjacentList.append(edge2)
node2.adjacentList.append(edge3)


vertexList = {node1, node2, node3}
algorithm = Algorithm();
algorithm.calculateShortestPath(vertexList, node1)
algorithm.getShortestPathTo(node3)
