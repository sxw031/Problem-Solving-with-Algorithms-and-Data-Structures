### Object
# Find a sequence of moves that allow the knight to visit every square on the board exactly once. The sequences is called "tour".
# The upper bound on the number of possible legal tours for an eight-by-eight chessboard is known as 1.305e35
# we can solve it by:
# 1. Represent the legal moves of a knight on a chessboard as a graph.
# 2. Use a graph algorithm to find a path of length row x columns -1 where every vertex on the graph is visited exactly once.

### Representation
# Each square on the the chessboard can be represented as a node in the graph: node 0 - node 20 and etc.
# Each legal move by the knight can be represented as an edge in the graph

from pythonds.graphs import Graph, Vertex

## PART 1 - build the full graph for the n-by-n board
def knightGraph(bdSize):
    ktGraph = Graph()
    for row in range(bdSize):
       	for col in range(bdSize):
       		# for each square：
           	nodeId = posToNodeId(row,col,bdSize)
           	newPositions = genLegalMoves(row,col,bdSize)
           	# all legal moves are then converted into edges in the graph
           	for e in newPositions:
               	nid = posToNodeId(e[0],e[1],bdSize)
               	ktGraph.addEdge(nodeId,nid)
    return ktGraph

# heler function that converts a location on the board in terms of a row and a column into a linear vertex number similiar to the vertex numbers
def posToNodeId(row, column, board_size):
    return (row * board_size) + column

# create a list of legal moves for that position on the board.
def genLegalMoves(x,y,bdSize):
    newMoves = []
    # 8 possible moves
    moveOffsets = [(-1,-2),(-1,2),(-2,-1),(-2,1),
                   ( 1,-2),( 1,2),( 2,-1),( 2,1)]
    for i in moveOffsets:
        newX = x + i[0]
        newY = y + i[1]
        # make sure that a particular move that is generated is still on the board.
        if legalCoord(newX,bdSize) and \
                        legalCoord(newY,bdSize):
            newMoves.append((newX,newY))
    return newMoves

def legalCoord(x,bdSize):
    if x >= 0 and x < bdSize:
        return True
    else:
        return False


## PART II. DFS - 2 ways
############################### The first way ###########################
# this is a special case of a DFS where the goal is to create the deepest depth first tree, without any branching
# when the depth first search algorithm finds a dead end(a place in the graph where there are no more moves possible), 
# it backs up the tree to the next deepest vertex that allows it to make legal move.
# directly solve the problem by explicitly forbidding a node to be visited more than once.

# n - the current depth in the search tree
# path - a list of vertices visited up to this point
# u - the vertex in the graph we wish to explore
# limit - the number of nodes in the path
# This is a recursive function.
# DFS also uses color to keep track of which vertices in the graph have been visited.
# white - unvisited
# gray - visited
# dead end reaches with a return tatus of False.
def knightTour(n,path,u,limit):
        u.setColor('gray')
        path.append(u)
        if n < limit:
            nbrList = list(u.getConnections()) # replace .getConnection() to orderByAvail to apply the speed-up heuristic
            i = 0
            done = False
            while i < len(nbrList) and not done:
                if nbrList[i].getColor() == 'white':
                    done = knightTour(n+1, path, nbrList[i], limit)
                i = i + 1
            if not done:  # prepare to backtrack
                path.pop()
                u.setColor('white')
        else: # base case, if we have a path that contains 64 vertices
            done = True
        return done

### Analysis - The first way
# The performance is O(k^N), where N is the number of squares on the chess board and k is a small constant,
# because on each nodes( on each level of tree), depends on the position of the knight, we can have two legal moves at the corners or three on the squares ajacent to the corners or eight at the middle of the board.
# So the branching factor is variable. 
## Heurisitc ##
# It is the way to speed up the 8-by-8 casees so that it runs in under one second.
# at line 104, using the vertex with the most availiable moves as your next vertex on the path is that it tends to have the knight visit the middle squares early on the tour.
#              When this happens it is easy for the knight to get stranded on one side of the board where it cannot reach unvisited suqares on the other side of the board.
# On the other hand, visiting the squares with the fewest availiable moves first pushes the knight to visit the squares around the edges of the board first.
#                    this ensures that the knight will visit the hard-to-reach corners early and can use the middle squares to hop cross the board only when neccessary.

def orderByAvail(n):
    resList = []
    for v in n.getConnections():
        if v.getColor() == 'white':
            c = 0
            for w in v.getConnections():
                if w.getColor() == 'white':
                    c = c + 1
            resList.append((c,v))
    resList.sort(key=lambda x: x[0]) # the critical line, this ensures that we select the vertex to get next that has the fewest availiable moves
    return [y[1] for y in resList]


############################### The second way ###########################
# The more general DFS is actually easier. 
# Its goal is to seach as deeply as possible, connecting as many nodes in the graph as possible and branching where necessary.
# depth first forest - when DSF creates more than one tree.
# DSF make use of predecessor links to construct the tree.
# two new instance variables: discovery and finish times. where discovery time trakcs the number of steps in the algorithm before a vertex is first encounted; the finish time is the number of stpes in the algorithm before a vertax is colored black.

class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0

    # dfs and dfsvisit keep track of the time across calls dfsvisit
    def dfs(self):
    	# self here is a instance of the DFSGraph
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(-1)
        for aVertex in self:
            if aVertex.getColor() == 'white':
                self.dfsvisit(aVertex)

    # starts with a single vertex called startVetex and explores all the neighboring white vertices as deeply as possible
    def dfsvisit(self,startVertex):
        startVertex.setColor('gray')
        self.time += 1
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                self.dfsvisit(nextVertex) # it calls itself recursively to continue the search at a deeper level.
                						  # it is the difference from bfs, whereas bfs addes the node to queue for later exploration
                						  # it is interesting bfs use queue, dfsvisit use stack.
        startVertex.setColor('black')
        self.time += 1
        startVertex.setFinish(self.time)

## Analysis - the second more general case
# The loops in dfs run in O(V), not counting what happens in dfsvisit, since they are executed once for each vertex in the graph.
# In dfsvisit, the loop is executed once for each edge in the adjacency list of the current vertex. 
#              Since dfsvisit is only called recursively if the vertex is white, the loop will execute a maximum of once for every edge in the graph or O(E)
# Therefore the toal time for DFS is O(V+E)

### Extra - Topological Sorting
# It takes a directed acyclic graph and produces a linear ordering of all its vertices such that,
#    if the Graph contains a edge(v,w) then the vertex v comes before the vertex w in the ordering.
# It helps in many applications include software project scheduling, precedence charts...




