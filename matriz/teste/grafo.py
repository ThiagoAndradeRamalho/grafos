from vertice import Vertice
from aresta import Aresta

class Grafo:

    def __init__(self, direcionado):
        self._lista_vertices = {}
        self._lista_arestas = []
        self._matriz_adjacencia = []
        self._matriz_incidencia = []
        self._lista_adjacentes = {}
        self._direcionado = direcionado
        self._vazio = True
        self._completo = False
        self._numComponentesConexos = 0

    @property
    def vertices(self):
        return {vertice.rotulo: vertice for vertice in self._lista_vertices}
    
    @property
    def arestas(self):
        return {str(aresta): aresta for aresta in self._lista_arestas}
    
    @property
    def direcionado(self):
        return self._direcionado
    
    @property
    def vazio(self):
        return len(self._lista_arestas) == 0
    
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
    
    def imprimir_vertices(self):
        for rotulo, vertice in self.vertices.items():
            print(vertice)
    
    def imprimir_lista_adjacentes(self):
        # Imprime as listas de adjacência
        for vertice, adjacentes in self._lista_adjacentes.items():
            print(f"Vértice {vertice}: {adjacentes}")

    def imprimir_matriz_adjacentes(self):
        self.set_matriz_adjacencia()
        print('Matriz de Adjacência')
        for i in range(len(self._matriz_adjacencia)):
            print(self._matriz_adjacencia[i])

    def imprimir_matriz_incidencia(self):
        matriz_incidencia = self.set_matriz_incidencia()
        for linha in matriz_incidencia:
            print(linha)

    def num_vertices(self):
        return len(self._lista_vertices)

    def num_arestas(self):
        return len(self._lista_arestas)

    def adjacentes(self, vertice):
        return [str(i) for i in self._lista_adjacentes[vertice]]
    
    def add_vertice(self, rotulo):
        if rotulo not in self._lista_vertices:
            self._lista_vertices[rotulo] = Vertice(rotulo)  # Usa o rótulo como chave
        else:
            print(f"Erro: vértice {rotulo} já existe.")


    # inicialmente pensei em toda vez que eu add uma aresta/vertice chamaria o set_lista_adjacentes, mas isso tornaria um codigo um pouco caro, ent toda vez que eu add, eu add tbm nas listas.
    # def add_aresta(self, origem, destino, peso):
    #     # Verifica se ambos os vértices estão presentes no grafo antes de adicionar a aresta
    #     if origem in [v.rotulo for v in self._lista_vertices] and destino in [v.rotulo for v in self._lista_vertices]:
    #         nova_aresta = Aresta(origem, destino, peso)
    #         self._lista_arestas.append(nova_aresta)  # Adiciona a aresta à lista de arestas
    #         self._lista_adjacentes[origem].append(destino)  # Atualiza a lista de adjacência
    #     else:
    #         print(f"Erro: vértice(s) {origem} ou {destino} não encontrado(s).")


    # add_aresta novo
    def add_aresta(self, origem, destino, peso):
        # Verifica se os vértices existem no grafo
        if origem in self._lista_vertices and destino in self._lista_vertices:
            nova_aresta = Aresta(origem, destino, peso)
            self._lista_arestas.append(nova_aresta)
            # Cria as entradas de adjacência caso ainda não existam
            if origem not in self._lista_adjacentes:
                self._lista_adjacentes[origem] = []
            if destino not in self._lista_adjacentes:
                self._lista_adjacentes[destino] = []
        else:
            print(f"Erro: vértice(s) {origem} ou {destino} não encontrado(s).")

    def remover_aresta(self, origem, destino):
        for chave, aresta in list(self.arestas.items()):
            if aresta.origem == origem and aresta.destino == destino:
                del self.arestas[chave]

                if origem in self._lista_adjacentes:
                    self._lista_adjacentes[origem].remove(destino)

                if not self._direcionado:
                    self._lista_adjacentes[destino].remove(origem)

                break
        return "Aresta {origem} {destino} não encontrada"



        # Cria um conjunto de arestas para otimizar a verificação de existência
        # aresta = (origem, destino)

        # if not self.aresta_existe(origem, destino):
        #     print(f"A aresta ({origem}, {destino}) não existe no grafo.")
        #     return

        # # Remove a aresta diretamente, criando uma nova lista sem a aresta a ser removida
        # self._lista_arestas = [a for a in self._lista_arestas if not (a.origem == origem and a.destino == destino)]
        # print(f"A aresta ({origem}, {destino}) foi removida com sucesso.")

    def set_lista_adjacentes(self):
        for rotulo, vertice in self._lista_vertices.items():
            self._lista_adjacentes[rotulo] = []

    def set_adjacentes(self):
        # Inicializa as listas de adjacência
        for rotulo in self._lista_vertices:
            self._lista_adjacentes[rotulo] = []

        if not self.direcionado:
            # Caso não seja direcionado, adiciona as arestas em ambos os sentidos
            for aresta in self._lista_arestas:
                # Adiciona as arestas para cada vértice
                self._lista_adjacentes[aresta.origem].append(aresta.destino)
                self._lista_adjacentes[aresta.destino].append(aresta.origem)
        else:
            # Caso seja direcionado, adiciona a aresta no sentido origem -> destino
            for aresta in self._lista_arestas:
                self._lista_adjacentes[aresta.origem].append(aresta.destino)

    def set_matriz_adjacencia(self):
        rotulos = list(self._lista_vertices.keys())  # Obtenha uma lista dos rótulos
        matriz = [[0] * len(rotulos) for _ in range(len(rotulos))]

        for aresta in self._lista_arestas:
            origem_idx = rotulos.index(aresta.origem)
            destino_idx = rotulos.index(aresta.destino)
            matriz[origem_idx][destino_idx] = 1

        self.matriz_adjacente = matriz
        
        def aresta_existe(self, o, d):
            for aresta in self.arestas.values():
                if aresta.origem == o and aresta.destino == d:
                    return True
        return False
    
    def set_matriz_incidencia(self):
        num_vertices = len(self.vertices)
        num_arestas = len(self.arestas)

        # Criação da matriz de incidência com zeros
        matriz_incidencia = [[0] * num_arestas for _ in range(num_vertices)]

        # Preenchendo a matriz com -1 e 1
        for i, (origem, destino) in enumerate(self.arestas):
            origem_idx = list(self.vertices.keys()).index(origem)
            destino_idx = list(self.vertices.keys()).index(destino)

            if self.direcionado:
                matriz_incidencia[origem_idx][i] = -1  # Origem da aresta
                matriz_incidencia[destino_idx][i] = 1  # Destino da aresta
            else:
                matriz_incidencia[origem_idx][i] = 1  # Origem da aresta
                matriz_incidencia[destino_idx][i] = 1  # Destino da aresta

        return matriz_incidencia
        
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

    def busca_profundidade(self, v):
        if v not in self.vertices:
            print(f"Erro: vértice {v} não encontrado.")
            return []

        t = 0
        for vertice in self.vertices.values():
            vertice._visitado = False
            vertice._pai = None
            vertice._tempo_descoberta = 0
            vertice._tempo_termino = 0

        ordem_visitados = []

        def dfs(vertice):
            nonlocal t
            t += 1
            vertice._visitado = True
            vertice._tempo_descoberta = t
            ordem_visitados.append(vertice.rotulo)

            if vertice.rotulo in self._lista_adjacentes:
                        for vizinho_rotulo in self._lista_adjacentes[vertice.rotulo]:
                            vizinho = self.vertices[vizinho_rotulo]
                            if not vizinho._visitado:
                                vizinho._pai = vertice
                                dfs(vizinho)

            t += 1
            vertice._tempo_termino = t

        vertice_inicial = self.vertices[v]
        dfs(vertice_inicial)

        return ordem_visitados
    

    #toda vez eu tinha que refazer um codigo de busca em profundidade pra poder usar em diferentes contexto




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

        vertices_visitados = set()  # Conjunto para armazenar vértices visitados
        n = 0  # Contador de componentes

        for v in self._lista_vertices:
            if v.rotulo not in vertices_visitados:
                # Chama a busca em profundidade e pega os vértices visitados
                visitados = self.busca_profundidade(v.rotulo)
                vertices_visitados.update(visitados)  # Marca todos os vértices como visitados
                n += 1  # Incrementa o contador de componentes

        return n
    
    def copiar_grafo(self):

        print('Criando a copia do grafo')

        novo_grafo = Grafo(self._direcionado)

        for v in self._lista_vertices:
            novo_grafo.add_vertice(v.rotulo)
            print(v)

        print('Criando as arestas da copia')
        
        for aresta in self._lista_arestas:
            novo_grafo.add_aresta(aresta.origem, aresta.destino, aresta.peso)
        
        return novo_grafo
    
    def ponte(self, origem, destino):

        ar = (origem, destino)

        nComponentes = self.num_componentes()

        print(nComponentes)

        g = self.copiar_grafo()

        g.remover_aresta(origem, destino)

        nNewComponentes = g.num_componentes()

        print(nNewComponentes)

        return nNewComponentes != nComponentes

    # def verificar_articulacao(self, vertice_remover):
    #     """ Verifica se a remoção de um vértice desconecta o grafo """
    #     # Copiar o grafo original para não alterar o grafo original
    #     grafo_copia = self.copiar_grafo()
        
    #     # Verificar se o vértice existe
    #     if vertice_remover not in [v.rotulo for v in grafo_copia._lista_vertices]:
    #         print(f"O vértice {vertice_remover} não existe no grafo.")
    #         return
        
    #     # Remover arestas associadas ao vértice
    #     grafo_copia._lista_arestas = [aresta for aresta in grafo_copia._lista_arestas
    #                                 if aresta.origem != vertice_remover and aresta.destino != vertice_remover]
        
    #     # Remover o vértice da lista de vértices
    #     grafo_copia._lista_vertices = [v for v in grafo_copia._lista_vertices if v.rotulo != vertice_remover]
        
    #     # Recriar a lista de adjacentes após a remoção
    #     grafo_copia.set_lista_adjacentes()
        
    #     # Verificar se o grafo copiado está conectado (usando DFS)
    #     vertices_visitados = set()
    
    # def dfs(v):
    #     vertices_visitados.add(v.rotulo)
    #     for vizinho in grafo_copia._lista_adjacentes[v.rotulo]:
    #         if vizinho not in vertices_visitados:
    #             # Encontra o vértice vizinho pelo rótulo diretamente
    #             vertice_vizinho = next((x for x in grafo_copia._lista_vertices if x.rotulo == vizinho), None)
    #             if vertice_vizinho:
    #                 dfs(vertice_vizinho)
    
    # # Iniciar a DFS a partir do primeiro vértice na lista
    # if grafo_copia._lista_vertices:
    #     dfs(grafo_copia._lista_vertices[0])

    # # Verificar se todos os vértices foram visitados
    # if len(vertices_visitados) == len(grafo_copia._lista_vertices):
    #     print("O grafo sem o vértice", vertice_remover, "continua conectado.")
    # else:
    #     print("O grafo sem o vértice", vertice_remover, "não está conectado.")




    def verificar_ponte(self, origem, destino):

        grafo_copia = self.copiar_grafo()
        
        grafo_copia.remover_aresta(origem, destino)

        # Verificar se todos os vértices foram visitados
        return grafo_copia.num_componentes() != self.num_componentes()


        
    



                
