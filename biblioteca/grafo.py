class Grafo:
    def __init__(self, direcionado=False, num_vertices=0):
        self.direcionado = direcionado
        self.lista = {}  # Lista de adjacência
        self.rotulos_vertices = {}  # Armazena rótulos dos vértices
        self.pesos_vertices = {}  # Armazena pesos dos vértices (opcional)
        self.rotulos_arestas = {}  # Armazena rótulos das arestas (opcional)
        self.pesos_arestas = {}  # Armazena pesos das arestas (opcional)
        self.num_vertices = 0  # Inicializa o número de vértices

        # Adiciona os vértices iniciais, se fornecidos
        for i in range(num_vertices):
            self.adicionar_vertice(str(i))
    
    def mapear_vertices_para_indices(self):
        """
        Retorna um dicionário que mapeia os vértices (strings) para índices inteiros.
        """
        return {vertice: idx for idx, vertice in enumerate(self.lista.keys())}


    def adicionar_vertice(self, vertice, rotulo=None):
        if vertice not in self.lista:
            self.lista[vertice] = []
            self.rotulos_vertices[vertice] = rotulo if rotulo else "sem rótulo"
            self.num_vertices += 1

    def remover_vertice(self, vertice):
        if vertice in self.lista:
            del self.lista[vertice]
            self.num_vertices -= 1
            for v in self.lista:
                if vertice in self.lista[v]:
                    self.lista[v].remove(vertice)
            print(f"Vértice '{vertice}' removido.")
        else:
            print(f"Vértice '{vertice}' não existe.")

    def adicionar_aresta(self, u, v, rotulo=None):
        if u not in self.lista:
            self.adicionar_vertice(u)
        if v not in self.lista:
            self.adicionar_vertice(v)
        if v not in self.lista[u]:
            self.lista[u].append(v)
            if not self.direcionado:
                self.lista[v].append(u)
            if rotulo:
                self.rotulos_arestas[(u, v)] = rotulo
            print(f"Aresta adicionada entre '{u}' e '{v}' com rótulo '{rotulo}'.")
        else:
            print(f"Aresta entre '{u}' e '{v}' já existe.")

    def remover_aresta(self, u=None, v=None, rotulo=None):
        """
        Remove uma aresta entre os vértices `u` e `v`, ou pela `rotulo` se especificado.
        """
        if rotulo:  # Se fornecido o rótulo da aresta
            for (origem, destino), r in list(self.rotulos_arestas.items()):
                if r == rotulo:
                    self.lista[origem].remove(destino)
                    if not self.direcionado:
                        self.lista[destino].remove(origem)
                    del self.rotulos_arestas[(origem, destino)]
                    print(f"Aresta com rótulo '{rotulo}' removida entre '{origem}' e '{destino}'.")
                    return
            print(f"Aresta com rótulo '{rotulo}' não encontrada.")
        elif u and v:  # Se fornecidos os vértices
            if u in self.lista and v in self.lista[u]:
                self.lista[u].remove(v)
                if not self.direcionado:
                    self.lista[v].remove(u)
                # Remove o rótulo associado à aresta, se existir
                self.rotulos_arestas.pop((u, v), None)
                print(f"Aresta removida entre '{u}' e '{v}'.")
            else:
                print(f"Aresta entre '{u}' e '{v}' não existe.")
        else:
            print("Erro: Especifique os vértices ou o rótulo da aresta a ser removida.")
    
    def existe_aresta(self, origem, destino):
        """
        Verifica se uma aresta entre `origem` e `destino` existe.
        """
        return origem in self.lista and destino in self.lista[origem]

    def exibir_lista(self):
        print("Lista de Adjacência:")
        for vertice, adjacentes in self.lista.items():
            print(f"{vertice}: {', '.join(map(str, adjacentes))}")

    def grau(self, vertice):
        """
        Calcula o grau do vértice no grafo.
        Para grafos não direcionados, retorna o número de arestas conectadas ao vértice.
        Para grafos direcionados, retorna o grau de entrada e saída.
        """
        if vertice not in self.lista:
            print(f"Vértice '{vertice}' não existe!")
            return None

        if not self.direcionado:
            # Para grafos não direcionados, o grau é o número de adjacentes
            return len(self.lista[vertice])
        else:
            # Para grafos direcionados
            grau_saida = len(self.lista[vertice])  # Número de arestas saindo do vértice
            grau_entrada = sum(1 for v in self.lista if vertice in self.lista[v])  # Número de arestas entrando no vértice
            return {"grau_entrada": grau_entrada, "grau_saida": grau_saida}
        
    def exibir_matriz_adjacencia(self):
        """
        Exibe a matriz de adjacência do grafo.
        Para grafos direcionados, 1 indica aresta de u para v.
        Para grafos não direcionados, 1 indica uma conexão entre u e v.
        Exibe rótulos das arestas, se existirem.
        """
        vertices = list(self.lista.keys())
        n = len(vertices)
        matriz = [["0" for _ in range(n)] for _ in range(n)]
        
        for i, u in enumerate(vertices):
            for j, v in enumerate(vertices):
                if self.existe_aresta(u, v):
                    rotulo = self.rotulos_arestas.get((u, v), "1")
                    matriz[i][j] = rotulo

        print("Matriz de Adjacência:")
        print("   " + "  ".join(vertices))
        for i, linha in enumerate(matriz):
            print(vertices[i] + "  " + "  ".join(linha))


    def exibir_matriz_incidencia(self):
        """
        Exibe a matriz de incidência do grafo.
        As colunas representam arestas, e as linhas representam vértices.
        Cada célula contém o rótulo da aresta (ou 1 se não houver rótulo).
        Para grafos direcionados:
            - Entrada (aresta entrando no vértice): -1
            - Saída (aresta saindo do vértice): 1
        """
        vertices = list(self.lista.keys())
        arestas = list(self.rotulos_arestas.keys())
        n = len(vertices)
        m = len(arestas)
        matriz = [["0" for _ in range(m)] for _ in range(n)]

        for j, (u, v) in enumerate(arestas):
            rotulo = self.rotulos_arestas.get((u, v), "1")
            u_idx = vertices.index(u)
            v_idx = vertices.index(v)
            matriz[u_idx][j] = rotulo if not self.direcionado else "1"  # Saída
            if not self.direcionado:
                matriz[v_idx][j] = rotulo
            else:
                matriz[v_idx][j] = "-1"  # Entrada

        print("Matriz de Incidência:")
        print("   " + "  ".join(f"e{j}" for j in range(m)))
        for i, linha in enumerate(matriz):
            print(vertices[i] + "  " + "  ".join(linha))

    def checar_adjacencia_vertices(self, u, v):
        """
        Verifica se existe uma aresta entre os vértices `u` e `v`.
        Para grafos direcionados, verifica a aresta de u para v.
        Para grafos não direcionados, verifica a aresta entre u e v (ou vice-versa).
        """
        if u in self.lista and v in self.lista[u]:
            print(f"Existe uma aresta entre '{u}' e '{v}'.")
            return True
        elif not self.direcionado and v in self.lista and u in self.lista[v]:
            print(f"Existe uma aresta entre '{u}' e '{v}'.")
            return True
        else:
            print(f"Não existe aresta entre '{u}' e '{v}'.")
            return False
        
    def checar_adjacencia_arestas(self, aresta1, aresta2):
        """
        Verifica se duas arestas são adjacentes.
        Duas arestas são adjacentes se elas compartilham um vértice.
        """
        if aresta1 not in self.rotulos_arestas.values() or aresta2 not in self.rotulos_arestas.values():
            print(f"As arestas '{aresta1}' ou '{aresta2}' não existem.")
            return False

        # Encontra os vértices correspondentes às arestas
        vertice1_1, vertice1_2 = next(((u, v) for (u, v), r in self.rotulos_arestas.items() if r == aresta1), (None, None))
        vertice2_1, vertice2_2 = next(((u, v) for (u, v), r in self.rotulos_arestas.items() if r == aresta2), (None, None))
        
        # Verifica se as arestas compartilham algum vértice
        if vertice1_1 in [vertice2_1, vertice2_2] or vertice1_2 in [vertice2_1, vertice2_2]:
            print(f"As arestas '{aresta1}' e '{aresta2}' são adjacentes.")
            return True
        else:
            print(f"As arestas '{aresta1}' e '{aresta2}' não são adjacentes.")
            return False

       
