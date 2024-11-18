class GrafoListaAdjacencia:
    def __init__(self, num_vertices, direcionado = False):
        self.num_vertices = num_vertices
        self.direcionado = direcionado
        self.lista = [[] for _ in range(num_vertices)] # cria uma lista de listas, onde cada lista interna representa os vertices adjacentes a um vertice

            
    def adicionar_aresta(self, u, v):
        self.lista[u].append(v) # adiciona o vertice v a uma lista de adjacencia do vertice u, conexao de u para v
        if not self.direcionado: 
         self.lista[v].append(u) # adiciona o vertice u a uma lista de adjacencia do vertice v, conexao de v para u
        # se for direcionado, é apenas u para v
        
        
    def remover_aresta(self, u, v):
        if v in self.lista[u]: # verifica se v esta na lista de adjacencia de u, se sim remove
            self.lista[u].remove(v)
        if not self.direcionado and u in self.lista[v]: # verifica se u esta na lista de adjacencia de v, se sim remove
            self.lista[v].remove(u)


    def exibir_lista(self):
        for i in range(self.num_vertices):
            print(f"{i}: {self.lista[i]}")
            
            
            
    def duplicar_grafo(self):
    # Cria um novo grafo com o mesmo número de vértices e o mesmo tipo (direcionado ou não)
        novo_grafo = GrafoListaAdjacencia(self.num_vertices, self.direcionado)
        
        # Copia a lista de adjacência do grafo original para o novo grafo
        for u in range(self.num_vertices):
            for v in self.lista[u]:
                novo_grafo.adicionar_aresta(u, v)
        
        return novo_grafo

