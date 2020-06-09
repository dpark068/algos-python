#import Graph from Graph
from pythonds.graphs import Graph, Vertex #dpc
from pythonds.basic import Queue



def buildGraph(wordFile):
    d = {}
    g= Graph()
    wfile = open(wordFile, 'r')

    for line in wfile:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    
    # add vertices and edges to graph
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1,word2)
    
    return g

def bfs(g,start):
    """ breadth first algo will look at each node at a level before pursing other child nodes"""
    # Color Predecessor distance
    start.setDistance(0)
    start.setColor('white')
    start.setPred(None)
    vertexQueue = Queue
    vertexQueue.enqueue(start)

    while len(vertexQueue) > 0:
        currVertex = vertexQueue.dequeue()
        for i in currVertex.getConnections():
            if i.getColor == 'white':
                i.setColor('gray')
                i.setDistance(currVertex.getDistance() + 1)
                i.setPred(currVertex)
                vertexQueue.enqueue(i)
        currVertex.setColor('black')

    
    
def traverse(y):
    x = y
    while x.getPred():
        print(x.getId())
        x = x.getPred()
    print(x.getId())

#traverse(g.getVertex('sage'))