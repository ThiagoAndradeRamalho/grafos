from vertice import Vertice
from aresta import Aresta


class Grafo:

    def __init__(self, direcionado):
        self._lista_vertices = []
        self._lista_arestas = []
        self._matriz_adjacencia = []
        self._matriz_incidencia = []
        self._lista_adjacentes = {}
        self._direcionado = direcionado
        self._vazio = True
        self._completo = True
        self._numComponentesConexos = 0

    @property
    def vertices(self):
        return [str(vertice) for vertice in self._lista_vertices]    
    
    @property
    def arestas(self):
        return [str(areresta) for areresta in self._lista_arestas]
    
    @property
    def direcionado(self):
        return self._direcionado
    
    @property
    def vazio(self):
        return self._vazio
    
    @property
    def completo(self):
        return self._completo
    
    def imprimir_lista_adjacentes(self):
        print('Lista de Adjacência')
        for vertice, adjacentes in self._lista_adjacentes.items():
            print(f'Vertice {vertice}: {adjacentes}')

    def imprimir_matriz_adjacentes(self):
        self.set_matriz_adjacencia()
        print('Matriz de Adjacência')
        for i in range(len(self._matriz_adjacencia)):
            print(self._matriz_adjacencia[i])

    def imprimir_matriz_incidencia(self):
        self.set_matriz_incidencia()
        print('Matriz de Incidencia')
        for i in range(len(self._matriz_incidencia)):
            print(self._matriz_incidencia[i])

    def adjacentes(self, vertice):
        return [str(i) for i in self._lista_adjacentes[vertice]]
    
    def add_vertice(self, vertices):
        self._lista_vertices = [Vertice(rotulo) for rotulo in vertices]

    def add_aresta(self, arestas, peso):
        self._lista_arestas = [Aresta(origem,destino,peso[pos]) for pos, (origem,destino) in enumerate(arestas)]

    def set_lista_adjacentes(self):
        for i in self._lista_vertices:
            self._lista_adjacentes[i.rotulo] = []

    def set_adjacentes(self):
        if not self.direcionado:
            for vertice in self._lista_vertices:
                for aresta in self._lista_arestas:
                    if vertice.rotulo == aresta.origem:
                        self._lista_adjacentes[vertice.rotulo].append(aresta.destino)
                    elif vertice.rotulo == aresta.destino:
                        self._lista_adjacentes[vertice.rotulo].append(aresta.origem)
        else:
            for vertice in self._lista_vertices:
                for aresta in self._lista_arestas:
                    if vertice.rotulo == aresta.origem:
                        self._lista_adjacentes[vertice.rotulo].append(aresta.destino)

    def set_matriz_adjacencia(self):
        n = len(self._lista_vertices)
        rotulos = [v.rotulo for v in self._lista_vertices]
        self._matriz_adjacencia = [[0] * n for _ in range(n)]
        for aresta in self._lista_arestas:
            i = rotulos.index(aresta.origem)
            j = rotulos.index(aresta.destino)

            self._matriz_adjacencia[i][j] = aresta.peso

            if not self.direcionado:
                self._matriz_adjacencia[j][i] = aresta.peso

        return self._matriz_adjacencia
    



    def aresta_existe(self, o, d):
        for aresta in self._lista_arestas:
            return aresta.origem == o and aresta.destino == d

    def num_vertices(self):
        return len(self._lista_vertices)

    def num_arestas(self):
        return len(self._lista_arestas)
    
    def set_matriz_incidencia(self):
        nV = self.num_vertices()
        nA = self.num_arestas()
        rotulos = [v.rotulo for v in self._lista_vertices]
        self._matriz_incidencia = [[0] * nV for _ in range(nA)]

        for x, aresta in enumerate(self._lista_arestas):
            i = rotulos.index(aresta.origem)
            j = rotulos.index(aresta.destino)

            if not self._direcionado:
                self._matriz_incidencia[x][j] = 1
                self._matriz_incidencia[x][i] = 1
            else:
                self._matriz_incidencia[x][j] = 1
                self._matriz_incidencia[x][i] = -1

        return self._matriz_incidencia

                
grafo = Grafo(direcionado=True)  # Se for direcionado, altere para True

# Adicionar Vértices
grafo.add_vertice(['v1', 'v2', 'v3'])

# Adicionar Arestas
arestas = [('v1', 'v2'), ('v2', 'v3')]
pesos = [10, 20]  # Exemplo de pesos para as arestas
grafo.add_aresta(arestas, pesos)

# Inicializar Lista de Adjacentes
grafo.set_lista_adjacentes()

# Adicionar Adjacentes
grafo.set_adjacentes()

grafo.imprimir_lista_adjacentes()

grafo.imprimir_matriz_adjacentes()

grafo.imprimir_matriz_incidencia()

# Imprimir Adjacentes para um Vértice Específico
print("Vértices adjacentes a v1:", grafo.adjacentes('v1'))

# Verificar se uma aresta existe
print("A aresta v1 -> v2 existe?", grafo.aresta_existe('v1', 'v2'))
print("A aresta v1 -> v4 existe?", grafo.aresta_existe('v1', 'v4'))