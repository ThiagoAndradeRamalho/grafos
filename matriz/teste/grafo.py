from vertice import Vertice
from aresta import Aresta

class Grafo:

    def __init__(self, direcionado):
        self._lista_vertices = []
        self._lista_arestas = []
        self._matriz_adjacencia = []
        self._matriz_incidencia = []
        self._lista_adjacentes = {}
        self._direcionado = direcionado
        self._vazio = True
        self._completo = False
        self._numComponentesConexos = 0
        self.num_Componentes = 0

    @property
    def vertices(self):
        return [str(vertice) for vertice in self._lista_vertices]    
    
    @property
    def arestas(self):
        return [str(areresta) for areresta in self._lista_arestas]
    
    @property
    def direcionado(self):
        return self._direcionado
    
    @property
    def vazio(self):
        self._vazio = len(self._lista_arestas) == 0
        return self._vazio
    
    @property
    def completo(self):
        nA = len(self.arestas)
        nV = len(self.vertices)

        if not self.direcionado:        
            a = (nV * (nV - 1)) / 2
        else:
            a = nV * (nV - 1)

        if a == nA:
            self._completo = True
        return self._completo
    
    def imprimir_lista_adjacentes(self):
        self.set_adjacentes()
        print('Lista de Adjacência')
        for vertice, adjacentes in self._lista_adjacentes.items():
            print(f'Vertice {vertice}: {adjacentes}')

    def imprimir_matriz_adjacentes(self):
        self.set_matriz_adjacencia()
        print('Matriz de Adjacência')
        for i in range(len(self._matriz_adjacencia)):
            print(self._matriz_adjacencia[i])

    def imprimir_matriz_incidencia(self):
        self.set_matriz_incidencia()
        print('Matriz de Incidencia')
        for i in range(len(self._matriz_incidencia)):
            print(self._matriz_incidencia[i])

    def imprimir_vertices(self):
        for v in self._lista_vertices:
            print(v.rotulo)

    def imprimir_arestas(self):
        for a in self._lista_arestas:
            print("Origem " + a.origem + " Destino " + a.destino)

    def num_vertices(self):
        return len(self._lista_vertices)

    def num_arestas(self):
        return len(self._lista_arestas)

    def adjacentes(self, vertice):
        return [str(i) for i in self._lista_adjacentes[vertice]]
    
    def add_vertice(self, vertice):
        # Se o 'vertice' for um objeto da classe 'Vertice', adiciona ele
        if isinstance(vertice, Vertice):
            self._lista_vertices.append(vertice)
            self._lista_adjacentes[vertice.rotulo] = []
        # Se o 'vertice' for um rótulo (string), cria um objeto 'Vertice' e adiciona
        elif isinstance(vertice, str):
            novo_vertice = Vertice(vertice)
            self._lista_vertices.append(novo_vertice)
            self._lista_adjacentes[novo_vertice.rotulo] = []
        else:
            print("Erro: O parâmetro vertice deve ser um objeto Vertice ou uma string.")

    def add_aresta(self, origem, destino, peso):
        # Verifica se ambos os vértices estão presentes no grafo antes de adicionar a aresta
        if origem in [v.rotulo for v in self._lista_vertices] and destino in [v.rotulo for v in self._lista_vertices]:
            nova_aresta = Aresta(origem, destino, peso)
            self._lista_arestas.append(nova_aresta)  # Adiciona a aresta à lista de arestas
            self._lista_adjacentes[origem].append(destino)  # Atualiza a lista de adjacência
        else:
            print(f"Erro: vértice(s) {origem} ou {destino} não encontrado(s).")

    def remover_aresta(self, origem, destino):

        if not self.aresta_existe(origem, destino):
            print(f"A aresta ({origem}, {destino}) não existe no grafo.")
            return

        # Remove a aresta diretamente, criando uma nova lista sem a aresta a ser removida
        self._lista_arestas = [a for a in self._lista_arestas if not (a.origem == origem and a.destino == destino)]

        self._lista_adjacentes[origem].remove(destino)
        print(f"A aresta ({origem}, {destino}) foi removida com sucesso.")

    def remover_vertice(self, v):
        if v not in self._lista_vertices:
            print('Vertice {v} nao existe')

        for a in self._lista_arestas:
            if a.origem == v or a.destino == v:
                self.remover_aresta(a.origem, a.destino)

        for vertice in self._lista_vertices:
            if vertice.rotulo == v:
                self._lista_vertices.remove(vertice)
                break
        
        del self._lista_adjacentes[v]

        self.imprimir_lista_adjacentes()

        print('Vertice ', v ,' removido com sucesso')

    def set_lista_adjacentes(self):
        for i in self._lista_vertices:
            self._lista_adjacentes[i.rotulo] = []

    def set_adjacentes(self):
        if not self.direcionado:
            for vertice in self._lista_vertices:
                for aresta in self._lista_arestas:
                    if vertice.rotulo == aresta.origem:
                        self._lista_adjacentes[vertice.rotulo].append(aresta.destino)
                    elif vertice.rotulo == aresta.destino:
                        self._lista_adjacentes[vertice.rotulo].append(aresta.origem)
        else:
            for vertice in self._lista_vertices:
                for aresta in self._lista_arestas:
                    if vertice.rotulo == aresta.origem:
                        self._lista_adjacentes[vertice.rotulo].append(aresta.destino)

    def set_matriz_adjacencia(self):
        n = len(self._lista_vertices)
        rotulos = [v.rotulo for v in self._lista_vertices]
        self._matriz_adjacencia = [[0] * n for _ in range(n)]
        for aresta in self._lista_arestas:
            i = rotulos.index(aresta.origem)
            j = rotulos.index(aresta.destino)

            self._matriz_adjacencia[i][j] = aresta.peso

            if not self.direcionado:
                self._matriz_adjacencia[j][i] = aresta.peso

        return self._matriz_adjacencia
    
    def aresta_existe(self, o, d):
        for aresta in self._lista_arestas:
            if aresta.origem == o and aresta.destino == d:
                return True
        return False
    
    def vertice_existe(self, v):
        for vertice in self._lista_vertices:
            if v == vertice.rotulo:
                return vertice
        return False
    
    def set_matriz_incidencia(self):
        nV = self.num_vertices()
        nA = self.num_arestas()
        rotulos = [v.rotulo for v in self._lista_vertices]
        self._matriz_incidencia = [[0] * nV for _ in range(nA)]

        for x, aresta in enumerate(self._lista_arestas):
            i = rotulos.index(aresta.origem)
            j = rotulos.index(aresta.destino)

            if not self._direcionado:
                self._matriz_incidencia[x][j] = 1
                self._matriz_incidencia[x][i] = 1
            else:
                self._matriz_incidencia[x][j] = 1
                self._matriz_incidencia[x][i] = -1

        return self._matriz_incidencia
    
    def busca_largura(self, vInicial):

        if vInicial not in [v.rotulo for v in self._lista_vertices]:
            print(f"O vértice {vInicial} não existe no grafo.")
            return

        mapa_vertices = {v.rotulo: v for v in self._lista_vertices}

        lista = []
        t = 1

        for v in self._lista_vertices:
            v._indice = 0
            v._nivel = -1
            v._pai = None

        vertice_inicial = mapa_vertices[vInicial]
        vertice_inicial._indice = t
        vertice_inicial._nivel = 0
        lista.append(vertice_inicial)

        while lista:
            v = lista.pop(0)

            for vizinho in self._lista_adjacentes[v.rotulo]:
                w = mapa_vertices[vizinho]

                if w._indice == 0:
                    t += 1
                    w._indice = t
                    w._nivel = v._nivel + 1
                    w._pai = v.rotulo
                    lista.append(w)

        for v in self._lista_vertices:
            print(f"Vértice {v.rotulo}: índice={v._indice}, nível={v._nivel}, pai={v._pai}")
    
    # def busca_profundidade(self, vInicial):

    #     if vInicial not in [v.rotulo for v in self._lista_vertices]:
    #         print(f"O vértice {vInicial} não existe no grafo.")
    #         return
        
    #     mapa_vertices = {v.rotulo: v for v in self._lista_vertices}

    #     t = 0

    #     for v in self._lista_vertices:
    #         v._tempo_descoberta = 0
    #         v._tempo_termino = 0
    #         v._pai = None

    #     def dfs_recursivo(v):
    #         nonlocal t
    #         t += 1
    #         v._tempo_descoberta = t

    #         for vizinho in self._lista_adjacentes[v.rotulo]:
    #             w = mapa_vertices[vizinho]

    #             if w._tempo_descoberta == 0:
    #                 w._pai = v.rotulo
    #                 dfs_recursivo(w)
            
    #         t +=1
    #         v._tempo_termino = t
           
    #     dfs_recursivo(mapa_vertices[vInicial])
            
    #     for v in self._lista_vertices:
    #         print(f"Vértice {v.rotulo}: descoberta={v._tempo_descoberta}, término={v._tempo_termino}, pai={v._pai}")

    # def busca_profundidade(self, vInicial):
    #     if vInicial not in [v.rotulo for v in self._lista_vertices]:
    #         print(f"O vértice {vInicial} não existe no grafo.")
    #         return
        
    #     mapa_vertices = {v.rotulo: v for v in self._lista_vertices}
    #     vertices_visitados = set()  # Agora o conjunto de visitados está dentro da função

    #     def dfs_recursivo(v):
    #         vertices_visitados.add(v.rotulo)  # Marca o vértice como visitado
    #         for vizinho in self._lista_adjacentes[v.rotulo]:
    #             if vizinho not in vertices_visitados:
    #                 dfs_recursivo(mapa_vertices[vizinho])

    #     # Inicia a DFS recursiva a partir do vértice inicial
    #     dfs_recursivo(mapa_vertices[vInicial])

    #     return vertices_visitados  # Retorna os vértices visitados

    def busca_profundidade(self, vInicial):
        # Cria o dicionário de vértices com o rótulo como chave
        mapa_vertices = {v.rotulo: v for v in self._lista_vertices}
        
        # Verifica se o vértice inicial está no mapa de vértices
        if vInicial not in mapa_vertices:
            print(f"Erro: {vInicial} não está em mapa_vertices.")
            print(f"Rótulos de vértices disponíveis: {list(mapa_vertices.keys())}")
            return False

        t = 0
        # n = 0
        ordem_visitados = []

        # Inicializa os vértices antes da busca
        for vertice in self._lista_vertices:
            vertice._visitado = False
            vertice._pai = None
            vertice._tempo_descoberta = 0
            vertice._tempo_termino = 0

        # Função recursiva para DFS
        def dfs(vertice):
            nonlocal t
            # nonlocal n
            # if vertice._pai == None:
            #     n += 1
            
            t += 1
            vertice._visitado = True
            vertice._tempo_descoberta = t
            ordem_visitados.append(vertice.rotulo)

            # Processa os vizinhos do vértice
            for vizinho in self._lista_adjacentes[vertice.rotulo]:
                if not mapa_vertices[vizinho]._visitado:
                    mapa_vertices[vizinho]._pai = vertice
                    dfs(mapa_vertices[vizinho])

            t += 1
            vertice._tempo_termino = t

        # Começa a busca a partir do vértice inicial
        vertice_inicial = mapa_vertices[vInicial]
        dfs(vertice_inicial)

        # self.num_Componentes = n
        # print("Numero c: "+ self.num_Componentes)
        return ordem_visitados






    def grafo_transposto(self):
        grafo_invertido = Grafo(direcionado=True)
        grafo_invertido.add_vertice([v.rotulo for v in self._lista_vertices])

        grafo_invertido.set_lista_adjacentes()

        for aresta in self._lista_arestas:
            grafo_invertido.add_aresta(aresta.destino, aresta.origem, aresta.peso)
        
        return grafo_invertido


    def kosaraju(self):
        lista_termino = []

        def dfs_ordem(v):
            nonlocal lista_termino
            self.busca_profundidade(v)
            ordem_termino = sorted(self._lista_vertices, key=lambda x: x._tempo_termino, reverse=True)

        for vertice in self._lista_vertices:
            vertice._visitado = False

        for vertice in self._lista_vertices:
            if vertice._tempo_descoberta == 0:
                dfs_ordem(vertice.rotulo)

        transposto = self.grafo_transposto()

        componentes = []

        

        mapa_vertices_invertido = {v.rotulo: v for v in transposto._lista_vertices}

        def dfs_componentes(v, componente):
            v_visitado = True
            componentes.append(v.rotulo)
            for vizinho in transposto._lista_adjacentes[v.rotulo]:
                w = mapa_vertices_invertido[vizinho]
                if not w._visitado:
                    dfs_componentes(w, componente)

        for vertice in transposto._lista_vertices:
            vertice._visitado = False
        
        for v in lista_termino:
            atual = []

            if not mapa_vertices_invertido[v.rotulo]._visitado:
                dfs_componentes(mapa_vertices_invertido[v.rotulo], atual)
                componentes.append(atual)
        

        return componentes
    
    def grafo_subjacente(self):

        self._lista_adjacentes.clear()

        for v in self._lista_vertices:
            self._lista_adjacentes[v.rotulo] = set()
            
        for aresta in self._lista_arestas:
            self._lista_adjacentes[aresta.origem].add(aresta.destino)
            self._lista_adjacentes[aresta.destino].add(aresta.origem)



    def fortemente_conexo(self):
        return len(self.kosaraju()) == 1

    def semi_fortemente_conexo(self):

        if self._direcionado:
            self.grafo_subjacente()

        vertices_visitados = set()

        def busca(v):
            vertices_visitados.add(v)
            for vizinho in self._lista_adjacentes[v]:
                if vizinho not in vertices_visitados:
                    busca(vizinho)

        v = next(iter((self._lista_adjacentes)))
        busca(v)

        return len(vertices_visitados) == len(self._lista_vertices)

        # for aresta in self._lista_arestas:
        #     if aresta.origem not in vertices_visitados:
        #         vertices_visitados.append(aresta.origem)
        #     elif aresta.destino not in vertices_visitados:
        #         vertices_visitados.append(aresta.destino)

        # return len(vertices_visitados) == self.num_vertices()  

