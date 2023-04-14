import heapq


class GraphList:
    # Instanciando Construtor
    def __init__(self, vertice_number:int, directed:bool = False, weighted:bool = False):
        self.vertice_number = vertice_number
        self.adj_list = {i: [] for i in range(vertice_number)}
        self.vertex_names = {}
        self.directed = directed
        self.weighted = weighted

    # Cria o grafo com base em um txt
    @staticmethod
    def load_graph_file(self, txt_graph_path:str):
        with open(txt_graph_path, 'r') as f:
            content = f.read()
            content = content.replace('\n',' ')
            content = content.split(" ")
            vertice_number = int(content[0])
            directed = bool(int(content[2]))
            weighted = bool(int(content[3]))
            graph = GraphList(vertice_number, directed, weighted)

            if weighted:
                for i in range(4, len(content), 3):
                    graph.add_edge(int(content[i])-1,int(content[i+1])-1)
            else:
                for i in range(4, len(content), 3):
                    graph.add_edge(int(content[i])-1,int(content[i+1])-1,int(content[i+2]))
        return graph

    # Adiciona Aresta
    def add_edge(self, u:int, v:int, weight:float = None) -> None:
        if self.weighted:
            self.adj_list[u].append((v, weight))
            if not self.directed:
                self.adj_list[v].append((u, weight))
        else:
            self.adj_list[u].append(v)
            if not self.directed:
                self.adj_list[v].append(u)

    # Remove Aresta
    def remove_edge(self, u:int, v:int) -> None:
        if self.weighted:
            self.adj_list[u] = [(vertex, w) for vertex, w in self.adj_list[u] if vertex != v]
            if not self.directed:
                self.adj_list[v] = [(vertex, w) for vertex, w in self.adj_list[v] if vertex != u]
        else:
            self.adj_list[u].remove(v)
            if not self.directed:
                self.adj_list[v].remove(u)

    # Adiciona vértice
    def add_vertice(self, name:str = None) -> None:
        self.vertice_number += 1
        self.adj_list[self.vertice_number - 1] = []
        if name is not None:
            self.vertex_names[self.vertice_number - 1] = name

    # Remove vértice
    def remove_vertice(self, label:int) -> None:
        del self.adj_list[label]
        self.vertice_number -= 1
        if label in self.vertex_names:
            del self.vertex_names[label]
        for key in self.vertex_names:
            if self.vertex_names[key] > label:
                self.vertex_names[key] -= 1

    # Retorna o índice do vértice
    def get_vertex_index(self, label:str) -> int:
        if label in self.vertex_names.values():
            return list(self.vertex_names.keys())[list(self.vertex_names.values()).index(label)]
        else:
            return -1

    # Retorna vizinhos
    def return_neighbor(self, label:int) -> None:
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
        
    # Busca em largura
    def breadth_first_search(self, start:int, end:int) -> None:
        visited = []
        queue = [start]

        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.append(node)
                print(node)
                if node == end:
                    break

                if self.weighted:
                    neighbors = [edge[0] for edge in graph.adj_list[start]]
                else:
                    neighbors = self.adj_list[start]

                queue.extend(neighbors)

    # Busca em profundidade
    def depth_search(self, start:int, end:int, visited:list[int]=None) -> None:
        if visited is None:
            visited = []

        visited.append(start)
        print(start)
        if start == end:
            return
        
        if self.weighted:
            neighbors = [edge[0] for edge in graph.adj_list[start]]
        else:
            neighbors = self.adj_list[start]
        
        for neighbor in neighbors:
            if neighbor not in visited:
                self.depth_search(neighbor, end, visited)

    # Dijkstra
    def dijkstra(self, start:int) -> dict[int, float]:
        # Inicializa a tabela de distâncias com valores infinitos
        distances = {node: float('inf') for node in graph.adj_list}
        # A distância para o nó inicial é zero
        distances[start] = 0
        # Cria uma fila de prioridade para armazenar os nós a serem processados
        queue = [(0, start)]
        
        while queue:
            # Remove o nó com a menor distância da fila de prioridade
            current_distance, current_node = heapq.heappop(queue)
            # Se a distância atual for maior do que a distância armazenada, pule este nó
            if current_distance > distances[current_node]:
                continue
            # Verifica os vizinhos do nó atual
            for neighbor, weight in self.adj_list[current_node]:
                # Calcula a distância até o vizinho
                distance = current_distance + weight
                # Se a distância for menor do que a armazenada, atualize
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    # Adiciona o vizinho na fila de prioridade
                    heapq.heappush(queue, (distance, neighbor))
    
        return distances

if __name__ == "__main__":

    graph = GraphList(7, directed=True, weighted=True)
    graph.add_edge(0, 1, 2)
    graph.add_edge(0, 3, 5)
    graph.add_edge(1, 2, 1)
    graph.add_edge(1, 4, 1.5)
    graph.add_edge(1, 5, 2.4)
    graph.add_edge(2, 4, 7)
    graph.add_edge(2, 5, 10)
    graph.add_edge(3, 4, 1)
    graph.add_edge(4, 5, 2)
    graph.add_edge(1, 6, 3)
    print(graph,'\n')

    # graph = GraphList(7, directed=True, weighted=False)
    # graph.add_edge(0, 1)
    # graph.add_edge(0, 3)
    # graph.add_edge(1, 2)
    # graph.add_edge(1, 4)
    # graph.add_edge(1, 5)
    # graph.add_edge(2, 4)
    # graph.add_edge(2, 5)
    # graph.add_edge(3, 4)
    # graph.add_edge(4, 5)
    # graph.add_edge(1, 6)
    # print(graph,'\n')

    graph.breadth_first_search(1, 6)
    print("\n")
    graph.depth_search(1, 6)

    print(graph.dijkstra(1))