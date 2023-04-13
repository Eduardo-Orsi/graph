# GraphList Readme
The GraphList class is a Python implementation of a graph using an adjacency list. This class allows for the creation of an undirected or directed, weighted or unweighted graph, and provides several methods for manipulating the graph, including adding and removing edges and vertices, searching for edges, getting the index of a vertex, and returning the neighbors of a vertex.

# Class Methods:
__init__(self, vertice_number: int, directed: bool = False, weighted: bool = False) -> None
This method initializes a GraphList object with the given number of vertices, and sets the graph to either directed or undirected and weighted or unweighted based on the provided arguments.

add_edge(self, u: int, v: int, weight: float = None) -> None
This method adds an edge between vertices u and v with an optional weight.

remove_edge(self, u: int, v: int) -> None
This method removes the edge between vertices u and v.

add_vertice(self, name: str = None) -> None
This method adds a vertex to the graph with an optional name.

remove_vertice(self, label: int) -> None
This method removes the vertex with the specified label from the graph.

get_vertex_index(self, label: str) -> int
This method returns the index of the vertex with the given name.

return_neighbor(self, label: int) -> None
This method returns a list of the neighbors of the vertex with the given label.

__str__(self) -> str
This method returns a string representation of the graph.

has_edge(self, u: int, v: int) -> bool
This method returns True if there is an edge between vertices u and v, and False otherwise.

breadth_first_search(self, start, end)
This method implements a breadth-first search algorithm on the graph starting from vertex start and ending at vertex end. It prints the visited vertices along the way.

# Example Usage:

graph = GraphList(7, directed=True, weighted=False)
graph.add_edge(0, 1)
graph.add_edge(0, 3)
graph.add_edge(1, 2)
graph.add_edge(1, 4)
graph.add_edge(1, 5)
graph.add_edge(2, 4)
graph.add_edge(2, 5)
graph.add_edge(3, 4)
graph.add_edge(4, 5)
graph.add_edge(1, 6)

print(graph)
Output:
0: [1, 3]
1: [2, 4, 5, 6]
2: [4, 5]
3: [4]
4: [5]
5: []
6: []

graph.breadth_first_search(1, 4)
Output:
1
2
4
