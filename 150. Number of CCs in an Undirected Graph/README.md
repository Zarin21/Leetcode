150. Number of Connected Components in Undirected Graph

There is an undirected graph with n nodes. There is also an edges array, where edges[i] = [a, b] means that there is an edge between node a and node b in the graph.

The nodes are numbered from 0 to n - 1.

Return the total number of connected components in that graph

Approach:
UNION FIND
1. Making a list of parents with itself as parents first
2. Making a list of rank where rank represent the number of members/children the node has including itself
3. Find(): finds the parent of the node
4. Union(): combines 2 nodes of the lower ranked parent
5. Keeps decrementing result as the number of Unions
6. res is the number of CCs

DFS
1. Adj List
2. DFS
