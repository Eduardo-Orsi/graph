import heapq
import time


class GraphList:
    # Instanciando Construtor
    def __init__(self, vertice_number:int, directed:bool = False, weighted:bool = False):
        self.vertice_number = vertice_number
        self.adj_list = {i: [] for i in range(vertice_number)}
        self.vertex_names = {}
        self.directed = directed
        self.weighted = weighted
        self.degree_list = None

    # Cria o grafo com base em um txt
    @staticmethod
    def load_graph_file(txt_graph_path:str):
        with open(txt_graph_path, 'r') as f:
            content = f.readlines()
            for line in range(len(content)):
                content[line] = content[line].replace('\n','')
            
            content[0] = content[0].split(' ')
            vertice_number = int(content[0][0])
            directed = bool(int(content[0][2]))
            weighted = bool(int(content[0][3]))

            graph = GraphList(vertice_number, directed, weighted)
            content.pop(0)

            if not weighted:
                for i in content:
                    i = i.split(' ')
                    graph.add_edge(int(i[0]),int(i[1]))
            else:
                for i in content:
                    i = i.split(' ')
                    graph.add_edge(int(i[0]),int(i[1]),float(i[2]))
        return graph

    # Adiciona Aresta
    def add_edge(self, u:int, v:int, weight:float = None) -> None:
        if self.weighted:
            self.adj_list[u].append((v, float(weight)))
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

    # Retorna a existência da aresta
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
            return True

        if self.weighted:
            neighbors = [edge[0] for edge in graph.adj_list[start]]
        else:
            neighbors = self.adj_list[start]
        
        for neighbor in neighbors:
            if neighbor not in visited:
                if self.depth_search(neighbor, end, visited):
                    return True
        return
        
    # Dijkstra
    def dijkstra(self, start:int) -> dict[int, float]:
        distances_dict = {node: float('inf') for node in graph.adj_list}
        distances_dict[start] = 0
        queue = [(0, start)]
        
        while queue:
            current_distance, current_node = heapq.heappop(queue)
            if current_distance > distances_dict[current_node]:
                continue
            
            for neighbor, weight in self.adj_list[current_node]:
                distance = current_distance + weight
                if distance < distances_dict[neighbor]:
                    distances_dict[neighbor] = distance
                    heapq.heappush(queue, (distance, neighbor))

        print(distances_dict)
        return distances_dict
    
    def is_planar(self) -> bool:

        if self.vertice_number < 5:
            return True

        if self.weighted:
            for node in self.adj_list: #i
                for node_neighbor in self.adj_list[node]: #j
                    for neighbor_neighbor in self.adj_list[node_neighbor[0]]:
                        if neighbor_neighbor == node:
                            return True
            return False
        
        for node in self.adj_list: #i
            for node_neighbor in self.adj_list[node]: #j
                for neighbor_neighbor in self.adj_list[node_neighbor]:
                    if neighbor_neighbor == node:
                        return True
                    
        return False

    def welsh_powell(self):
        colors = {node: None for node in self.degree_list}
        color_count = 0

        for vertex in self.degree_list:
            if colors[vertex] == None:
                while any([colors[neighbor] == color_count for neighbor in self.return_neighbor(vertex)]):
                    color_count += 1
                colors[vertex] = color_count
            color_count = 0

        return colors
    
    def dsatur(self):
        # Inicialização
        uncolored_vertices = list(range(self.vertice_number))
        max_degree = max(len(self.adj_list[vertex]) for vertex in uncolored_vertices)
        max_saturation = 0
        colors = {}
        
        # Enquanto houver vértices não coloridos
        while uncolored_vertices:
            # Seleciona o vértice com o maior grau de saturação ou, em caso de empate, com o maior grau
            selected_vertex = max(uncolored_vertices, key=lambda v: (colors[v] if v in colors else -1, -len(self.adj_list[v])))
            
            # Atribui a cor disponível que minimize a saturação
            available_colors = set(range(max_degree + 1))
            for neighbor in self.adj_list[selected_vertex]:
                if neighbor in colors:
                    available_colors.discard(colors[neighbor])
            
            colors[selected_vertex] = min(available_colors)
            uncolored_vertices.remove(selected_vertex)
            
            # Atualiza a saturação dos vizinhos
            for neighbor in self.adj_list[selected_vertex]:
                if neighbor not in colors:
                    colors[neighbor] = colors[neighbor] + 1 if neighbor in colors else 1
                    max_saturation = max(max_saturation, colors[neighbor])
        
        return colors

    def get_degree_list(self) -> None:
        self.degree_list = [[node, len(self.adj_list[node])] for node in self.adj_list]
    
    def sort_degree_list(self) -> None:
        if not self.degree_list:
            return None
        self.degree_list.sort(key=lambda x: x[1], reverse=True)
        self.degree_list = [node[0] for node in self.degree_list]

def print_color_map(colors: dict[int, int]) -> None:
    for key, value in colors.items():
        print(f"{key}|{value}")

if __name__ == "__main__":

    graph = GraphList.load_graph_file("graphs_txt/k5.txt")
    print(graph)
    graph.get_degree_list()
    graph.sort_degree_list()

    initial_time = time.time()
    colors_dsatur = graph.is_planar()
    print(f"Tempo de Execução Planaridade: {time.time() - initial_time}")

    initial_time = time.time()
    color_welsh_powell = graph.welsh_powell()
    print(color_welsh_powell)
    print(f"Tempo de Execução Welsh Powell: {time.time() - initial_time}")
    print(f"Número de cores: {max(color_welsh_powell)}")

    print('\n')

    initial_time = time.time()
    colors_dsatur = graph.dsatur()
    print(colors_dsatur)
    print(f"Tempo de Execução DSATUR: {time.time() - initial_time}")
    print(f"Número de cores: {max(colors_dsatur)}")