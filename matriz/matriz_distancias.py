class Grafo:

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0]*self.vertices for i in range(self.vertices)]

    def adiciona_aresta(self, u, v, peso):
        self.grafo[u-1][v-1] = peso

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
        
    def contagem_arestas(self):
        contador = 0
        for i in range(self.vertices):
            for j in range(self.vertices):
                if self.grafo[i][j]!= 0:
                    contador += 1
        print(contador)
        return contador

    def mostra_matriz(self):
        print('Matriz de Adjacencia')
        for i in range(self.vertices):
            print(self.grafo[i])

v = int(input('Digite a quantidade de vertices'))
g = Grafo(v)

a = int(input('Digite a quantidade de arestas'))
for i in range(a):
    u = int(input('De qual vertice parte esta aresta'))
    v = int(input('Para qual vertice chega esta aresta'))
    p = int(input('Qual o peso dessa aresta'))
    g.adiciona_aresta(u,v,p)


g.contagem_arestas()
g.mostra_matriz()