### What is Graph?
# Tree is a special kind of graph
# Good examples are paths

### Vocabulary and Definitions
# Vertex or node - It can have a name we called key. The additional informtion of it is "payload"
# Edge or arc - one way or two way to show a relationship between two vertices. 
#               directed graph or digraph: If the edges in a graph are all one-way.
# Weight - the cost to show that there is a cost to go from one vertex to another.
# Path - sequence of vertices that are connected by edges (V3, V4, V0, V1) for example
# Cycle - A cycle in a directed graph that starts and ends at the same vertex. graph without cycle is called acyclic graph.
#         DAG - Direct Acyclic Graph. A direct graph with no cycles.

# A graph can be represented as G = (E,V), where V is a set of vertices and E is a set of edges.
# Each Edge is a tuple(v,w,5), for example from v to w, the weight is 5.

### ADT(Abstract Data Type)
# Graph() creates a new, empty graph.
# addVertex(vert) adds an instance of Vertex to the graph.
# addEdge(fromVert, toVert) Adds a new, directed edge to the graph that connects two vertices.
# addEdge(fromVert, toVert, weight) Adds a new, weighted, directed edge to the graph that connects two vertices.
# getVertex(vertKey) finds the vertex in the graph named vertKey.
# getVertices() returns the list of all vertices in the graph. 
# in returns True for a statement of the form vertex in graph, if the given vertex is in the graph, False otherwise.

### Implementations
# There are two well-known implementations of a graph, the adjecency matrix and the adjecency list.

## 1. An adjecency Matrix
# each of the rows and columns represent a vertex in the graph.
# the value stored in the cell indicates if there is an edge from vertex x to vertex w, the value also can represent the weight.
# When two vertices are connected by an edge, we say that they are adjacent.
# Advantage: simple and easy to see with small graphs. good for when the number of edges is large, in other word, not sparsely connected which is not usually the case.
# Disadvantage: most of the cells are empty.

## 2. An adjecency List (we implement it)
# more efficient way
# a master list of all the vertices in the Graph object
# In each vertex object in the graph, maintains a list of the other vertices that it is conencted to . This we can use Dictionary.

# holds the master list of vertices, which maps vertex names to vertex objects
class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
    	"""make easy to iterate over the vertex objects"""
        return iter(self.vertList.values())

# represent each vertex in the graph
class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {} # keep track of the vertices to which it is connected, and the weight of each edge, this dictionary is called connectedTo

    def addNeighbor(self,nbr,weight=0):
    	"""add a connection from its vertex to another"""
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
    	"""get all the vertices in the adjacency list"""
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

### GRAPH ADT SUMMARY ###
# Breadth first search for finding the unweighted shortest path.
# Dijkstra’s algorithm for weighted shortest path.
# Depth first search for graph exploration.
# Strongly connected components for simplifying a graph.
# Topological sort for ordering tasks.
# Minimum weight spanning trees for broadcasting messages.



