class GrafoListaAdjacencia:
    def __init__(self, num_vertices, direcionado = False):
        self.num_vertices = num_vertices
        self.direcionado = direcionado
        self.lista = [[] for _ in range(num_vertices)] # cria uma lista de listas, onde cada lista interna representa os vertices adjacentes a um vertice
            
    def adicionar_aresta(self, u, v):
        max_index = max(u, v)
        while len(self.lista) <= max_index:
            self.lista.append([])  # Adiciona listas vazias para novos vértices

        # Adiciona as conexões u -> v e v -> u
        self.lista[u].append(v)
        self.lista[v].append(u) 
        
    def remover_aresta(self, u, v):
        if v in self.lista[u]: # verifica se v esta na lista de adjacencia de u, se sim remove
            self.lista[u].remove(v)
        if not self.direcionado and u in self.lista[v]: # verifica se u esta na lista de adjacencia de v, se sim remove
            self.lista[v].remove(u)
            print('removido com sucesso')



    def exibir_lista(self):
        for i in range(self.num_vertices):
            print(f"{i}: {self.lista[i]}")