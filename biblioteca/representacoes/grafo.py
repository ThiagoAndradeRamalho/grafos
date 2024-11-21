class Grafo:
    def __init__(self, num_vertices, direcionado):
        self.num_vertices = num_vertices
        self.direcionado = direcionado
        self.lista = [[] for _ in range(num_vertices)]

    def adicionar_aresta(self, u, v):
        max_index = max(u, v)
        while len(self.lista) <= max_index:
            self.lista.append([])

        self.lista[u].append(v)
        if not self.direcionado:
            self.lista[v].append(u)

    def remover_aresta(self, u, v):
        if v in self.lista[u]:
            self.lista[u].remove(v)
            print(f"Aresta removida: {u} -> {v}")

        if not self.direcionado and u in self.lista[v]:
            self.lista[v].remove(u)
            print(f"Aresta removida: {v} -> {u}")

    def duplicar_grafo(self):
        novo_grafo = Grafo(self.num_vertices, self.direcionado)
        for u in range(self.num_vertices):
            for v in self.lista[u]:
                novo_grafo.adicionar_aresta(u, v)
        return novo_grafo

    def grau(self, v):
        if not self.direcionado:
            return len(self.lista[v])
        else:
            grau_saida = len(self.lista[v])
            grau_entrada = sum(1 for u in range(self.num_vertices) if v in self.lista[u])
            return grau_entrada, grau_saida

    def exibir_lista(self):
        for i in range(len(self.lista)):
            print(f"{i}: {self.lista[i]}")

    def exibir_matriz_adjacencia(self):
        matriz = [[0] * len(self.lista) for _ in range(len(self.lista))]
        
        for u in range(len(self.lista)):
            for v in self.lista[u]:
                matriz[u][v] = 1
                if not self.direcionado:
                    matriz[v][u] = 1
        
        print("Matriz de Adjacência:")
        for linha in matriz:
            print(" ".join(map(str, linha)))

    def exibir_matriz_incidencia(self):
        arestas = []
        for u in range(len(self.lista)):
            for v in self.lista[u]:
                if not self.direcionado and (v, u) in arestas:
                    continue
                arestas.append((u, v))

        matriz = [[0] * len(arestas) for _ in range(len(self.lista))]
        
        for i, (u, v) in enumerate(arestas):
            matriz[u][i] = 1
            if not self.direcionado:
                matriz[v][i] = 1
        
        print("Matriz de Incidência:")
        for linha in matriz:
            print(" ".join(map(str, linha)))
