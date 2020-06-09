""" General DFS --> O(V+E)"""

from pythonds.graphs import Graph
class DFSGraph(Graph):
    def __init__(self):
        super(self).__init__()
        self.time = 0

    def dfs(self):
        """ Iterate over each vertex"""
        
        # set color and pred
        for vertex in self:
            vertex.setColor('white')
            vertex.setPred(-1)
        
        # backtracking
        for vertex in self:
            if vertex.getColor == 'white':
                self.dfsvisit(vertex)
            



    def dfsvisit(self,startVertex):
        """ iterate through depths of node: set color, discoverytime and iterate through its connections """
        startVertex.setColor = 'gray'
        startVertex.setDiscovery(self.time + 1)
        self.time += 1
        nextVertices = startVertex.getConnections()

        for nextVertex in nextVertices:
            if nextVertex.getColor == 'white':
                nextVertex.setPred(startVertex)
                dfsvisit(nextVertex)
        startVertex.setColor('black')
        self.time += 1
        startVertex.setFinish(self.time)