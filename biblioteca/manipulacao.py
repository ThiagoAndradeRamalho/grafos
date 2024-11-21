# Este módulo será responsável pelas operações de manipulação e consulta dos grafos.


from representacoes.lista_adjacencia import GrafoListaAdjacencia
from representacoes.matriz_adjacencia import GrafoMatrizAdjacencia
from representacoes.matriz_incidencia import GrafoMatrizIncidencia

rotulos_vertices = {}
rotulos_arestas = {}
pesos_vertices = {}
pesos_arestas = {}

def rotular_vertice(grafo, vertice, rotulo):
    if grafo not in rotulos_vertices:
        rotulos_vertices[grafo] = {}

    rotulos_vertices[grafo][vertice] = rotulo
    
    
def obter_rotulo_vertice(grafo, vertice):
    if grafo in rotulos_vertices and vertice in rotulos_vertices[grafo]:
        return rotulos_vertices[grafo][vertice]
    else:
        return None
    
def rotular_aresta(grafo, u, v, rotulo):
    if grafo not in rotulos_arestas:
        rotulos_arestas[grafo] = {}

    rotulos_arestas[grafo][(u, v)] = rotulo

def ponderar_vertice(grafo, vertice, peso):
    if grafo not in pesos_vertices:
        pesos_vertices[grafo] = {}

    pesos_vertices[grafo][vertice] = peso
    print(f"Vértice {vertice} ponderado com peso '{peso}'.") #passar p mmain dps
    
def ponderar_aresta(grafo, u, v, peso):
    if grafo not in pesos_arestas:
        pesos_arestas[grafo] = {}

    pesos_arestas[grafo][(u, v)] = peso
    print(f"Aresta entre {u} e {v} ponderada com peso '{peso}'.") #passar p mmain dps

                
def checar_adjacencia_vertices(grafo, u, v):
    if isinstance(grafo, GrafoMatrizAdjacencia):
        return grafo.matriz[u][v] != 0
    elif isinstance(grafo, GrafoListaAdjacencia):
        return v in grafo.lista[u]
    elif isinstance(grafo, GrafoMatrizIncidencia):
        for aresta in range(len(grafo.matriz[0])):
            if grafo.matriz[u][aresta] != 0 and grafo.matriz[v][aresta] != 0:
                return True
        return False
    else:
        print("Tipo de grafo desconhecido.")
        return False


def checar_adjacencia_arestas(grafo, u, v):
    if isinstance(grafo, GrafoListaAdjacencia):
        return v in grafo.lista[u]
    
    elif isinstance(grafo, GrafoMatrizAdjacencia):
        return grafo.matriz[u][v] != 0
    
    elif isinstance(grafo, GrafoMatrizIncidencia):
        for aresta in range(len(grafo.matriz[0])):
            if grafo.matriz[u][aresta] != 0 and grafo.matriz[v][aresta] != 0:
                return True
        return False
    else:
        print("Tipo de grafo desconhecido.")
        return False
        
        
def existe_aresta(grafo, v, u):
    if isinstance(grafo, GrafoMatrizAdjacencia):
        return grafo.matriz[u][v] != 0
    elif isinstance(grafo, GrafoListaAdjacencia):
        return v in grafo.lista[u]
    elif isinstance(grafo, GrafoMatrizIncidencia):
        for aresta in range(len(grafo.matriz[0])):
            if grafo.matriz[u][aresta] != 0 and grafo.matriz[v][aresta] != 0:
                return True
        return False

def quantidade_vertices(grafo):
    if isinstance(grafo, GrafoMatrizAdjacencia):
        return len(grafo.matriz)  # num de vertices = o tamanho da matriz
    
    elif isinstance(grafo, GrafoListaAdjacencia):
        return len(grafo.lista)  # num de vertices = o tamanho da lista de adjacência
    
    elif isinstance(grafo, GrafoMatrizIncidencia):
        return len(grafo.matriz)  # num de vertices = o num de linhas na matriz de incidência
    
    else:
        print("Tipo de grafo desconhecido.")
        return 0

