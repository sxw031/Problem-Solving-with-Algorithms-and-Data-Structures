# consider a problem that online game designers and internet radio providers face:
# This is important in gaming because every players can communicate and listeners can tuned in and getting all the data
# It is a typical boardcast problem

# 1. the boardcast host has some information that the listeners all need to recieve. 
#    (simplest solution)  Define:
#                       - Baordcasting host to keep all information in the list and send individual message to each ---> uncontrolled flooding.
#					   	  How it works? (it generates many more unnecessary messages than our first stragety)
#                       1. Each message starts with a ttl(time to live) value set to some number greater than or equal to the number of edges between boardcast host and its most distant listener
#						2. Each routers get a copy of the message and passes the message on to all of its neighboring routers.
#                       3. When the message is passed on the ttl is decreased. 
#                       4. Each router continues to send copies of the message to all its neighors until the ttl value reaches 0.
#    (Prim's algorithm)   Define: 
#					    - Construct a minimum weight spanning tree solution defined as T for G = (V,E), where T is a subset of E that connects all the vertices in V. The sum of the weights of the edges in T is minimized.
#                         How is works?
#  						- The broadcast host simply sends a single copy of the broadcast message into the network. 
# 						- Each router forwards the message to any neighbor that is part of the spanning tree, excluding the neighbor that just sent it the message. 
#                    

### Develop the Prim's alorithm ###
# It belongs to a family of algorithms called the "greedy algorithm", because at each step we will choose the cheapest next step(lowest weight in this case).

## The basic idea:
# """ While T is not yet a spanning tree
#     Find an edge that is safe to add to the tree
#     Add the new edge to T """

## define a safe edge:
#  any edge that connects a vertex that is in the spanning tree to a vertex that is not in the spanning tree.
#  This ensures that the tree will always remain a tree and therefore have no cycles.

# same to Dijkstra's algorithm, it also use a priority queue to select the next vertex to add to the growing graph.

from pythonds.graphs import PriorityQueue, Graph, Vertex

def prim(G,start):
    pq = PriorityQueue()
    for v in G:
    	# the distance to all the other vertices are initialized to infinity.
        v.setDistance(sys.maxsize)
        v.setPred(None)
    # we begin with the starting vertex as A for example
    start.setDistance(0)
    # we add initially the vertices which are the neighors of A to the priority queue
    pq.buildHeap([(v.getDistance(),v) for v in G])
    while not pq.isEmpty():
    	# look for the smallest distance
        currentVert = pq.delMin()
        # examine its neighbors 
        for nextVert in currentVert.getConnections():
        	# update the new distances
          	newCost = currentVert.getWeight(nextVert)
          	if nextVert in pq and newCost<nextVert.getDistance():
          		# set their predecessor links and new distance values
              	nextVert.setPred(currentVert)
              	nextVert.setDistance(newCost)
              	pq.decreaseKey(nextVert,newCost)

