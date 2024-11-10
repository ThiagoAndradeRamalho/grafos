class Grafo:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.grafo = {i: [] for i in range(1, num_vertices + 1)}  # Lista de adjacência
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

    def adicionar_aresta(self):
        """Adiciona arestas entre vertices, perguntando ao usuario quais vertices ligar e se todas as ligacoes serao direcionadas ou nao. 
        Repete as ligacoes ate o usuario digitar 'FIM'."""
        
        # Pergunta ao usuario se todas as arestas serao direcionadas ou nao
        resposta = input("Deseja que o grafo seja direcionado? (s/n): ").strip().lower()
        direcionado = resposta == 's'
        
        while True:
            # Solicita ao usuario os vertices a serem ligados
            entrada = input("Digite os vertices a serem ligados no formato 'vertice1 vertice2' ou 'FIM' para encerrar: ").strip()
            
            if entrada.lower() == 'fim':
                print("Encerrando a adicao de arestas.")
                break
            
            try:
                # Separa os vertices de entrada
                vertice1, vertice2 = map(int, entrada.split())
                
                # Verifica se os vertices existem no grafo
                if vertice1 in self.grafo and vertice2 in self.grafo:
                    if direcionado:
                        # Aresta direcionada: adiciona apenas a direcao de vertice1 -> vertice2
                        self.grafo[vertice1].append(vertice2)
                        print(f"Aresta direcionada adicionada de {vertice1} para {vertice2}.")
                    else:
                        # Aresta nao direcionada: adiciona as duas direcoes
                        if vertice2 not in self.grafo[vertice1]:
                            self.grafo[vertice1].append(vertice2)
                        if vertice1 not in self.grafo[vertice2]:
                            self.grafo[vertice2].append(vertice1)
                        print(f"Aresta nao direcionada adicionada entre {vertice1} e {vertice2}.")
                else:
                    print("Um dos vertices nao existe.")
                    
            except ValueError:
                print("Entrada invalida. Certifique-se de digitar dois numeros inteiros ou 'FIM' para encerrar.")
                
####################### REMOCAO DE ARESTAS #######################
                                
    def ponderar_e_rotular_vertices(self):
        """Permite ao usuário definir rótulos e ponderações para cada vértice do grafo."""
        print("\nPonderação e rotulação dos vértices:")
        for vertice in self.grafo:
            rotulo = input(f"Insira o rótulo para o vértice {vertice}: ")
            peso = float(input(f"Insira o peso para o vértice {vertice}: "))
            
            # Armazena o rótulo e o peso do vértice
            self.rotulos_vertices[vertice] = rotulo
            self.vertices_ponderados[vertice] = peso
            
        print("\nRótulos e ponderações dos vértices definidos com sucesso.")
    
    def exibir_com_rotulos_e_pesos_vertices(self):
        """Exibe os rótulos e pesos dos vértices."""
        print("\nRótulos e Pesos dos Vértices:")
        for vertice in self.grafo:
            rotulo = self.rotulos_vertices.get(vertice, "Sem rótulo")
            peso = self.vertices_ponderados.get(vertice, 0)
            print(f"Vértice {vertice}: Rótulo: {rotulo}, Peso: {peso}")

    def ponderar_e_rotular_arestas(self):
        """Permite ao usuário definir rótulos e ponderações para cada aresta do grafo, levando em conta se o grafo é direcionado ou não."""
        print("\nPonderação e rotulação das arestas:")
        for vertice, adjacentes in self.grafo.items():
            for adjacente in adjacentes:
                # Se o grafo não é direcionado, verifica se a aresta já foi ponderada e rotulada
                if not self.grafo_direcionada(vertice, adjacente):
                    # Aresta direcionada ou não foi ponderada
                    rotulo = input(f"Insira o rótulo para a aresta de {vertice} para {adjacente}: ")
                    peso = float(input(f"Insira o peso para a aresta de {vertice} para {adjacente}: "))
                    
                    # Armazena o rótulo e peso da aresta
                    self.arestas_ponderadas[(vertice, adjacente)] = {"rotulo": rotulo, "peso": peso}
                    print(f"Aresta de {vertice} para {adjacente} ponderada e rotulada com sucesso.")
                    
                    # Caso o grafo seja não direcionado, adiciona a aresta na direção oposta
                    if vertice != adjacente:
                        self.arestas_ponderadas[(adjacente, vertice)] = {"rotulo": rotulo, "peso": peso}
                    
    def grafo_direcionada(self, vertice1, vertice2):
        """Verifica se a aresta (vertice1, vertice2) é direcionada ou já foi ponderada e rotulada"""
        return (vertice1, vertice2) in self.arestas_ponderadas

    def exibir_com_rotulos_e_pesos(self):
        """Exibe o grafo com rótulos e pesos das arestas."""
        print("\nLista de Adjacência com Rótulos e Pesos das Arestas:")
        for vertice, adjacentes in self.grafo.items():
            adj_formatado = []
            for adjacente in adjacentes:
                # Verifica se a aresta está ponderada
                if (vertice, adjacente) in self.arestas_ponderadas:
                    rotulo = self.arestas_ponderadas[(vertice, adjacente)]["rotulo"]
                    peso = self.arestas_ponderadas[(vertice, adjacente)]["peso"]
                    adj_formatado.append(f"({adjacente}) [{rotulo}, Peso: {peso}]")
                else:
                    adj_formatado.append(f"({adjacente}) [Sem rótulo, Peso: 0]")
            print(f"{vertice} -> {adj_formatado}")
            