def quantidade_arestas(grafo):
    if isinstance(grafo, GrafoMatrizAdjacencia):
        return sum(1 for i in range(len(grafo.matriz)) for j in range(i, len(grafo.matriz)) if grafo.matriz[i][j] != 0)
    elif isinstance(grafo, GrafoListaAdjacencia):
        return sum(len(adjacentes) for adjacentes in grafo.lista) // 2    
    elif isinstance(grafo, GrafoMatrizIncidencia):
        return len(grafo.matriz[0])
    else:
        print("Tipo de grafo desconhecido.")
        return 0

def grafo_vazio(grafo):
    return quantidade_arestas(grafo) == 0

def grafo_completo(grafo):
    if isinstance(grafo, GrafoMatrizAdjacencia):
        n = len(grafo.matriz)  
        return all(grafo.matriz[i][j] != 0 for i in range(n) for j in range(i + 1, n))
    
    elif isinstance(grafo, GrafoListaAdjacencia):
        n = len(grafo.lista)  
        # verifica se cada vertice ta conectado a todos os outros vertices
        return all(len(grafo.lista[v]) == n - 1 for v in grafo.lista)
    
    elif isinstance(grafo, GrafoMatrizIncidencia):
        n = len(grafo.matriz)  
        max_arestas = n * (n - 1) // 2  # max de arestas em um grafo completo
        return quantidade_arestas(grafo) == max_arestas
    
    else:
        print("Tipo de grafo desconhecido.")
        return False
    
    

def exibir_vertices(grafo):
    num_vertices = quantidade_vertices(grafo)
    print(f"Vértices do grafo ({num_vertices} no total):")
    if isinstance(grafo, GrafoMatrizAdjacencia) or isinstance(grafo, GrafoMatrizIncidencia):
        for i in range(num_vertices):
            rotulo = rotulos_vertices.get(grafo, {}).get(i, "sem rótulo")
            peso = pesos_vertices.get(grafo, {}).get(i, "sem peso")
            print(f"Vértice {i} (Rótulo: {rotulo}, Peso: {peso})")
    elif isinstance(grafo, GrafoListaAdjacencia):
        for vertice in range(num_vertices): 
            rotulo = rotulos_vertices.get(grafo, {}).get(vertice, "sem rótulo")
            peso = pesos_vertices.get(grafo, {}).get(vertice, "sem peso")
            print(f"Vértice {vertice} (Rótulo: {rotulo}, Peso: {peso})")


def exibir_arestas(grafo):
    print("Arestas do grafo:")
    if isinstance(grafo, GrafoMatrizAdjacencia):
        for i in range(len(grafo.matriz)):
            for j in range(i, len(grafo.matriz[i])):
                if grafo.matriz[i][j] != 0:
                    rotulo = rotulos_arestas.get(grafo, {}).get((i, j), "sem rótulo")
                    peso = pesos_arestas.get(grafo, {}).get((i, j), "sem peso")
                    print(f"Aresta entre {i} e {j} (Rótulo: {rotulo}, Peso: {peso})")
    elif isinstance(grafo, GrafoListaAdjacencia):
        for u in range(grafo.num_vertices):
            for v in grafo.lista[u]:
                if u < v:  
                    rotulo = rotulos_arestas.get(grafo, {}).get((u, v), "sem rótulo")
                    peso = pesos_arestas.get(grafo, {}).get((u, v), "sem peso")
                    print(f"Aresta entre {u} e {v} (Rótulo: {rotulo}, Peso: {peso})")
    elif isinstance(grafo, GrafoMatrizIncidencia):
        for e in range(len(grafo.matriz[0])):
            vertices_conectados = [v for v in range(len(grafo.matriz)) if grafo.matriz[v][e] != 0]
            if len(vertices_conectados) == 2:
                u, v = vertices_conectados
                rotulo = rotulos_arestas.get(grafo, {}).get((u, v), "sem rótulo")
                peso = pesos_arestas.get(grafo, {}).get((u, v), "sem peso")
                print(f"Aresta entre {u} e {v} (Rótulo: {rotulo}, Peso: {peso})")


