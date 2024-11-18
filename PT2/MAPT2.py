class GrafoMA:
    def __init__(self, num_vertices, direcionado=False):
        self.num_vertices = num_vertices
        self.direcionado = direcionado
        self.matriz_adjacencia = [[0] * num_vertices for _ in range(num_vertices)]

    def exibir_matriz_adjacencia(self):
        """Exibe a matriz de adjacência."""
        for linha in self.matriz_adjacencia:
            print(' '.join(map(str, linha)))

    def adicionar_vertices(self, qtd_vertices):
        """Adiciona vértices ao grafo, aumentando o tamanho da matriz de adjacência."""
        # Expande a matriz para o número correto de vértices
        nova_matriz = [[0] * (self.num_vertices + qtd_vertices) for _ in range(self.num_vertices + qtd_vertices)]

        # Copia as entradas existentes para a nova matriz
        for i in range(self.num_vertices):
            for j in range(self.num_vertices):
                nova_matriz[i][j] = self.matriz_adjacencia[i][j]

        # Atualiza a matriz de adjacência com o novo tamanho
        self.matriz_adjacencia = nova_matriz
        self.num_vertices += qtd_vertices


    def adicionar_aresta(self, vertice1, vertice2, direcionado=False):
        """Adiciona uma aresta entre dois vértices na matriz de adjacência."""
        if vertice1 == vertice2:
            raise ValueError("Não é permitido adicionar loops (aresta de um vértice para ele mesmo).")

        if not direcionado:
            self.matriz_adjacencia[vertice1 - 1][vertice2 - 1] = 1  # Matriz não direcionada
            self.matriz_adjacencia[vertice2 - 1][vertice1 - 1] = 1
        else:
            self.matriz_adjacencia[vertice1 - 1][vertice2 - 1] = 1  # Matriz direcionada

    def encontrar_pontes_tarjan(self):
        """Encontra pontes no grafo usando o algoritmo de Tarjan (adaptado para Matriz de Adjacência)."""
        tempo_descoberta = {}
        menor_tempo = {}
        pai = {}
        pontes = []
        tempo = [0]

        def dfs(v):
            tempo_descoberta[v] = menor_tempo[v] = tempo[0]
            tempo[0] += 1

            for u in range(self.num_vertices):
                if self.matriz_adjacencia[v][u] == 1:
                    if u not in tempo_descoberta:
                        pai[u] = v
                        dfs(u)
                        menor_tempo[v] = min(menor_tempo[v], menor_tempo[u])

                        if menor_tempo[u] > tempo_descoberta[v]:
                            pontes.append((v + 1, u + 1))
                    elif u != pai.get(v):
                        menor_tempo[v] = min(menor_tempo[v], tempo_descoberta[u])

        for v in range(self.num_vertices):
            if v not in tempo_descoberta:
                dfs(v)

        return pontes
