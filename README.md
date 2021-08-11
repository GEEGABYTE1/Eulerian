# Eulerian

Eulerian Path and Cycle Detection Algorithm with implementation of Graph Depth-First Search.

# Eulerian Path 
The Eulerian Path is a path that visits every edge exactly once. There are two conditions that must be true for a graph to be Eulerian:
  - a) All vertices with non-zero degrees are connected. We don't care about vertices that have no edges becase they would be separate from the overall graph.
 -  b) If zero or two vertices have odd degrees and all other vertices have even degrees. Not that only one vertex with an odd degree is not possible in an unidrected graph (sum of all degrees is always even in an undirected graph).
 
*Note: A Graph with no edges is considered Eulerian because there are no edges to traverse*

In an Eulerian path, each time we visit a vertex, we walk through two univisted edges with an end point. Therefore, all middle vertices in the Eulerian Path must have an even degree. In our solution, we did not assume that the middle vertices had an even degree. Rather, we assumed the abolute middle vertex as the vertex with the most edges. The vertex with the most edges means that the vertex is the middle of most vertices, therefore creating paths to each vertex. Therfore, we had understood that the vertex that had the biggest amount of edges has to be traveled at least more than once. 

With the Depth-First Search algorithm, we traverse each path by depth starting from 

# Eulerian Cycle 


# More Information
