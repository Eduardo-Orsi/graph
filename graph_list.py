
class GraphList:
    # Instanciando Construtor
    def __init__(self, vertice_number: int, directed: bool = False, weighted: bool = False):
        self.vertice_number = vertice_number
        self.adj_list = {i: [] for i in range(vertice_number)}
        self.vertex_names = {}
        self.directed = directed
        self.weighted = weighted

    # Adiciona Aresta
    def add_edge(self, u: int, v: int, weight: float = None) -> None:
        if self.weighted:
            self.adj_list[u].append((v, weight))
            if not self.directed:
                self.adj_list[v].append((u, weight))
        else:
            self.adj_list[u].append(v)
            if not self.directed:
                self.adj_list[v].append(u)

    # Remove Aresta
    def remove_edge(self, u: int, v: int) -> None:
        if self.weighted:
            self.adj_list[u] = [(vertex, w) for vertex, w in self.adj_list[u] if vertex != v]
            if not self.directed:
                self.adj_list[v] = [(vertex, w) for vertex, w in self.adj_list[v] if vertex != u]
        else:
            self.adj_list[u].remove(v)
            if not self.directed:
                self.adj_list[v].remove(u)

    # Adiciona vértice
    def add_vertice(self, name: str = None) -> None:
        self.vertice_number += 1
        self.adj_list[self.vertice_number - 1] = []
        if name is not None:
            self.vertex_names[self.vertice_number - 1] = name

    # Remove vértice
    def remove_vertice(self, label: int) -> None:
        del self.adj_list[label]
        self.vertice_number -= 1
        if label in self.vertex_names:
            del self.vertex_names[label]
        for key in self.vertex_names:
            if self.vertex_names[key] > label:
                self.vertex_names[key] -= 1

    # Retorna o índice do vértice
    def get_vertex_index(self, label: str) -> int:
        if label in self.vertex_names.values():
            return list(self.vertex_names.keys())[list(self.vertex_names.values()).index(label)]
        else:
            return -1

    # Retorna vizinhos
    def return_neighbor(self, label: int) -> None:
        if self.weighted:
            return [vertex for vertex, weight in self.adj_list[label]]
        else:
            return self.adj_list[label]

    # Função de print
    def __str__(self) -> str:
        s = ""
        for i in range(self.vertice_number):
            if i not in self.adj_list:
                continue
            if i in self.vertex_names:
                s += str(i) + " (" + self.vertex_names[i] + "): "
            else:
                s += str(i) + ": "
            s += str(self.adj_list[i]) + "\n"
        return s

    # Retorna a existência do aresta
    def has_edge(self, u: int, v: int) -> bool:
        if self.weighted:
            return any([vertex == v for vertex, weight in self.adj_list[u]])
        else:
            return v in self.adj_list[u]
        

if __name__ == "__main__":

    # Testando a classe Graph
    graph = GraphList(6, directed=True, weighted=True)
    graph.add_edge(0, 1, 1.9)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)
    graph.add_edge(1, 4)
    graph.add_edge(2, 4)
    graph.add_edge(2, 5)
    graph.add_edge(3, 4)
    graph.add_edge(4, 5)
    print(graph,'\n')
