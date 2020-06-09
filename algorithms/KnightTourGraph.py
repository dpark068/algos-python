""" Knights Tour algo is O(k^n), k = small constant, n = # of squares of chessboard 
How can we increase speed?
"""
from pythonds.graphs import Graph

def knightGraph(bdSize):
    """ create graph and all the vertices(spots on board) and edges(legal moves)"""
    g = Graph()

    for row in range(bdSize):
        for col in range(bdSize):
            # for each cell figure out its possible next moves and create edges
            pos = posToNodeId(row,col,bdSize)
            moves = genLegalMoves(row,col,bdSize)
            for move in moves:
                movePos = posToNodeId(move[0],move[1],bdSize)
                g.addEdge(pos,movePos)
    return g        

def posToNodeId(row, col, board_size):
    """ Unique id for each cell """
    return (row * bdSize) + col

def genLegalMoves(x,y,bdSize):
    """ What are the potential moves """

    offsets = [(-2,1),(-2,-1),(2,1),(2,-1), \
    (-1,2),(-1,-2),(1,-2),(1,2)]

    legalMoves = []
    for offset in offsets:
        newX = x + offset[0]
        newY = y + offset[1]
        if legalCoord(newX,bdSize) and legalCoord(newY, bdSize):
            legalMoves.append((newX,newY))
    
    return legalMoves

def legalCoord(x,bdSize):
    """ Determine if a move is legal by checking bounds of board """
    if x >= 0 and x < bdSize:
        return True
    else:
        return False

def knightTour(n,path,u,limit):
    """ DFS algorithm to search all paths - will iterate to all its connections
    n - depth of tree, path - current path taken, u - current node, limit - targets bound (64)
    """

    u.setColor('gray')
    path.append(u)
    if n < limit:
        done = False
        for connect in u.getConnections():
            if connect.getColor() == 'white':
                done = knightTour(n+1,path,connect,limit)
        if not done:
            path.pop()
            u.setColor('white')
    else:
        done = True
    return done