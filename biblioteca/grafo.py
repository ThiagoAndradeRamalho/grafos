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
            print(f"{vertice}: {', '.join(map(str, adjacentes))}")

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
        print("   " + "  ".join(map(str, vertices)))
        for i, linha in enumerate(matriz):
            print(f"{vertices[i]:<3} " + "  ".join(map(str, linha)))

    def exibir_matriz_incidencia(self):
        vertices = list(self.lista.keys())
        arestas = []
        
        for u in self.lista:
            for v in self.lista[u]:
                if self.direcionado:
                    arestas.append((u, v))
                elif (v, u) not in arestas:
                    arestas.append((u, v))
        
        rotulos_vertices = {vertice: self.rotulos_vertices.get(vertice, str(idx)) for idx, vertice in enumerate(vertices)}
        rotulos_arestas = {}
        
        for idx, (u, v) in enumerate(arestas):
            rotulo_u = self.rotulos_vertices.get(u, str(vertices.index(u)))
            rotulo_v = self.rotulos_vertices.get(v, str(vertices.index(v)))
            rotulo_aresta = self.rotulos_arestas.get((u, v), str(idx))
            rotulos_arestas[(u, v)] = rotulo_aresta

        print("Matriz de Incidência:")
        print("     " + "  ".join([rotulos_arestas[(u, v)] for u, v in arestas]))
        
        for vertice in vertices:
            linha = [0] * len(arestas)
            for idx, (u, v) in enumerate(arestas):
                if self.direcionado:
                    if u == vertice:
                        linha[idx] = 1
                    elif v == vertice:
                        linha[idx] = -1
                else:
                    if u == vertice or v == vertice:
                        linha[idx] = 1
            print(f"{rotulos_vertices[vertice]:<4} " + "  ".join(map(str, linha)))

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
        if rotulo:
            for (origem, destino), r in list(self.rotulos_arestas.items()):
                if r == rotulo:
                    self.lista[origem].remove(destino)
                    if not self.direcionado:
                        self.lista[destino].remove(origem)
                    del self.rotulos_arestas[(origem, destino)]
                    print(f"Aresta com rótulo '{rotulo}' removida entre '{origem}' e '{destino}'.")
                    return
            print(f"Aresta com rótulo '{rotulo}' não encontrada.")
        elif u and v:
            if u in self.lista and v in self.lista[u]:
                self.lista[u].remove(v)
                if not self.direcionado:
                    self.lista[v].remove(u)
                self.rotulos_arestas.pop((u, v), None)
                print(f"Aresta removida entre '{u}' e '{v}'.")
            else:
                print(f"Aresta entre '{u}' e '{v}' não existe.")
        else:
            print("Erro: Especifique os vértices ou o rótulo da aresta a ser removida.")
    
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
