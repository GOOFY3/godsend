import sys;

class Vertex(object):
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.adjacentList = []
        self.predecessor = None
        self.minDistance = sys.maxsize
    def __cmp__(self, otherVertex):
        return __cmp__(self.minDistance, otherVertex.minDistance);
    def __lt__(self, otherVertex):
        selfPriority = self.minDistance
        otherPriority = otherVertex.minDistance
        return selfPriority < otherPriority
class Edge(object):
    def __init__(self, startVertex, targetVertex, weight):
        self.weight = weight
        self.startVertex = startVertex
        self.targetVertex = targetVertex
    def calculateShortestPath(self, vertexList, targetVertex):
        queue = [];
        startVertex.minDistance = 0
        heapq.heappush(startVertex)
        while len(queue) > 0:
            actualVertex = heapq.heappop(queue);
            for edge in actualVertex.adjacentList:
                u = actualVertex.startVertex
                v = actualVertex.targetVertex
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
