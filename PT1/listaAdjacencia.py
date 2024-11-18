class Grafo:
    def __init__(self, num_vertices, direcionado=False):
        self.num_vertices = num_vertices
        self.grafo = {i: [] for i in range(1, num_vertices + 1)}  # Lista de adjacência
        self.direcionado = direcionado
        self.vertices_ponderados = {}  # Ponderação dos vértices
        self.rotulos_vertices = {}  # Rótulos dos vértices
        self.arestas_ponderadas = {}  # Ponderação e rótulos das arestas
        
    def exibir_lista_adjacencia(self):
        """Exibe a lista de adjacencia do grafo no formato desejado."""
        for vertice, adjacentes in self.grafo.items():
            print(f"{vertice} -> {adjacentes}")

    def adicionar_vertices(self, qtd_vertices):
        """Adiciona um numero especificado de novos vertices ao grafo."""
        self.num_vertices += qtd_vertices
        for i in range(self.num_vertices - qtd_vertices + 1, self.num_vertices + 1):
            self.grafo[i] = []

    # Funções de manipulação do grafo (adição e remoção de vértices e arestas)
    def adicionar_aresta(self, vertice1, vertice2, direcionado=False):
        if vertice1 not in self.grafo or vertice2 not in self.grafo:
            raise ValueError("Um dos vértices fornecidos não existe.")
        if vertice1 == vertice2:
            raise ValueError("Não é permitido adicionar loops (aresta de um vértice para ele mesmo).")
        if direcionado:
            if vertice2 in self.grafo[vertice1]:
                raise ValueError(f"Aresta {vertice1} -> {vertice2} já existe.")
        else:
            if vertice2 in self.grafo[vertice1] or vertice1 in self.grafo[vertice2]:
                raise ValueError(f"Aresta entre {vertice1} e {vertice2} já existe.")
        
        self.grafo[vertice1].append(vertice2)
        if not direcionado:
            self.grafo[vertice2].append(vertice1)

    def remover_aresta_por_vertices(self, vertice1, vertice2):
        if vertice1 in self.grafo and vertice2 in self.grafo:
            if vertice2 in self.grafo[vertice1]:
                self.grafo[vertice1].remove(vertice2)
            if vertice1 in self.grafo[vertice2]:
                self.grafo[vertice2].remove(vertice1)
        else:
            print("Um dos vértices não existe.")

    def ponderar_e_rotular_vertices(self):
        for vertice in self.grafo:
            rotulo = input(f"Insira o rótulo para o vértice {vertice}: ")
            peso = float(input(f"Insira o peso para o vértice {vertice}: "))
            self.rotulos_vertices[vertice] = rotulo
            self.vertices_ponderados[vertice] = peso

    # Métodos de consulta e exibição
    def exibir_com_rotulos_e_pesos(self):
        for vertice, adjacentes in self.grafo.items():
            adj_formatado = []
            for adjacente in adjacentes:
                adj_formatado.append(f"({adjacente}) [Peso: {self.vertices_ponderados.get(adjacente, 0)}]")
            print(f"{vertice} -> {adj_formatado}")

    def contar_arestas(self):
        count = sum(len(adjacentes) for adjacentes in self.grafo.values())
        return count if self.direcionado else count // 2

    def checar_vazio(self):
        for adjacentes in self.grafo.values():
            if adjacentes:
                return False
        return True

    def checar_completo(self):
        for v1 in self.grafo:
            for v2 in self.grafo:
                if v1 != v2:
                    if self.direcionado:
                        if v2 not in self.grafo[v1]:
                            return False
                    else:
                        if v2 not in self.grafo[v1] and v1 not in self.grafo[v2]:
                            return False
        return True

    def checar_conectividade(self):
        def dfs(v, visitados):
            visitados.add(v)
            for vizinho in self.grafo[v]:
                if vizinho not in visitados:
                    dfs(vizinho, visitados)

        visitados = set()
        dfs(1, visitados)
        if len(visitados) == self.num_vertices:
            return "conexo"
        return "não conexo"

    # Funções relacionadas a pontes e articulações
    def duplicar_grafo(self):
        grafo_duplicado = Grafo(self.num_vertices, self.direcionado)
        for v1 in self.grafo:
            for v2 in self.grafo[v1]:
                grafo_duplicado.adicionar_aresta(v1, v2, self.direcionado)
        return grafo_duplicado

    def remover_vertice_e_arestas(self, vertice):
        """Remove o vértice e todas as arestas que o conectam."""
        if vertice in self.grafo:
            del self.grafo[vertice]
            for v in self.grafo:
                if vertice in self.grafo[v]:
                    self.grafo[v].remove(vertice)

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

    # Função para verificar se existem múltiplos componentes conexos
    def checar_pontes_por_rotulo(self, rotulo):
        grafo_duplicado = self.duplicar_grafo()
        grafo_duplicado.remover_aresta_por_rotulo(rotulo)

        # Verifica se o grafo duplicado ainda é conexo
        if not grafo_duplicado.verificar_conectividade():
            print(f"A aresta com rótulo '{rotulo}' é uma ponte.")
        else:
            print(f"A aresta com rótulo '{rotulo}' não é uma ponte.")

    def checar_pontes_por_vertices(self, vertice1, vertice2):
        grafo_duplicado = self.duplicar_grafo()
        grafo_duplicado.remover_aresta_por_vertices(vertice1, vertice2)

        # Verifica se o grafo duplicado ainda é conexo
        if not grafo_duplicado.verificar_conectividade():
            print(f"A aresta entre {vertice1} e {vertice2} é uma ponte.")
        else:
            print(f"A aresta entre {vertice1} e {vertice2} não é uma ponte.")

    def checar_articulacoes(self, vertice):
        grafo_duplicado = self.duplicar_grafo()
        grafo_duplicado.remover_vertice_e_arestas(vertice)

        # Verifica se o grafo duplicado ainda é conexo
        if not grafo_duplicado.verificar_conectividade():
            print(f"O vértice {vertice} é uma articulação.")
        else:
            print(f"O vértice {vertice} não é uma articulação.")
    
    def encontrar_pontes_tarjan(self):
    # Inicializando os vetores necessários
        tempo_descoberta = {}  # Tempo de descoberta de cada vértice
        menor_tempo = {}       # Menor tempo alcançável a partir do vértice
        pai = {}               # Pai do vértice na DFS
        pontes = []            # Lista para armazenar as pontes encontradas
        tempo = [0]            # Contador de tempo (usado como lista para mutabilidade)

    # Função DFS interna
        def dfs(v):
            # Configura o tempo de descoberta e o menor tempo inicial do vértice atual
            tempo_descoberta[v] = menor_tempo[v] = tempo[0]
            tempo[0] += 1

            # Explorar todos os vizinhos de v
            for u in self.grafo[v]:
                if u not in tempo_descoberta:  # Se o vértice u não foi visitado
                    pai[u] = v
                    dfs(u)  # Recursão na DFS

                    # Após a DFS de u, atualizar o menor_tempo de v
                    menor_tempo[v] = min(menor_tempo[v], menor_tempo[u])

                    # Verificar se a aresta (v, u) é uma ponte
                    if menor_tempo[u] > tempo_descoberta[v]:
                        pontes.append((v, u))
                # Se u já foi visitado e não é o pai de v, atualizar menor_tempo[v]
                elif u != pai.get(v):
                    menor_tempo[v] = min(menor_tempo[v], tempo_descoberta[u])

    # Iniciar DFS para todos os vértices não visitados
        for v in self.grafo:
            if v not in tempo_descoberta:
                dfs(v)

        return pontes