def dfs(grafo, v, visitado):
    if isinstance(grafo, GrafoMatrizAdjacencia):
        visitado[v] = True
        for vizinho in range(grafo.num_vertices):
            if grafo.matriz[v][vizinho] != 0 and not visitado[vizinho]:
                dfs(grafo, vizinho, visitado)

    elif isinstance(grafo, GrafoListaAdjacencia):
        visitado[v] = True
        for vizinho in grafo.lista[v]:
            if not visitado[vizinho]:
                dfs(grafo, vizinho, visitado)

    elif isinstance(grafo, GrafoMatrizIncidencia):
        visitado[v] = True
        for aresta in range(len(grafo.matriz[0])):
            if grafo.matriz[v][aresta] != 0:  # Se está conectado pela aresta
                for vizinho in range(grafo.num_vertices):
                    if (
                        vizinho != v
                        and grafo.matriz[vizinho][aresta] != 0
                        and not visitado[vizinho]
                    ):
                        dfs(grafo, vizinho, visitado)

    else:
        raise TypeError("Tipo de grafo não suportado para DFS.")



def kosaraju(self):
    if isinstance(self, GrafoListaAdjacencia):
        def dfs(grafo, vertice, visitados, stack=None):
            visitados[vertice] = True
            for vizinho in grafo.lista[vertice]:
                if not visitados[vizinho]:
                    dfs(grafo, vizinho, visitados, stack)
            if stack is not None:
                stack.append(vertice)  # Empilha o vértice após explorar seus vizinhos

        def construir_reverso(grafo):
            grafo_reverso = GrafoListaAdjacencia(grafo.num_vertices, grafo.direcionado)
            for u in range(grafo.num_vertices):
                for v in grafo.lista[u]:
                    grafo_reverso.adicionar_aresta(v, u)  # Inverte as arestas
            return grafo_reverso

        # Passo 1: Fazer busca em profundidade (DFS) e salvar tempos de término
        visitados = [False] * self.num_vertices
        stack = []
        for v in range(self.num_vertices):
            if not visitados[v]:
                dfs(self, v, visitados, stack)

        # Passo 2: Construir o grafo reverso
        grafo_reverso = construir_reverso(self)

        # Passo 3: Fazer DFS no grafo reverso em ordem decrescente de tempos de término
        visitados = [False] * grafo_reverso.num_vertices
        cfc = []  # Lista para armazenar os componentes fortemente conectados
        while stack:
            v = stack.pop()
            if not visitados[v]:
                componente = []
                dfs(grafo_reverso, v, visitados, componente)
                cfc.append(componente)

        return cfc
    
    elif isinstance(self, GrafoMatrizAdjacencia):
        def dfs_matriz_adjacencia(grafo, vertice, visitados, stack=None):
            visitados[vertice] = True
            for vizinho in range(grafo.num_vertices):
                if grafo.matriz[vertice][vizinho] != 0 and not visitados[vizinho]:
                    dfs_matriz_adjacencia(grafo, vizinho, visitados, stack)
            if stack is not None:
                stack.append(vertice)

        def construir_reverso_matriz_adjacencia(grafo):
            grafo_reverso = GrafoMatrizAdjacencia(grafo.num_vertices, grafo.direcionado)
            for u in range(grafo.num_vertices):
                for v in range(grafo.num_vertices):
                    if grafo.matriz[u][v] != 0:
                        grafo_reverso.matriz[v][u] = grafo.matriz[u][v]
            return grafo_reverso

        # Passo 1: Fazer DFS e salvar tempos de término
        visitados = [False] * self.num_vertices
        stack = []
        for v in range(self.num_vertices):
            if not visitados[v]:
                dfs_matriz_adjacencia(self, v, visitados, stack)

        # Passo 2: Construir o grafo reverso
        grafo_reverso = construir_reverso_matriz_adjacencia(self)

        # Passo 3: Fazer DFS no grafo reverso
        visitados = [False] * grafo_reverso.num_vertices
        cfc = []
        while stack:
            v = stack.pop()
            if not visitados[v]:
                componente = []
                dfs_matriz_adjacencia(grafo_reverso, v, visitados, componente)
                cfc.append(componente)

        return cfc

    elif isinstance(self, GrafoMatrizIncidencia):
        pass  #kosaraju matriz de incidencia

