# Eulerian ℇ

Eulerian Path and Cycle Detection Algorithm with implementation of Graph Depth-First Search.

# Eulerian Path ⤴️
The Eulerian Path is a path that visits every edge exactly once. There are two conditions that must be true for a graph to be Eulerian:
  - a) All vertices with non-zero degrees are connected. We don't care about vertices that have no edges becase they would be separate from the overall graph.
 -  b) If zero or two vertices have odd degrees and all other vertices have even degrees (check `More Information` to see the definitions of both *even* and *odd* degrees of a vertex). Not that only one vertex with an odd degree is not possible in an unidrected graph (sum of all degrees is always even in an undirected graph).
 
*Note: A Graph with no edges is considered Eulerian because there are no edges to traverse*

In an Eulerian path, each time we visit a vertex, we walk through two univisted edges with an end point. Therefore, all middle vertices in the Eulerian Path must have an even degree. In our solution, we did not assume that the middle vertices had an even degree. Rather, we assumed the abolute middle vertex as the vertex with the most edges. The vertex with the most edges means that the vertex is the middle of most vertices, therefore creating paths to each vertex. Therfore, we had understood that the vertex that had the biggest amount of edges has to be traveled at least more than once. 

With the Depth-First Search algorithm, we traverse each path by depth starting from each vertex. Each vertex can only be visited once, however, the vertex with the most edges can be visited multiple times to allow the full traversal of the graph as some vertices may not lead to other vertices on the opposite side of the graph. With backtracking, we make sure that the if the current vertex is the same as the biggest vertex, we can add it to the path, else, we will leave the vertex and continue to the next one. The recursion happens for each vertex and for each edge, and to make sure we don't land on the same edge again, we backtrack and keep track of the previous vertex. 

At the end, to really see the eulerian paths, we only see the ones that have the biggest vertex as the root vertex. With the biggest vertex, the depth-first search can go through every single edge without tracing back as it has multiple edges to more than 10% of the graph. 

# Eulerian Cycle 🔄

The Eulerian Cycle is sort of the same as the Eulerian Path, however, just has some additional edge cases. The Eulerian Cycle or Graph can be described as, "Is it possible to draw the graph without lifiting your pencil or pen"? In other words, an Eulerian Cycle is an Eulerian Path, which starts and ends on the same vertex. Similar to the Eulerian Path, there are two conditions that must be true:
 - a) same as condition (a) for Eulerian Path 
 - b) All vertices have even degree

For the Eulerian Cycle, and vertex can be the middle vertex. Therefore all vertices by definition must have an even degree. However, the Euerian Cycle is just an extended definition of the Eulerian Path. The last vertex must lead to an unvisited edge that leads to the first vertex. With Depth-First Search, the last vertex will always have unvisited edges until it has been traversed. We know this because the DFS algorithm keeps track of the vertices that have been visited. If the last vertex is the only vertex in the graph that has not been visited, then it's edges should be assumed that they are the only non-visited ones left. However, only one edge leads to the start vertex. Therefore, by traversing the each edge one-by-one with the DFS alg, and getting our Eulerian Paths because a graph with an Eulerian Path is considered *Semi-Eulerian*, we can compare if the last vertex has an edge that leads to the start vertex. If it does, it is considered to be Eulerian.


# More Information 📊

All graphs for the test cases are undirected.

Additional helper functions were created to help keep track of eulerian paths and vertices. 

The inputs are clustered together. Therefore, the algorithm can compute multiple graphs at once with iteration.

*Odd Degree*: If the sum of no. of edges of a vertex is an odd number, the vertex is said to have an odd degree.

*Even Degree*: If the sum of no. of edges of a vertex is an even number, the vertex is said to have an even degree.

Time Complexity of Search (raw algorithm; without formatting the vertices and edges): `O(no. vertices + no.edges)`

`inputs.py` are the test cases.
`graph.py` is the underlying graph data structure needed for this algorithm.
`dfs.py` is the Depth-First-Traversal Algorithm Implementation

Made in Python 🐍
