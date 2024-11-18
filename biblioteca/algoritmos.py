# Este módulo conterá algoritmos relacionados ao percurso euleriano.

# Funções principais:
# Algoritmo de Fleury para encontrar um caminho euleriano.
# Funções auxiliares para verificação de ciclos eulerianos e grafos eulerianos.

# Objetivo: Centralizar os algoritmos de busca e percurso nos grafos, 
# especialmente aqueles relacionados ao caminho e ciclo euleriano.


from representacoes.lista_adjacencia import GrafoListaAdjacencia
from representacoes.matriz_adjacencia import GrafoMatrizAdjacencia
from representacoes.matriz_incidencia import GrafoMatrizIncidencia


# lista de ajdacencia
def kosaraju(self):
        def dfs(v, visitados, stack=None):
            visitados[v] = True
            for adjacente in self.grafo[v]:
                if not visitados[adjacente]:
                    dfs(adjacente, visitados, stack)
            if stack is not None:
                stack.append(v)

        visitados = [False] * self.num_vertices
        stack = []

        for vertice in range(self.num_vertices):
            if not visitados[vertice]:
                dfs(vertice, visitados, stack)

        grafo_transposto = self.duplicar_grafo()
        grafo_transposto.grafo = {v: [] for v in grafo_transposto.grafo}

        for v1 in self.grafo:
            for v2 in self.grafo[v1]:
                grafo_transposto.adicionar_aresta(v2, v1, self.direcionado)

        visitados = [False] * self.num_vertices
        sccs = []

        while stack:
            vertice = stack.pop()
            if not visitados[vertice]:
                componente = []
                grafo_transposto.dfs(vertice, visitados, componente)
                sccs.append(componente)

        return sccs

def fleury(self):
    # Algoritmo de Fleury para encontrar um caminho euleriano
    pass