def numero_componentes_conexos(grafo):
        """Retorna o número de componentes conexos no grafo."""
        visitados = [False] * grafo.num_vertices

        def dfs(vertice):
            visitados[vertice] = True
            for vizinho in obter_vizinhos(grafo, vertice):
                if not visitados[vizinho]:
                    dfs(vizinho)

        componentes = 0
        for v in range(grafo.num_vertices):
            if not visitados[v]:
                componentes += 1
                dfs(v)
        
        return componentes

def obter_vizinhos(grafo, vertice):
    """Retorna os vizinhos de um vértice em diferentes representações de grafo."""
    if isinstance(grafo, GrafoListaAdjacencia):
        # Lista de adjacência: os vizinhos já estão na lista correspondente ao vértice
        return grafo.lista[vertice]
    
    elif isinstance(grafo, GrafoMatrizAdjacencia):
        # Matriz de adjacência: verificar os índices onde há uma aresta (valor != 0)
        return [j for j in range(len(grafo.matriz[vertice])) if grafo.matriz[vertice][j] != 0]
    
    elif isinstance(grafo, GrafoMatrizIncidencia):
        # Matriz de incidência: encontrar arestas conectadas ao vértice e identificar os outros vértices conectados
        vizinhos = []
        for e in range(len(grafo.matriz[0])):  # Percorrer as arestas
            if grafo.matriz[vertice][e] != 0:  # Se a aresta envolve o vértice
                for u in range(len(grafo.matriz)):  # Procurar outro vértice na mesma aresta
                    if u != vertice and grafo.matriz[u][e] != 0:
                        vizinhos.append(u)
        return vizinhos
    
    else:
        raise TypeError("Tipo de grafo não suportado para obter vizinhos.")

def checar_ponte(grafo, u, v):
        """Checa se a aresta (u, v) é uma ponte."""
        if isinstance(grafo, GrafoMatrizAdjacencia):
            copia = GrafoMatrizAdjacencia(grafo.num_vertices, direcionado=False)
            copia.matriz = [linha[:] for linha in grafo.matriz]
            copia.matriz[u][v] = 0
            copia.matriz[v][u] = 0
        elif isinstance(grafo, GrafoListaAdjacencia):
            copia = GrafoListaAdjacencia(grafo.num_vertices, direcionado=False)
            copia.lista = [adjacentes[:] for adjacentes in grafo.lista]
            if v in copia.lista[u]:
                copia.lista[u].remove(v)
            if u in copia.lista[v]:
                copia.lista[v].remove(u)
        elif isinstance(grafo, GrafoMatrizIncidencia):
            copia = GrafoMatrizIncidencia(grafo.num_vertices, len(grafo.matriz[0]))
            copia.matriz = [linha[:] for linha in grafo.matriz]
            for e in range(len(grafo.matriz[0])):
                if grafo.matriz[u][e] != 0 and grafo.matriz[v][e] != 0:
                    for vertice in range(grafo.num_vertices):
                        copia.matriz[vertice][e] = 0
        else:
            raise TypeError("Tipo de grafo não suportado.")

        componentes_antes = numero_componentes_conexos(grafo)
        componentes_depois = numero_componentes_conexos(copia)
        return componentes_depois > componentes_antes

