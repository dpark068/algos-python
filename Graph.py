class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nrb] = weight

    def __str__(self):
        return "Vertex id is %s" % self.id
    
    def getConnections(self):
        return self.connectedTo.keys()
    
    def getId(self):
        return self.id
    
    def getWeight(self,nbr):
        if nbr in self.connectedTo:
            return self.connectedTo[nbr]
        return None

class Graph:
    def __init__(self):
        self.vertexList = {}
        self.size = 0

    def addVertex(self,key):
        """ Add new vertex into graph """
        vertex = Vertex(key)
        self.size += 1
        self.vertexList[key] = vertex
        return vertex

    def getVertex(self,n):
        """ Check to see if vertex exists """
        if n in self.vertexList:
            return self.vertexList[n]
        return None
    
    def __contains__(self,n):
        """ Check to see if vertex is in graph """
        if n in self.vertexList:
            return True
        return False
    
    def addEdge(self,f,t,weight=0):
        """ Add edge between two vertices f-from, t-to """
        if f not in self.vertexList:
            fromVertex = self.addVertex(f)
        if t not in self.vertexList:
            toVertex = self.addVertex(t)
        
        fromVertex.addNeighbor(toVertex,weight)

    def getVertices(self):
        """ Get all vertices """
        return self.vertexList.keys()

    def __iter__(self):
        """ easy to iterate over all the vertex objects in a particular graph """
        return iter(self.vertList.values())