#         explicação do porque nao utilizei essa função, apezar de parecer mais otimizada:
#         A função que você criou verifica os vértices visitados ao percorrer as arestas, mas ela pode não capturar a conexão completa entre os vértices. Além disso, ela não garante que todos os vértices estejam realmente acessíveis entre si, uma característica essencial para um grafo semi-fortemente conexo. Então, apesar de ser mais simples e com menor complexidade, essa abordagem pode levar a resultados incorretos em alguns casos.

# A nova versão, que converte o grafo em um grafo não-direcionado e usa busca em profundidade (DFS) para verificar conectividade, garante que todos os vértices estejam conectados diretamente ou indiretamente. Isso resulta em maior precisão, embora exija mais operações devido à DFS.

    def simplesmente_conexo(self):

        if self._direcionado:
            self.grafo_subjacente()

    def num_componentes(self):
        self.num_Componentes = 0

        for vertice in self._lista_vertices:
            if not vertice._visitado:
                self.busca_profundidade(vertice.rotulo)
                self.num_Componentes += 1  

        return self.num_Componentes
    
    def copiar_grafo(self):
        grafo_copiado = Grafo(self.direcionado)

        # Copiar os vértices
        for vertice in self._lista_vertices:
            grafo_copiado.add_vertice(vertice)
            

        print("n ",grafo_copiado.imprimir_vertices())

        # Copiar as arestas
        for aresta in self._lista_arestas:
            grafo_copiado.add_aresta(aresta.origem, aresta.destino, aresta.peso)


        return grafo_copiado
    
    def ponte(self, origem, destino):

        if not self.aresta_existe(origem, destino):
            print('Aresta não existe')

        nComponentes = self.num_componentes()

        g = self.copiar_grafo()

        g.remover_aresta(origem, destino)

        g.imprimir_arestas()
        
        g.imprimir_lista_adjacentes()

        nNewComponentes = g.num_componentes()

        print(nNewComponentes)

        return nNewComponentes != nComponentes
    
    def articulacao(self, v):
        if not self.vertice_existe(v):
            print("Vertice {v} não existe")

        g = self.copiar_grafo()

        g.remover_vertice(v)

        return g.num_componentes() != self.num_componentes()



        
    



                