def checar_articulacao(grafo, v):
    """Checa se a remoção do vértice 'v' e suas arestas desconecta o grafo."""
    
    # Criar uma cópia do grafo original
    if isinstance(grafo, GrafoMatrizAdjacencia):
        copia = GrafoMatrizAdjacencia(grafo.num_vertices, grafo.direcionado)
        copia.matriz = [linha[:] for linha in grafo.matriz]
        
        # Remover o vértice e as arestas incidentes
        for i in range(grafo.num_vertices):
            copia.matriz[v][i] = 0
            copia.matriz[i][v] = 0
        
        copia.matriz.pop(v)
        for i in range(len(copia.matriz)):
            copia.matriz[i].pop(v)
        copia.num_vertices -= 1  # Atualiza o número de vértices

    elif isinstance(grafo, GrafoListaAdjacencia):
        copia = GrafoListaAdjacencia(grafo.num_vertices, grafo.direcionado)
        copia.lista = [adjacentes[:] for adjacentes in grafo.lista]
        
        # Remover o vértice e as arestas incidentes
        copia.lista.pop(v)
        for adjacentes in copia.lista:
            if v in adjacentes:
                adjacentes.remove(v)
        copia.num_vertices -= 1  # Atualiza o número de vértices

    elif isinstance(grafo, GrafoMatrizIncidencia):
        copia = GrafoMatrizIncidencia(grafo.num_vertices, len(grafo.matriz[0]), grafo.direcionado)
        copia.matriz = [linha[:] for linha in grafo.matriz]
        
        # Remover as arestas incidentes ao vértice
        for e in range(len(grafo.matriz[0])):
            if grafo.matriz[v][e] != 0:
                for u in range(grafo.num_vertices):
                    copia.matriz[u][e] = 0
        
        copia.matriz.pop(v)
        for i in range(len(copia.matriz)):
            copia.matriz[i].pop(v)
        copia.num_vertices -= 1  # Atualiza o número de vértices

    else:
        raise TypeError("Tipo de grafo não suportado.")
    
    # Contar o número de componentes conexos antes e depois de remover o vértice
    componentes_antes = numero_componentes_conexos(grafo)
    componentes_depois = numero_componentes_conexos(copia)
    
    # Se o número de componentes aumentou, a remoção do vértice desconectou o grafo
    if componentes_depois > componentes_antes:
        print(f"A remoção do vértice {v} desconectou o grafo.")
        return True  # O vértice é uma articulação
    else:
        print(f"A remoção do vértice {v} não desconectou o grafo.")
        return False  # O vértice não é uma articulação

def tarjan(grafo):
    if isinstance(grafo, GrafoListaAdjacencia):
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
            for u in grafo.lista[v]:
                if u not in tempo_descoberta:  # Se o vértice u não foi visitado
                    pai[u] = v
                    dfs(u)  # Recursão na DFS

                    # Após a DFS de u, atualizar o menor_tempo de v
                    menor_tempo[v] = min(menor_tempo[v], menor_tempo[u])

                    # Verificar se a aresta (v, u) é uma ponte
                    if menor_tempo[u] > tempo_descoberta[v]:
                        pontes.append((v, u))  # Armazenar a aresta como ponte
                # Se u já foi visitado e não é o pai de v, atualizar menor_tempo[v]
                elif u != pai.get(v):
                    menor_tempo[v] = min(menor_tempo[v], tempo_descoberta[u])

        # Iniciar DFS para todos os vértices não visitados
        for v in range(grafo.num_vertices):
            if v not in tempo_descoberta:
                dfs(v)

        return pontes
        
    elif isinstance(grafo, GrafoMatrizAdjacencia):
        tempo_descoberta = {}
        menor_tempo = {}
        pai = {}
        pontes = []
        tempo = [0]

        def dfs(v):
            tempo_descoberta[v] = menor_tempo[v] = tempo[0]
            tempo[0] += 1

            for u in range(grafo.num_vertices):
                if grafo.matriz[v][u] == 1:  # Ajuste para acessar matriz_adjacencia
                    if u not in tempo_descoberta:
                        pai[u] = v
                        dfs(u)
                        menor_tempo[v] = min(menor_tempo[v], menor_tempo[u])

                        if menor_tempo[u] > tempo_descoberta[v]:
                            pontes.append((v, u))  # Ajuste para índices começando de 1
                    elif u != pai.get(v):  # Se u já foi visitado e não é o pai de v
                        menor_tempo[v] = min(menor_tempo[v], tempo_descoberta[u])

        for v in range(grafo.num_vertices):
            if v not in tempo_descoberta:
                dfs(v)

        return pontes


    elif isinstance(grafo, GrafoMatrizIncidencia):
        time = [0]  # Tempo de descoberta de vértices
        pontes = []  # Lista para armazenar as pontes
        descoberta = [-1] * grafo.num_vertices  # Armazena o tempo de descoberta de cada vértice
        menor = [-1] * grafo.num_vertices  # Armazena o menor tempo de descoberta de um vértice adjacente
        pai = [-1] * grafo.num_vertices  # Pai de cada vértice durante a DFS

        def dfs(v):
            descoberta[v] = menor[v] = time[0]
            time[0] += 1

            for i in range(grafo.num_arestas):
                if grafo.matriz[v][i] == 1:  # Acessa a matriz de incidência
                    u = -1
                    for j in range(grafo.num_vertices):
                        if grafo.matriz[j][i] == 1 and j != v:  # Encontra o vértice adjacente
                            u = j
                            break

                    if u != -1 and descoberta[u] == -1:  # Se u não foi visitado
                        pai[u] = v
                        dfs(u)
                        menor[v] = min(menor[v], menor[u])

                        if menor[u] > descoberta[v]:
                            pontes.append((v, u))  # Ajustar para índices começando de 1
                    elif u != -1 and u != pai[v]:  # Se u já foi visitado e não é o pai de v
                        menor[v] = min(menor[v], descoberta[u])

        for v in range(grafo.num_vertices):
            if descoberta[v] == -1:
                dfs(v)

        return pontes  # Retorna a lista de pontes encontradas
