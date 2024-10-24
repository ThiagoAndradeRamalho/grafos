class Grafo:

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0]*self.vertices for i in range(self.vertices)]

    def adiciona_aresta(self, u, v):
        self.grafo[u-1][v-1] = 1

    def remove_aresta(self, u, v):
        self.grafo[u-1][v-1] = 0

    def checagagem_adjacencia_vertice(self, u, v):
        if self.grafo[u-1][v-1] == 1:
            return True 
        else:
            return False
        
    def chegagem_adjacencia_aresta(self, u1, v1, u2, v2):
        if u1 == u2 or u1 == v2 or v1 == u2 or v1 == v2:
            return True
        else: 
            return False  

    def mostra_matriz(self):
        print('Matriz de Adjacencia')
        for i in range(self.vertices):
            print(self.grafo[i])
            

g = Grafo(4)
g.adiciona_aresta(1,2)
g.adiciona_aresta(3,4)
g.remove_aresta(3,4)
g.mostra_matriz()