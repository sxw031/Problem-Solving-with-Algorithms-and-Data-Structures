############### Topic 1 - SCC(Strongly Connected Components) ##################
# In web pages, we treat a page as a vertex, and the hepyerlinks on the page as edges connecting one vertex to another.
# SCC - a algorithm that can help find clusters of highly interconnected vertices in a graph.
#       we formally defined C, of a graph G, as the largest subset of vertices C belongs to G such that for every pair of vertices v,w belongs to G we have path from v to w and a path from w to v.
# We can show a simplified view of the graph by combining all the vertices in one strongly connected component into a single larger vertex.
# The transportation of G - all the edges in the graph have been reversed.

## Describe the algorithm to compute the SCC:
# 1. call dfs for graph G to compute the finish times for each vertex.
# 2. comput G(t), the transportation of G.
# 3. call dfs for G(t), but in main loop of DFS explore each vertex in decreasing order of finish time.
# 4. Each tree in the forest computed in step 3 is SCC, output the index for each vertex in each tree in the forest to identify the component.

############### Topic 2 - Shortest Path Problem ##################
# find the path with smallest total weight along which to route any given message.
# 1. when we use a broswer to request a web page from a server, the request must travel over your local area work and out to the internet through a router.
# 2. The request travels over the internet and eventually arrives at a router for the local area network where server is located.
# 3. The web page we requested then travels back through the same routers to get to your broswer.
# traceroute labels all the additional routers inside the "internet", they are working together to get your information from place to place.
# Each router on the internet is connected to one or more other routers. Your information flows through different routers at different times.

### Dijkatra's Algorithm ###
# similiar to BFS, it is a iterative algorithm that provides us with the shortest path from one particular starting node to all other nodes in the graph.
# we use "dist" to track the total cost from the start node to each destination
# dist instance contains the current total weight of the smallest weight path from the start to the vertex in the question.
# dist first created to be a very large number, and that is used to determine the order of the objects in the priority queue.
# The alogrithm iterate once for every vertex, however the order that we iterate over the vertex is controlled a priority queue.

from pythonds.graphs import PriorityQueue, Graph, Vertex
def dijkstra(aGraph,start):
    pq = PriorityQueue()
    start.setDistance(0)
    # initially the new costs to get them through the start node are their direct costs, so we update the costs to each of these nodes.
    # we also set the predecessor for each node to u and add each node to the priority queue.
    # we use the distance as the key for the priority queue.
    pq.buildHeap([(v.getDistance(),v) for v in aGraph])
    # we examine the vertices that are adjacent to x
    while not pq.isEmpty():
        currentVert = pq.delMin()
        for nextVert in currentVert.getConnections():
            newDist = currentVert.getDistance() \
                    + currentVert.getWeight(nextVert)
            if newDist < nextVert.getDistance():
                nextVert.setDistance( newDist )
                nextVert.setPred(currentVert)
                pq.decreaseKey(nextVert,newDist)


### Analysis ###
# building the priority queue take O(V) times since we initially add every vertex in the graph to the priority queue.
# then while loop is executed every vertex since vertices are all added at the beginning and only removed after that 
#      within the loop, we call delMin, takes O(logN) times  ---> while loop give us VlogV times.
# 	   within the loop, the for loop: is executed once for each edge in the graph and within for loop we call decreaseKey takes ElogV
# Therefore combine takes (V+E)LogV