def fleury(grafo):
    # Para GrafoMatrizAdjacencia
    if isinstance(grafo, GrafoMatrizAdjacencia):
        graus = [sum(grafo.matriz[v]) for v in range(grafo.num_vertices)]
        impares = [v for v in range(grafo.num_vertices) if graus[v] % 2 != 0]
        if len(impares) > 2:
            return "O grafo não é euleriano."

        caminho = []
        vertice_atual = impares[0] if impares else 0
        stack = [vertice_atual]

        while stack:
            u = stack[-1]
            aresta_encontrada = False
            for v in range(grafo.num_vertices):
                if grafo.matriz[u][v] == 1:
                    grafo.matriz[u][v] = 0
                    if not grafo.direcionado:
                        grafo.matriz[v][u] = 0
                    stack.append(v)
                    aresta_encontrada = True
                    break
            if not aresta_encontrada:
                caminho.append(stack.pop())

        return caminho

    # Para GrafoListaAdjacencia
    elif isinstance(grafo, GrafoListaAdjacencia):
        graus = [len(grafo.lista[v]) for v in range(grafo.num_vertices)]
        impares = [v for v in range(grafo.num_vertices) if graus[v] % 2 != 0]
        if len(impares) > 2:
            return "O grafo não é euleriano."

        caminho = []
        vertice_atual = impares[0] if impares else 0
        stack = [vertice_atual]

        while stack:
            u = stack[-1]
            if grafo.lista[u]:
                v = grafo.lista[u].pop()
                grafo.lista[v].remove(u)  # Remover a aresta simétrica
                stack.append(v)
            else:
                caminho.append(stack.pop())

        return caminho

    # Para GrafoMatrizIncidencia
    elif isinstance(grafo, GrafoMatrizIncidencia):
        graus = [sum(grafo.matriz[v]) for v in range(grafo.num_vertices)]
        impares = [v for v in range(grafo.num_vertices) if graus[v] % 2 != 0]
        if len(impares) > 2:
            return "O grafo não é euleriano."

        caminho = []
        vertice_atual = impares[0] if impares else 0
        stack = [vertice_atual]

        while stack:
            u = stack[-1]
            aresta_encontrada = False
            for i, aresta in enumerate(grafo.arestas):
                if grafo.matriz[u][i] == 1:
                    v = aresta[1] if grafo.arestas[i][0] == u else aresta[0]
                    grafo.matriz[u][i] = 0
                    if not grafo.direcionado:
                        grafo.matriz[v][i] = 0
                    stack.append(v)
                    aresta_encontrada = True
                    break
            if not aresta_encontrada:
                caminho.append(stack.pop())

        return caminho

    else:
        return "Tipo de grafo não reconhecido."
