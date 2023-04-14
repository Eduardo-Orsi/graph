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
    def load_graph_file(txt_graph_path:str):
        with open(txt_graph_path, 'r') as f:
            content = f.read()
            content = content.replace('\n',' ')
            content = content.split(" ")
            vertice_number = int(content[0])
            directed = bool(int(content[2]))
            weighted = bool(int(content[3]))
            graph = GraphList(vertice_number, directed, weighted)

            if not weighted:
                for i in range(4, len(content), 3):
                    graph.add_edge(int(content[i]),int(content[i+1]))
            else:
                for i in range(4, len(content), 3):
                    graph.add_edge(int(content[i]),int(content[i+1]),float(content[i+2]))
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
        distances = {node: float('inf') for node in graph.adj_list}
        distances[start] = 0
        queue = [(0, start)]
        
        while queue:
            current_distance, current_node = heapq.heappop(queue)
            if current_distance > distances[current_node]:
                continue
            
            for neighbor, weight in self.adj_list[current_node]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(queue, (distance, neighbor))

        print(distances)
        return distances

if __name__ == "__main__":

    graph = GraphList.load_graph_file("espacoaereo.txt")
    print(graph)
    graph.dijkstra(1)
    graph.depth_search(2, 1)
