class Grafo:

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[] for i in range(self.vertices)]

    def adiciona_aresta(self, u, v):
        self.grafo[u-1].append(v)

    def mostrar_lista(self, u, v):
            for i in range(self.vertices):
                print(f'{i+1}:', end='  ')
                for j in range(self.vertices):
                    print(j)   
        