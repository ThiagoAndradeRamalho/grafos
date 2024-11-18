class GrafoListaAdjacencia:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.lista = [[] for _ in range(num_vertices)] # cria uma lista de listas, onde cada lista interna representa os vertices adjacentes a um vertice
        self.t = 0
            
    def adicionar_aresta(self, u, v):
        self.lista[u].append(v) # adiciona o vertice v a uma lista de adjacencia do vertice u, conexao de u para v
        self.lista[v].append(u) # adiciona o vertice u a uma lista de adjacencia do vertice v, conexao de v para u
        # se for direcionado, é apenas u para v
        
        
    def remover_aresta(self, u, v):
        if v in self.lista[u]: # verifica se v esta na lista de adjacencia de u, se sim remove
            self.lista[u].remove(v)
        if u in self.lista[v]: # verifica se u esta na lista de adjacencia de v, se sim remove
            self.lista[v].remove(u)



    def exibir_lista(self):
        for i in range(self.num_vertices):
            print(f"{i}: {self.lista[i]}")