class Grafo:
    def __init__(self, num_vertices, direcionado=False):
        self.num_vertices = num_vertices
        self.grafo = [[0] * num_vertices for _ in range(num_vertices)]  # Matriz de adjacência
        self.direcionado = direcionado
        self.vertices_ponderados = {}  # Ponderação dos vértices
        self.rotulos_vertices = {}  # Rótulos dos vértices
        self.arestas_ponderadas = {}  # Ponderação e rótulos das arestas

    # Funções de manipulação do grafo (adição e remoção de vértices e arestas)
    def adicionar_aresta(self, vertice1, vertice2, peso=1, direcionado=False):
        if vertice1 >= self.num_vertices or vertice2 >= self.num_vertices:
            raise ValueError("Um dos vértices fornecidos não existe.")
        if vertice1 == vertice2:
            raise ValueError("Não é permitido adicionar loops (aresta de um vértice para ele mesmo).")
        if self.grafo[vertice1][vertice2] != 0:
            raise ValueError(f"Aresta entre {vertice1} e {vertice2} já existe.")
        
        self.grafo[vertice1][vertice2] = peso
        if not direcionado:
            self.grafo[vertice2][vertice1] = peso

    def remover_aresta_por_vertices(self, vertice1, vertice2):
        if vertice1 < self.num_vertices and vertice2 < self.num_vertices:
            self.grafo[vertice1][vertice2] = 0
            self.grafo[vertice2][vertice1] = 0
        else:
            print("Um dos vértices não existe.")

    def ponderar_e_rotular_vertices(self):
        for vertice in range(self.num_vertices):
            rotulo = input(f"Insira o rótulo para o vértice {vertice}: ")
            peso = float(input(f"Insira o peso para o vértice {vertice}: "))
            self.rotulos_vertices[vertice] = rotulo
            self.vertices_ponderados[vertice] = peso

    # Métodos de consulta e exibição
    def exibir_com_rotulos_e_pesos(self):
        for vertice in range(self.num_vertices):
            adj_formatado = []
            for adjacente in range(self.num_vertices):
                if self.grafo[vertice][adjacente] != 0:
                    adj_formatado.append(f"({adjacente}) [Peso: {self.grafo[vertice][adjacente]}]")
            print(f"{vertice} -> {adj_formatado}")

    def contar_arestas(self):
        count = sum(sum(1 for x in linha if x != 0) for linha in self.grafo)
        return count if self.direcionado else count // 2

    def checar_vazio(self):
        for linha in self.grafo:
            if any(linha):
                return False
        return True

    def checar_completo(self):
        for i in range(self.num_vertices):
            for j in range(self.num_vertices):
                if i != j:
                    if self.direcionado:
                        if self.grafo[i][j] == 0:
                            return False
                    else:
                        if self.grafo[i][j] == 0 and self.grafo[j][i] == 0:
                            return False
        return True

    def checar_conectividade(self):
        def dfs(v, visitados):
            visitados.add(v)
            for i in range(self.num_vertices):
                if self.grafo[v][i] != 0 and i not in visitados:
                    dfs(i, visitados)

        visitados = set()
        dfs(0, visitados)  # Começa o DFS a partir do vértice 0
        return "conexo" if len(visitados) == self.num_vertices else "não conexo"

    # Funções relacionadas a pontes e articulações
    def duplicar_grafo(self):
        grafo_duplicado = Grafo(self.num_vertices, self.direcionado)
        for i in range(self.num_vertices):
            for j in range(self.num_vertices):
                if self.grafo[i][j] != 0:
                    grafo_duplicado.adicionar_aresta(i, j, self.grafo[i][j], self.direcionado)
        return grafo_duplicado

    def remover_vertice_e_arestas(self, vertice):
        """Remove o vértice e todas as arestas que o conectam."""
        if vertice < self.num_vertices:
            for i in range(self.num_vertices):
                self.grafo[vertice][i] = 0
                self.grafo[i][vertice] = 0
        else:
            print("Vértice não encontrado.")

    def kosaraju(self):
        def dfs(v, visitados, stack=None):
            visitados[v] = True
            for i in range(self.num_vertices):
                if self.grafo[v][i] != 0 and not visitados[i]:
                    dfs(i, visitados, stack)
            if stack is not None:
                stack.append(v)

        visitados = [False] * self.num_vertices
        stack = []

        for vertice in range(self.num_vertices):
            if not visitados[vertice]:
                dfs(vertice, visitados, stack)

        grafo_transposto = self.duplicar_grafo()
        grafo_transposto.grafo = [[0] * self.num_vertices for _ in range(self.num_vertices)]

        for i in range(self.num_vertices):
            for j in range(self.num_vertices):
                if self.grafo[i][j] != 0:
                    grafo_transposto.adicionar_aresta(j, i, self.grafo[i][j], self.direcionado)

        visitados = [False] * self.num_vertices
        sccs = []

        while stack:
            vertice = stack.pop()
            if not visitados[vertice]:
                componente = []
                grafo_transposto.dfs(vertice, visitados, componente)
                sccs.append(componente)

        return sccs

    # Função para verificar se existem múltiplos componentes conexos
    def checar_pontes_por_rotulo(self, rotulo):
        grafo_duplicado = self.duplicar_grafo()
        grafo_duplicado.remover_aresta_por_rotulos(rotulo)

        # Verifica se o grafo duplicado ainda é conexo
        if grafo_duplicado.checar_conectividade() == "não conexo":
            print(f"A aresta com rótulo '{rotulo}' é uma ponte.")
        else:
            print(f"A aresta com rótulo '{rotulo}' não é uma ponte.")

    def checar_pontes_por_vertices(self, vertice1, vertice2):
        grafo_duplicado = self.duplicar_grafo()
        grafo_duplicado.remover_aresta_por_vertices(vertice1, vertice2)

        # Verifica se o grafo duplicado ainda é conexo
        if grafo_duplicado.checar_conectividade() == "não conexo":
            print(f"A aresta entre {vertice1} e {vertice2} é uma ponte.")
        else:
            print(f"A aresta entre {vertice1} e {vertice2} não é uma ponte.")

    def checar_articulacoes(self, vertice):
        grafo_duplicado = self.duplicar_grafo()
        grafo_duplicado.remover_vertice_e_arestas(vertice)

        # Verifica se o grafo duplicado ainda é conexo
        if grafo_duplicado.checar_conectividade() == "não conexo":
            print(f"O vértice {vertice} é uma articulação.")
        else:
            print(f"O vértice {vertice} não é uma articulação.")