grafo = Grafo(direcionado=True)  # Se for direcionado, altere para True

# Adicionar Vértices
for v in ['v1', 'v2', 'v3', 'v4', 'v5']:
    grafo.add_vertice(v)

# Adicionar Arestas
arestas = [('v1', 'v2'), ('v2', 'v3'), ('v1', 'v3')]
pesos = [10, 20, 30]  # Exemplo de pesos para as arestas

for (origem, destino), peso in zip(arestas, pesos):
    grafo.add_aresta(origem, destino, peso)

# Adicionar Adjacentes
grafo.set_adjacentes()

print("Lista Adjacentes")
grafo.imprimir_lista_adjacentes()

print("Matriz Incidentes")
grafo.imprimir_matriz_incidencia()

print("Matriz Adjacentes")
grafo.imprimir_matriz_adjacentes()



# Imprimir Adjacentes para um Vértice Específico
print("Vértices adjacentes a v1:", grafo.adjacentes('v1'))

# Verificar se uma aresta existe
print("A aresta v1 -> v2 existe?", grafo.aresta_existe('v1', 'v2'))
print("A aresta v1 -> v4 existe?", grafo.aresta_existe('v1', 'v4'))

p = str(grafo.vazio)
print("Grafo vazio? "+p)

p = str(grafo.completo)
print("Grafo completo? "+p)

p = str(grafo.aresta_existe('v1', 'v2'))
print("Aresta v1 e v2 existe?", p)

print('BFS')
grafo.busca_largura('v1')

print('imprimindo vertices')
grafo.imprimir_vertices()

print('DFS')
n = grafo.busca_profundidade('v1')
print(n)

# componentes_fortemente_conexos = grafo.kosaraju()
# print("Componentes Fortemente Conexos:", componentes_fortemente_conexos)

# p = str(grafo.fortemente_conexo())
# print('Grafo Fortemente Conexo?',p)

# p = str(grafo.semi_fortemente_conexo())
# print('Grafo Semi Fortemente Conexo?',p)

p = str(grafo.num_componentes())
print('Nuemro componentes?',p)

# p = str(grafo.ponte('v1', 'v2'))
# print('A aresta é ponte?',p)

# p = str(grafo.ponte('v1', 'v2'))
# print('A aresta é ponte?',p)


p = grafo.verificar_ponte('v1','v3')
print("A aresta v1 v2 é ponte? ", p)