####################### TESTAR DAQUI PRA BAIXO #######################

    def checar_adjacencia_vertices(self):
        """Verifica se dois vértices são adjacentes, considerando a direção das arestas em grafos direcionados."""
        vertice1 = int(input("Digite o primeiro vértice: "))
        vertice2 = int(input("Digite o segundo vértice: "))

        if vertice1 in self.grafo and vertice2 in self.grafo:
            if self.direcionado:
                if vertice2 in self.grafo[vertice1]:
                    print(f"{vertice1} -> {vertice2}: São adjacentes (direção considerada).")
                    return True
                else:
                    print(f"{vertice1} -> {vertice2}: Não são adjacentes (direção considerada).")
                    return False
            else:
                if vertice2 in self.grafo[vertice1] or vertice1 in self.grafo[vertice2]:
                    print(f"{vertice1} <-> {vertice2}: São adjacentes (grafo não direcionado).")
                    return True
                else:
                    print(f"{vertice1} <-> {vertice2}: Não são adjacentes (grafo não direcionado).")
                    return False
        else:
            print("Um dos vértices não existe.")
            return False

    def checar_adjacencia_arestas(self):
        """Verifica se duas arestas são adjacentes, considerando a direção das arestas em grafos direcionados."""
        aresta1 = input("Digite a primeira aresta no formato 'vertice1 vertice2': ").strip()
        aresta2 = input("Digite a segunda aresta no formato 'vertice1 vertice2': ").strip()

        try:
            v1_arest1, v2_arest1 = map(int, aresta1.split())
            v1_arest2, v2_arest2 = map(int, aresta2.split())

            if self.direcionado:
                # Em grafos direcionados, as arestas são direcionadas, por isso a checagem precisa considerar a direção.
                if (v2_arest1 == v1_arest2) or (v1_arest1 == v1_arest2) or (v2_arest1 == v2_arest2):
                    print(f"As arestas ({aresta1}) e ({aresta2}) são adjacentes (direção considerada).")
                    return True
                else:
                    print(f"As arestas ({aresta1}) e ({aresta2}) não são adjacentes (direção considerada).")
                    return False
            else:
                # Em grafos não direcionados, basta compartilhar um vértice para serem adjacentes.
                if v1_arest1 == v1_arest2 or v1_arest1 == v2_arest2 or v2_arest1 == v1_arest2 or v2_arest1 == v2_arest2:
                    print(f"As arestas ({aresta1}) e ({aresta2}) são adjacentes (grafo não direcionado).")
                    return True
                else:
                    print(f"As arestas ({aresta1}) e ({aresta2}) não são adjacentes (grafo não direcionado).")
                    return False
        except ValueError:
            print("Entrada inválida. Certifique-se de digitar as arestas no formato 'vertice1 vertice2'.")
            return False
        
####################### Checagem da existência de arestas #######################

####################### Checagem da quantidade de vértices e arestas #######################

####################### Checagem de grafo vazio #######################

    def checar_completo(self):
        """Verifica se o grafo é completo, considerando a direção das arestas."""
        if self.direcionado:
            for v1 in self.grafo:
                for v2 in self.grafo:
                    if v1 != v2:
                        if v2 not in self.grafo[v1] or v1 not in self.grafo[v2]:
                            print(f"O grafo não é completo. Falta aresta entre {v1} e {v2}.")
                            return False
            print("O grafo é completo (em ambas as direções para grafos direcionados).")
            return True
        else:
            for v1 in self.grafo:
                for v2 in self.grafo:
                    if v1 != v2:
                        if v2 not in self.grafo[v1] and v1 not in self.grafo[v2]:
                            print(f"O grafo não é completo. Falta aresta entre {v1} e {v2}.")
                            return False
            print("O grafo é completo (grafo não direcionado).")
            return True

    def checar_conectividade(self):
        """Verifica a conectividade do grafo, considerando se é simples, semi-forte ou fortemente conexo."""
        def dfs(v, visitados):
            visitados.add(v)
            for vizinho in self.grafo[v]:
                if vizinho not in visitados:
                    dfs(vizinho, visitados)

        visitados = set()
        dfs(1, visitados)  # Começa a partir do vértice 1

        if len(visitados) == self.num_vertices:
            if self.direcionado:
                print("O grafo é fortemente conexo.")
            else:
                print("O grafo é conexo.")
        else:
            print("O grafo não é conexo.")

    def checar_componente_forte_conexao(self):
        """Verifica a quantidade de componentes fortemente conexos no grafo, considerando grafos direcionados."""
        if self.direcionado:
            print("Para verificar a quantidade de componentes fortemente conexos, é necessário implementar o algoritmo de Kosaraju.")
        else:
            print("Em grafos não direcionados, usamos componentes conexos em vez de componentes fortemente conexos.")


####################### Checagem de ponte e articulação #######################