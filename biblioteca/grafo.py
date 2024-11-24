class Grafo:
    def __init__(self, direcionado=False, num_vertices=0):
        self.direcionado = direcionado
        self.lista = {}
        self.rotulos_vertices = {}
        self.pesos_vertices = {}
        self.rotulos_arestas = {}
        self.pesos_arestas = {}
        self.num_vertices = 0

        for i in range(num_vertices):
            self.adicionar_vertice(str(i))
    
    def mapear_vertices_para_indices(self):
        return {vertice: idx for idx, vertice in enumerate(self.lista.keys())}
    
    def exibir_lista(self):
        print("Lista de Adjacência:")
        for vertice, adjacentes in self.lista.items():
            rotulo_vertice = self.rotulos_vertices.get(vertice, vertice)
            adjacentes_rotulados = [self.rotulos_vertices.get(v, v) for v in adjacentes]
            print(f"{rotulo_vertice}: {', '.join(adjacentes_rotulados)}")

    def exibir_matriz_adjacencia(self, direcionado=True):
        vertices = list(self.lista.keys())
        n = len(vertices)
        matriz = [[0 for _ in range(n)] for _ in range(n)]

        for i, u in enumerate(vertices):
            for v in self.lista[u]:
                j = vertices.index(v)
                matriz[i][j] = 1
                if not direcionado:
                    matriz[j][i] = 1

        print("Matriz de Adjacência:")
        print("   " + "  ".join([self.rotulos_vertices.get(v, v) for v in vertices]))
        for i, linha in enumerate(matriz):
            rotulo_vertice = self.rotulos_vertices.get(vertices[i], vertices[i])
            print(f"{rotulo_vertice:<3} " + "  ".join(map(str, linha)))

    def exibir_matriz_incidencia(self):
        arestas = []
        for u in self.lista:
            for v in self.lista[u]:
                if self.direcionado or (v, u) not in arestas:
                    arestas.append((u, v))

        self.matriz_incidencia = [[0] * len(arestas) for _ in range(self.num_vertices)]

        for j, (u, v) in enumerate(arestas):
            u_idx = list(self.lista.keys()).index(u)
            v_idx = list(self.lista.keys()).index(v)

            if self.direcionado:
                self.matriz_incidencia[u_idx][j] = -1
                self.matriz_incidencia[v_idx][j] = 1
            else:
                self.matriz_incidencia[u_idx][j] = 1
                self.matriz_incidencia[v_idx][j] = 1

        print("Matriz de Incidência:")

        arestas_rotuladas = [self.rotulos_arestas.get((u, v), f"{u}-{v}") for (u, v) in arestas]
        print("   " + "  ".join(arestas_rotuladas))  

        for i, linha in enumerate(self.matriz_incidencia):
            vertice = list(self.lista.keys())[i]
            rotulo_vertice = self.rotulos_vertices.get(vertice, vertice)
            print(f"{rotulo_vertice:<6} " + "  ".join(map(str, linha)))

    def adicionar_vertice(self, rotulo=None):
        vertice = str(self.num_vertices)
        self.lista[vertice] = []
        self.rotulos_vertices[vertice] = rotulo if rotulo else "sem rótulo"
        self.num_vertices += 1
        print(f"Vértice '{vertice}' adicionado.")
        
    def remover_vertice(self, rotulo=None):
            vertice = self.obter_vertice_por_rotulo(rotulo) if rotulo else None
            if vertice is None:
                print(f"Erro: Vértice com rótulo '{rotulo}' não encontrado.")
                return
            
            if vertice in self.lista:
                adjacentes = list(self.lista[vertice])  
                for v in adjacentes:
                    self.remover_aresta(self.rotulos_arestas.get((vertice, v), None) or self.rotulos_arestas.get((v, vertice), None))
               
                del self.lista[vertice]
                self.num_vertices -= 1
                for v in self.lista:
                    if vertice in self.lista[v]:
                        self.lista[v].remove(vertice)
                print(f"Vértice removido.")
            else:
                print(f"Vértice não existe.")

    def remover_aresta(self, rotulo):
        aresta = self.obter_aresta_por_rotulo(rotulo)
        if aresta is None:
            print(f"Erro: Aresta com rótulo '{rotulo}' não encontrada.")
            return

        u, v = aresta
        if v in self.lista[u]:
            self.lista[u].remove(v)
            if not self.direcionado:
                self.lista[v].remove(u)
            print(f"Aresta removida.")
        else:
            print(f"Aresta não existe.")
        
    def obter_vertice_por_rotulo(self, rotulo):
        for vertice, r in self.rotulos_vertices.items():
            if r == rotulo:
                return vertice
        return None
        
    def obter_vertice_por_rotulo(self, rotulo):
        for vertice, r in self.rotulos_vertices.items():
            if r == rotulo:
                return vertice
        return None
    
    def remover_aresta_por_vertices(self, u, v):
        # Verifica se os vértices existem
        if u not in self.lista or v not in self.lista:
            print(f"Erro: Vértice '{u}' ou '{v}' não encontrado.")
            return

        # Verifica se existe a aresta entre u e v
        if v in self.lista[u]:
            self.lista[u].remove(v)
            if not self.direcionado:
                self.lista[v].remove(u)
            print(f"Aresta removida entre '{u}' e '{v}'.")
        else:
            print(f"Aresta entre '{u}' e '{v}' não existe.")

    def obter_vertice_por_rotulo(self, rotulo):
        for vertice, r in self.rotulos_vertices.items():
            if r == rotulo:
                return vertice
        return None

    def adicionar_aresta(self, u, v, rotulo=None):
        if u not in self.lista and u not in self.rotulos_vertices:
            u = self.obter_vertice_por_rotulo(u)
        if v not in self.lista and v not in self.rotulos_vertices:
            v = self.obter_vertice_por_rotulo(v)
        
        if u not in self.lista or v not in self.lista:
            print(f"Erro: Vértice '{u}' ou '{v}' não existe. Aresta não pode ser adicionada.")
            return
        
        if v not in self.lista[u]:
            self.lista[u].append(v)
            if not self.direcionado:
                self.lista[v].append(u)

            if rotulo:
                self.rotulos_arestas[(u, v)] = rotulo
                if u not in self.rotulos_vertices:
                    self.rotulos_vertices[u] = rotulo
                if v not in self.rotulos_vertices:
                    self.rotulos_vertices[v] = rotulo

            print(f"Aresta adicionada entre '{u}' e '{v}' com rótulo '{rotulo}'.")
        else:
            print(f"Aresta entre '{u}' e '{v}' já existe.")
            
    def checar_adjacencia_vertices(self, u, v):
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
        if aresta1 not in self.rotulos_arestas.values() or aresta2 not in self.rotulos_arestas.values():
            print(f"As arestas '{aresta1}' ou '{aresta2}' não existem.")
            return False

        vertice1_1, vertice1_2 = next(((u, v) for (u, v), r in self.rotulos_arestas.items() if r == aresta1), (None, None))
        vertice2_1, vertice2_2 = next(((u, v) for (u, v), r in self.rotulos_arestas.items() if r == aresta2), (None, None))
        
        if vertice1_1 in [vertice2_1, vertice2_2] or vertice1_2 in [vertice2_1, vertice2_2]:
            print(f"As arestas '{aresta1}' e '{aresta2}' são adjacentes.")
            return True
        else:
            print(f"As arestas '{aresta1}' e '{aresta2}' não são adjacentes.")
            return False

    def checagem_aresta(self, origem, destino):
        return origem in self.lista and destino in self.lista[origem]

    def grau_do_vertice(self, vertice):
        if vertice not in self.lista:
            print(f"Vértice '{vertice}' não existe!")
            return None

        if not self.direcionado:
            return len(self.lista[vertice])
        else:
            grau_saida = len(self.lista[vertice])
            grau_entrada = sum(1 for v in self.lista if vertice in self.lista[v])
            return {"grau entrada": grau_entrada, "grau saida": grau_saida}

    def rotular_vertice(self, vertice, rotulo):
        self.rotulos_vertices[vertice] = rotulo
        print(f"Vértice '{vertice}' rotulado como '{rotulo}'.")

    def rotular_aresta(self, u, v, rotulo):
        if (u, v) in self.rotulos_arestas or (v, u) in self.rotulos_arestas:
            self.rotulos_arestas[(u, v)] = rotulo
            print(f"Aresta '{u}-{v}' rotulada como '{rotulo}'.")
        else:
            print(f"Aresta entre '{u}' e '{v}' não existe.")

    def ponderar_vertice(self, vertice, peso):
            self.pesos_vertices[vertice] = peso
            print(f"Vértice '{vertice}' ponderado com peso {peso}.")

    def obter_aresta_por_rotulo(self, rotulo):
        for (u, v), r in self.rotulos_arestas.items():
            if r == rotulo:
                return u, v
        print(f"Aresta com rótulo '{rotulo}' não encontrada.")
        return None

    def ponderar_aresta(self, rotulo, peso):
        aresta = self.obter_aresta_por_rotulo(rotulo)
        
        if aresta is not None:
            u, v = aresta
            
            if v in self.lista[u]:
                if not self.direcionado:
                    self.pesos_arestas[(u, v)] = peso
                    self.pesos_arestas[(v, u)] = peso
                else:
                    self.pesos_arestas[(u, v)] = peso
                print(f"Aresta entre '{u}' e '{v}' ponderada com peso {peso}.")
            else:
                print(f"Aresta entre '{u}' e '{v}' não existe. Não é possível atribuir peso.")
        else:
            print(f"Aresta com rótulo '{rotulo}' não encontrada.")

    def existe_aresta(self, rotulo_origem, rotulo_destino):
        """ Verifica se existe uma aresta de 'origem' para 'destino' usando rótulos """
        origem = self.rotulos_vertices.get(rotulo_origem)
        destino = self.rotulos_vertices.get(rotulo_destino)

        if origem and destino:
            if origem in self.lista:
                return destino in self.lista[origem]
        return False