class GrafoLA:
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