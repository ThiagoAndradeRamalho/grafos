class GrafoMI:
    def __init__(self, num_vertices, direcionado=False):
        self.num_vertices = num_vertices
        self.direcionado = direcionado  # Define se o grafo é direcionado ou não
        self.arestas = []  # Lista para armazenar as arestas
        self.rotulos_arestas = {}  # Dicionário para armazenar os rótulos das arestas
        self.matriz_incidencia = []  # Matriz de incidência (inicialmente vazia)
        self.grafo = {i: [] for i in range(num_vertices)}  # Inicializa a lista de adjacência vazia

    def adicionar_aresta(self, vertice1, vertice2):
        if vertice1 == vertice2:
            raise ValueError("Não é permitido adicionar loops (aresta de um vértice para ele mesmo).")

        # Ajustar os vértices para começar de 0, se necessário
        vertice1 -= 1
        vertice2 -= 1

        # Adiciona a aresta à lista de arestas
        self.arestas.append((vertice1, vertice2))

        # Se for necessário, podemos solicitar o rótulo da aresta
        rotulo = input(f"Insira o rótulo para a aresta conectando {vertice1 + 1} e {vertice2 + 1}: ")
        self.rotulos_arestas[(vertice1, vertice2)] = rotulo
        if not self.direcionado:
            self.rotulos_arestas[(vertice2, vertice1)] = rotulo  # Para grafos não direcionados

        # Atualiza a lista de adjacência
        self.grafo[vertice1].append(vertice2)
        self.grafo[vertice2].append(vertice1)  # Para grafos não direcionados

    def adicionar_vertices(self, qtd_vertices):
        """Adiciona um número especificado de novos vértices ao grafo."""
        self.num_vertices += qtd_vertices
        # Adiciona novos vértices à lista de adjacência
        for i in range(self.num_vertices - qtd_vertices, self.num_vertices):
            self.grafo[i] = []

    def montar_matriz_incidencia(self):
        """Montar a matriz de incidência depois de adicionar as arestas"""
        # A matriz de incidência terá o número de linhas igual ao número de arestas
        # e o número de colunas igual ao número de vértices
        self.matriz_incidencia = [[0] * self.num_vertices for _ in range(len(self.arestas))]

        for i, (vertice1, vertice2) in enumerate(self.arestas):
            if self.direcionado:
                self.matriz_incidencia[i][vertice1] = -1  # Aresta saindo do vértice1
                self.matriz_incidencia[i][vertice2] = 1   # Aresta entrando no vértice2
            else:
                self.matriz_incidencia[i][vertice1] = 1  # Conectando vertice1
                self.matriz_incidencia[i][vertice2] = 1  # Conectando vertice2

    def exibir_matriz_incidencia(self):
        """Exibe a matriz de incidência do grafo no formato desejado."""
        print("Matriz de Incidência:")
        for aresta in self.matriz_incidencia:
            print(" ".join(map(str, aresta)))

    def encontrar_pontes_tarjan(self):
        # Variáveis auxiliares
        time = [0]  # Tempo de descoberta de vértices
        pontes = []  # Lista para armazenar as pontes
        descoberta = [-1] * self.num_vertices  # Armazena o tempo de descoberta de cada vértice
        menor = [-1] * self.num_vertices  # Armazena o menor tempo de descoberta de um vértice adjacente
        pai = [-1] * self.num_vertices  # Pai de cada vértice durante a DFS

        def dfs(v):
            """Função de busca em profundidade (DFS) com a detecção de pontes"""
            descoberta[v] = menor[v] = time[0]
            time[0] += 1

            for u in self.grafo[v]:  # Aqui acessa a lista de adjacência
                if descoberta[u] == -1:  # Se o vértice u não foi visitado
                    pai[u] = v
                    dfs(u)
                    menor[v] = min(menor[v], menor[u])

                    # Se a condição de ponte for satisfeita
                    if menor[u] > descoberta[v]:
                        pontes.append((v + 1, u + 1))  # Ajustar para índices começando de 1
                elif u != pai[v]:  # Se u já foi visitado e não é o pai de v
                    menor[v] = min(menor[v], descoberta[u])

        # Iniciar DFS em todos os vértices
        for v in range(self.num_vertices):
            if descoberta[v] == -1:
                dfs(v)

        return pontes  # Retorna a lista de pontes encontradas
