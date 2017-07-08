### Description
# In a word ladder puzzle, you must make the change occur gradually by changing one letter at a time.
# At each step you must transfer one word into another word., you are not allowed to transform a word into a non-word.

### Approach - PART 1
# Suppose that we have a huge number of buckets, each of them with a four-letter word on the outside, except that one of the letters in the label has been replaced by an underscore.
# As we process each word in our list we compare the word with each bucket, using the "_" as a wildcard
# Every time we find a matching bucket, we put our word in that bucket.
# Once we have all the words in the appropriate buckets we know that all the words in the bucket must be connected.
# we can use dictionary to describe it; labels on the buckets are the keys; the values stored for that key is a list of words.
# Once we have the dictionary built we can create the graph. We start our graph by creating a vertex for each word in the graph. Then we create edges between all the vertices we find for words found under the same key in the dictionary.

from pythonds.graphs import Graph

def buildGraph(wordFile):
    d = {}
    g = Graph()
    wfile = open(wordFile,'r')
    # create buckets of words that differ by one letter
    for line in wfile:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    # add vertices and edges for words in the same bucket
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1,word2)
    return g

### PART II - find the shortest solution， using Breadth First Search(BFS, easiest)
# it finds all the vertices that are a distance k from s before it finds any vertices that are a distance k+1.
# A white vertex is an undiscovered vertex; initially discovered ---> gray; when BFS has completely explored a vertex is colored black.
# If it is white, the vertex is unexplored, and four things happen:
#    a). The new, unexplored vertex nbr, is colored gray.
#    b). The predecessor of nbr is set to the current node currentVert
#    c). The distance to nbr is set to the distance to currentVert + 1
#    d). nbr is added to the end of a queue. Adding nbr to the end of the queue effectively schedules this node for further exploration, but not until all the other vertices on the adjacency list of currentVert have been explored.

from pythonds.graphs import Graph, Vertex
from pythonds.basic import Queue

def bfs(g,start):
  start.setDistance(0)
  start.setPred(None)
  vertQueue = Queue()
  vertQueue.enqueue(start)
  while (vertQueue.size() > 0):
    currentVert = vertQueue.dequeue()
    for nbr in currentVert.getConnections():
      if (nbr.getColor() == 'white'):
        nbr.setColor('gray')
        nbr.setDistance(currentVert.getDistance() + 1)
        nbr.setPred(currentVert)
        vertQueue.enqueue(nbr)
    currentVert.setColor('black')

def traverse(y):
    x = y
    while (x.getPred()):
        print(x.getId())
        x = x.getPred()
    print(x.getId())

traverse(g.getVertex('sage'))

### Analysis
# 1. while loop, at most, one time for each vertex in the graph V
# 2. for loop, which is nested inside the while loop at most once for each edge in the graph. E
# Therefore searching takes O(V+E)
