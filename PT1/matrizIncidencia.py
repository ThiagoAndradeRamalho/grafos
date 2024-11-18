class GrafoIncidencia:
    def __init__(self, num_vertices, direcionado=False):
        self.num_vertices = num_vertices
        self.direcionado = direcionado
        self.matriz_incidencia = []  # Matriz de incidência
        self.arestas_ponderadas = {}  # Ponderação e rótulos das arestas
        self.vertices_ponderados = {}  # Ponderação dos vértices
        self.rotulos_vertices = {}  # Rótulos dos vértices

    # Criação e remoção de arestas
    def adicionar_aresta(self, vertice1, vertice2):
        if vertice1 == vertice2:
            raise ValueError("Não é permitido adicionar loops (aresta de um vértice para ele mesmo).")

        # Criação da nova aresta na matriz de incidência
        nova_aresta = [0] * self.num_vertices
        if self.direcionado:
            nova_aresta[vertice1] = -1  # Aresta saindo de vertice1
            nova_aresta[vertice2] = 1   # Aresta entrando em vertice2
        else:
            nova_aresta[vertice1] = 1  # Conectando vertice1
            nova_aresta[vertice2] = 1  # Conectando vertice2

        # Adiciona a nova coluna (aresta) à matriz de incidência
        self.matriz_incidencia.append(nova_aresta)

    def remover_aresta_por_vertices(self, vertice1, vertice2):
        for i, aresta in enumerate(self.matriz_incidencia):
            if (aresta[vertice1] == 1 and aresta[vertice2] == 1) or \
               (self.direcionado and aresta[vertice1] == -1 and aresta[vertice2] == 1):
                del self.matriz_incidencia[i]
                break

    # Ponderação e rotulação de vértices
    def ponderar_e_rotular_vertices(self):
        for vertice in range(self.num_vertices):
            rotulo = input(f"Insira o rótulo para o vértice {vertice}: ")
            peso = float(input(f"Insira o peso para o vértice {vertice}: "))
            self.rotulos_vertices[vertice] = rotulo
            self.vertices_ponderados[vertice] = peso

    # Ponderação e rotulação de arestas
    def ponderar_e_rotular_arestas(self):
        for i, aresta in enumerate(self.matriz_incidencia):
            rotulo = input(f"Insira o rótulo para a aresta {i}: ")
            peso = float(input(f"Insira o peso para a aresta {i}: "))
            self.arestas_ponderadas[i] = {'rotulo': rotulo, 'peso': peso}

    # Checagem de adjacência entre vértices
    def checar_adjacencia_vertices(self, vertice1, vertice2):
        for aresta in self.matriz_incidencia:
            if aresta[vertice1] == 1 and aresta[vertice2] == 1:
                return True
        return False

    # Checagem da existência de arestas
    def existe_aresta(self, vertice1, vertice2):
        for aresta in self.matriz_incidencia:
            if aresta[vertice1] == 1 and aresta[vertice2] == 1:
                return True
        return False

    # Checagem de grafo vazio e completo
    def checar_vazio(self):
        return len(self.matriz_incidencia) == 0

    def checar_completo(self):
        for v1 in range(self.num_vertices):
            for v2 in range(self.num_vertices):
                if v1 != v2:
                    if not self.existe_aresta(v1, v2):
                        return False
        return True

    # Função para verificar se o grafo é conexo
    def checar_conectividade(self):
        def dfs(v, visitados):
            visitados.add(v)
            for i, aresta in enumerate(self.matriz_incidencia):
                if aresta[v] == 1:
                    vertice_adjacente = aresta.index(1) if aresta.index(1) != v else aresta[::-1].index(1)
                    if vertice_adjacente not in visitados:
                        dfs(vertice_adjacente, visitados)

        visitados = set()
        dfs(0, visitados)  # Começa a partir do vértice 0
        return "conexo" if len(visitados) == self.num_vertices else "não conexo"

    def duplicar_grafo(self):
        grafo_duplicado = GrafoIncidencia(self.num_vertices, self.direcionado)
        for aresta in self.matriz_incidencia:
            grafo_duplicado.matriz_incidencia.append(aresta[:])
        return grafo_duplicado

    # Função para verificar se existem múltiplos componentes conexos
    def checar_pontes_por_rotulo(self, rotulo):
        # Criar grafo duplicado e remover a aresta com o rótulo específico
        grafo_duplicado = self.duplicar_grafo()
        aresta_id = None
        for i, aresta in enumerate(self.matriz_incidencia):
            if self.arestas_ponderadas.get(i, {}).get("rotulo") == rotulo:
                aresta_id = i
                break

        if aresta_id is not None:
            grafo_duplicado.remover_aresta_por_vertices(aresta_id)

            # Verifica se o grafo duplicado ainda é conexo
            if grafo_duplicado.checar_conectividade() == "não conexo":
                print(f"A aresta com rótulo '{rotulo}' é uma ponte.")
            else:
                print(f"A aresta com rótulo '{rotulo}' não é uma ponte.")
        else:
            print(f"A aresta com rótulo '{rotulo}' não foi encontrada.")

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