grafo = Grafo(direcionado=True)  # Se for direcionado, altere para True

# Adicionar Vértices
vertices = ['v1', 'v2', 'v3', 'v4', 'v5']

for v in vertices:
 grafo.add_vertice(v)

grafo.set_lista_adjacentes()

# Adicionar Arestas
arestas = [('v1', 'v2'), ('v2', 'v3'), ('v3', 'v4')]
pesos = [10, 20, 30]  # Exemplo de pesos para as arestas

for (origem, destino), peso in zip(arestas, pesos):
    grafo.add_aresta(origem, destino, peso)




# Adicionar Adjacentes
grafo.set_adjacentes()

grafo.imprimir_lista_adjacentes()

grafo.imprimir_matriz_adjacentes()

grafo.imprimir_matriz_incidencia()

# Imprimir Adjacentes para um Vértice Específico
print("Vértices adjacentes a v1:", grafo.adjacentes('v1'))

# Verificar se uma aresta existe
print("A aresta v1 -> v2 existe?", grafo.aresta_existe('v1', 'v2'))
print("A aresta v1 -> v4 existe?", grafo.aresta_existe('v1', 'v4'))

p = str(grafo.vazio)
print("Grafo vazio? "+p)

p = str(grafo.completo)
print("Grafo completo? "+p)


print('BFS')
grafo.busca_largura('v1')

print('DFS')
p = grafo.busca_profundidade('v1')
print(p)

componentes_fortemente_conexos = grafo.kosaraju()
print("Componentes Fortemente Conexos:", componentes_fortemente_conexos)

p = str(grafo.fortemente_conexo())
print('Grafo Fortemente Conexo?',p)

p = str(grafo.semi_fortemente_conexo())
print('Grafo Semi Fortemente Conexo?',p)

p = str(grafo.num_componentes())
print('Nuemro componentes?',p)

p = str(grafo.ponte('v1', 'v2'))
print('A aresta é ponte?',p)

p = str(grafo.articulacao('v2'))
print('O vertice é articulação?',p)
