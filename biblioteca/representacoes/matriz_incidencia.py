
class GrafoMatrizIncidencia:
    def __init__(self, num_vertices, num_arestas, direcionado=False):
        self.num_vertices = num_vertices
        self.num_arestas = num_arestas
        self.direcionado = direcionado
        self.matriz = [[0] * num_arestas for _ in range(num_vertices)] # cria matriz de incidencia com num_vertices linha e num_arestas colunas
            
            
    def adicionar_aresta(self, u, v, e):
        if e < 0 or e >= self.num_arestas:
            print(f"Erro: índice de aresta fora do limite (permitido: 0 a {self.num_arestas - 1}).")
            return

        self.matriz[u][e] = 1  # Aresta de u
        if self.direcionado:
            self.matriz[v][e] = -1  # Aresta direcionada para v
        else:
            self.matriz[v][e] = 1  # Aresta não direcionada

        
    def obter_extremidades(self, e, direcionado=False): # retornar os vertices conectados pela aresta e
        vertices = []
        for i in range(self.num_vertices): # itera todos os vertices
            if self.matriz[i][e] == 1: # verifica se o vertice i é o ponto de origem de e
                vertices.append(i)
            elif not direcionado and self.matriz[i][e] == -1:
                vertices.append(i)
        return tuple(vertices) if len(vertices) == 2 else (None, None)

    def mostrar_arestas_ocupadas(self):
        print("Arestas ocupadas:")
        for e in range(self.num_arestas):
            u, v = self.obter_extremidades(e) # encontrar vertices conectados
            if u is not None and v is not None:
                print(f"Índice {e}: Aresta entre {u} e {v}")
                
        
    def remover_aresta(self, e):
        if e >= self.num_arestas or e < 0:
            print("Erro: índice de aresta fora do limite.")
            return
    
        for i in range(self.num_vertices): # itera sobre todos os vertices
            self.matriz[i][e] = 0 # remove a aresta 
        
    
    def exibir_matriz(self):
        for linha in self.matriz:
            print(" ".join(map(str, linha)))
            
            
            