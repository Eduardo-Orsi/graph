
class GraphMat:
    # Instanciando Construtor
    def __init__(self, vertice_number: int, directed: bool = False, weighted: bool = False):
        self.vertice_number = vertice_number
        self.adj_matrix = [[0] * vertice_number for _ in range(vertice_number)]
        self.vertex_names = {}
        self.directed = directed
        self.weighted = weighted
        self.weights = [[float('inf')] * vertice_number for _ in range(vertice_number)] if weighted else None

    # Adiciona Aresta
    def add_edge(self, line: int, column: int, weight: float = None) -> None:
        if self.weighted:
            self.weights[line][column] = weight
            if not self.directed:
                self.weights[column][line] = weight
            self.adj_matrix[line][column] = 1
        if not self.directed:
            self.adj_matrix[column][line] = 1

    # Remove Vértice
    def remove_edge(self, line: int, column: int) -> None:
        self.adj_matrix[line][column] = 0
        if not self.directed:
            self.adj_matrix[column][line] = 0
        if self.weighted:
            self.weights[line][column] = float('inf')
            if not self.directed:
                self.weights[column][line] = float('inf')
    
    # Adiciona vértice
    def add_vertice(self, name:str = None) -> None:
        self.vertice_number += 1
        for line in self.adj_matrix:
            line.append(0)
        self.adj_matrix.append([0] * self.vertice_number)
        if name is not None:
            self.vertex_names[self.vertice_number - 1] = name

    # Remove coluna
    def remove_column(self, label:int):
        self.adj_matrix.pop(label)
        for row in self.adj_matrix:
            row.pop(label)
        self.vertice_number -= 1
        if label in self.vertex_names:
            del self.vertex_names[label]
        for key in self.vertex_names:
            if self.vertex_names[key] > label:
                self.vertex_names[key] -= 1

    # Pega o índice do vértice
    def get_vertex_index(self, label:str) -> int:
        if label in self.vertex_names.values():
            return list(self.vertex_names.keys())[list(self.vertex_names.values()).index(label)]
        else:
            return -1

    # Retorna vizinhos
    def return_neighbor(self,label:int):
        neighbor = []
        for i in range(len(self.adj_matrix[label])):
            if self.adj_matrix[label][i] == 1:
                neighbor.append(i)
        return neighbor

    # Função de print
    def __str__(self) -> str:
        s = ""
        for i in range(self.vertice_number):
            if i in self.vertex_names:
                s += str(i) + " (" + self.vertex_names[i] + "): "
            else:
                s += str(i) + ": "
            for j in range(self.vertice_number):
                s += str(self.adj_matrix[i][j]) + " "
            s += "\n"
        return s
    
    # Retorna a existência do aresta
    def has_edge(self, u:int, v:int) -> bool:
        return self.adj_matrix[u][v] == 1


if __name__ == "__main__":

    # Testando a classe Graph
    graph = GraphMat(6, directed=True, weighted=True)

    graph.add_edge(0, 1)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)
    graph.add_edge(1, 4)
    graph.add_edge(2, 4)
    graph.add_edge(2, 5)
    graph.add_edge(3, 4)
    graph.add_edge(4, 5)
    print(graph,'\n')

    print(f"Tem aresta: {graph.has_edge(1, 2)} \n")

    print(f"Vizinho: {graph.return_neighbor(2)}\n")

    graph.remove_edge(0, 1)
    print("Grafo depois de remover aresta")
    print(graph,'\n')

    print("Grafo depois de remover vertice")
    graph.remove_column(2)
    print(graph,'\n')