from grafo import Grafo

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
        return "Nao existe o vertice {vertice}"
    
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
    return v in grafo.lista[u]



def checar_adjacencia_arestas(u, v, x, y):
    if v != x:
        return False
    
    return existe_aresta(u,v) and existe_aresta(x,y)
        
        
def existe_aresta(grafo, v, u):
        return v in grafo.lista[u]

def quantidade_vertices(grafo):
        return len(grafo.lista)  # num de vertices = o tamanho da lista de adjacência

def quantidade_arestas(grafo):
    return sum(len(adjacentes) for adjacentes in grafo.lista) // 2    

def grafo_vazio(grafo):
    return quantidade_arestas(grafo) == 0

def grafo_completo(grafo):
    n = len(grafo.lista)  
    # verifica se cada vertice ta conectado a todos os outros vertices
    return all(len(grafo.lista[v]) == n - 1 for v in grafo.lista)
    

def exibir_vertices(grafo):
    num_vertices = quantidade_vertices(grafo)
    print(f"Vértices do grafo ({num_vertices} no total):")
    for vertice in range(num_vertices): 
        rotulo = rotulos_vertices.get(grafo, {}).get(vertice, "sem rótulo")
        peso = pesos_vertices.get(grafo, {}).get(vertice, "sem peso")
        print(f"Vértice {vertice} (Rótulo: {rotulo}, Peso: {peso})")


def exibir_arestas(grafo):
    print("Arestas do grafo:")
    for u in range(grafo.num_vertices):
        for v in grafo.lista[u]:
            if u < v:  
                rotulo = rotulos_arestas.get(grafo, {}).get((u, v), "sem rótulo")
                peso = pesos_arestas.get(grafo, {}).get((u, v), "sem peso")
                print(f"Aresta entre {u} e {v} (Rótulo: {rotulo}, Peso: {peso})")

def busca_profundidade(grafo):
    num_vertices = quantidade_vertices(grafo)
    TD = [0] * num_vertices  
    TT = [0] * num_vertices  
    pai = [None] * num_vertices 
    t = 0  
    ordem_visitados = []  
    componentes = 0  

    for u in range(num_vertices):
        if TD[u] == 0:  
            componentes += 1  
            # print(f"Nova árvore DFS iniciada no vértice {u}")
            t = _dfs(grafo, u, TD, TT, pai, t, ordem_visitados)

    if componentes == 1:
        print("O grafo é conexo.")
    else:
        print(f"O grafo não é conexo. Ele tem {componentes} componentes conectados.")

    # print("Tempo de Descoberta: ", TD)
    # print("Tempo de Término: ", TT)
    # print("Predecessores: ", pai)
    # print("Ordem de visitação dos vértices:", ordem_visitados)

    return componentes

def _dfs(grafo, u, TD, TT, pai, t, ordem_visitados, destino=None, encontrado=None):
    t += 1
    TD[u] = t
    ordem_visitados.append(u)

    # Verifica se alcançamos o destino
    if destino is not None and u == destino:
        if encontrado is not None:
            encontrado[0] = True  # Marca que encontramos o destino
        return t

    # Continua a busca
    for v in vizinhos(grafo, u):
        if TD[v] == 0:  # Vértice não visitado
            pai[v] = u
            t = _dfs(grafo, v, TD, TT, pai, t, ordem_visitados, destino, encontrado)

    t += 1
    TT[u] = t
    return t

def vizinhos(grafo, u):
    return grafo.lista[u]


def subgrafo_subjacente(grafo):
    grafo_subjacente = Grafo(grafo.num_vertices - 1, False)
    for u in range(len(grafo.lista)):
        for v in grafo.lista[u]:
            if u < v:
                grafo_subjacente.adicionar_aresta(u, v)
    return grafo_subjacente

def verifica_conectividade(grafo):
    #verifica se o grafo é simplesmente conexo
    grafo_subjacente = subgrafo_subjacente(grafo)
    componentes = busca_profundidade(grafo_subjacente)

    if componentes == 1:
        print("O grafo é simplesmente conexo (S-Conexo).")
    else:
        print(f"O grafo não é simplesmente conexo. Ele possui {componentes} componentes.")

    #verifica se o grafo é semifortemente conexo
    num_vertices = grafo.num_vertices

    #verifica para cada par de vértices (u, v)
    for u in range(num_vertices):
        for v in range(num_vertices):
            if u != v:
                # Confere se pelo menos um alcança o outro
                if not (isAlcancavel(grafo, u, v) or isAlcancavel(grafo, v, u)):
                    print(f"O grafo não é semifortemente conexo. Problema nos vértices ({u}, {v}).")
                    return "S-Conexo"

    print("O grafo é semifortemente conexo (SF-Conexo).")
    for u in range(num_vertices):
        for v in range(num_vertices):
            if u != v:
                # Verifica se há conectividade bidirecional (u → v e v → u)
                if not (isAlcancavel(grafo, u, v) and isAlcancavel(grafo, v, u)):
                    print(f"O grafo não é fortemente conexo. Problema nos vértices ({u}, {v}).")
                    return "Semifortemente Conexo"

    print("O grafo é fortemente conexo (F-Conexo).")
    return "Fortemente Conexo"


def isAlcancavel(grafo, origem, destino):
    num_vertices = grafo.num_vertices
    TD = [0] * num_vertices
    TT = [0] * num_vertices
    pai = [None] * num_vertices
    ordem_visitados = []
    encontrado = [False]  # Variável mutável para verificar se destino foi alcançado

    # Executa a DFS a partir da origem
    _dfs(grafo, origem, TD, TT, pai, 0, ordem_visitados, destino, encontrado)
    
    return encontrado[0]

def busca_profundidade_componentes(grafo):
    visitados = [False] * grafo.num_vertices

    def dfs(u):
        visitados[u] = True
        for v in grafo.lista[u]:
            if v < grafo.num_vertices and not visitados[v]:  # Certifique-se de que 'v' está dentro do limite
                dfs(v)

    componentes = 0
    for u in range(grafo.num_vertices):
        if not visitados[u] and len(grafo.lista[u]) > 0:  # Apenas processa vértices conectados
            dfs(u)
            componentes += 1

    return componentes

def naive(grafo):
    pontes = []
    if grafo.direcionado:
        subjacente = subgrafo_subjacente(grafo)
        numComponentes = busca_profundidade(subjacente)
        print(numComponentes)
        
        for u in range(grafo.num_vertices):
            for v in grafo.lista[u]:
                if u < v:
                    subjacente.remover_aresta(u, v)
                    n = busca_profundidade(subjacente)
                    print("Sem a aresta",n)
                    if n > numComponentes:
                        pontes.append((u, v))
                subjacente.adicionar_aresta(u, v)  # Restaurar aresta após a remoção
        return pontes


def fleury(grafo):
    # Verificar número de vértices de grau ímpar
    vertices_grau_impar = [u for u in range(grafo.num_vertices) if grafo.grau(u)[0] % 2 != 0]
    print("Vértices com grau ímpar:", vertices_grau_impar)
    
    if len(vertices_grau_impar) > 2:
        raise ValueError("O grafo não possui caminho euleriano (mais de dois vértices de grau ímpar).")

    grafo_aux = grafo.duplicar_grafo()

    # Escolhe o vértice inicial: se há vértices ímpares, comece por um deles; caso contrário, escolha o vértice 0
    u = vertices_grau_impar[0] if vertices_grau_impar else 0

    caminho = []  # Caminho Euleriano

    while any(len(arestas) > 0 for arestas in grafo_aux.lista):  # Enquanto houver arestas no grafo
        print(f"Vértice atual: {u}, Arestas disponíveis: {grafo_aux.lista[u]}")

        arestas = grafo_aux.lista[u]

        if not arestas:  # Se não houver mais arestas para este vértice
            print(f"Vértice {u} sem arestas. Encerrando busca neste ramo.")
            break

        for v in arestas[:]:  # Iterar sobre uma cópia para evitar problemas durante modificações
            print(f"Tentando a aresta ({u}, {v})")
            grafo_aux.remover_aresta(u, v)  # Remove a aresta temporariamente

            if busca_profundidade_componentes(grafo_aux) == 1 or len(arestas) == 1:  # Verifica conectividade
                print(f"Aresta ({u}, {v}) removida. Atualizando caminho.")
                caminho.append((u, v))
                u = v  # Atualiza para o próximo vértice
                break
            else:
                # Se a remoção desconectou o grafo, restaura a aresta
                grafo_aux.adicionar_aresta(u, v)

        else:  # Se todas as arestas disponíveis forem pontes
            v = arestas[0]
            grafo_aux.remover_aresta(u, v)
            print(f"Todas as arestas são pontes. Removendo ({u}, {v}).")
            caminho.append((u, v))
            u = v  # Atualiza para o próximo vértice

        print(f"Caminho até agora: {caminho}")

    print(f"Caminho euleriano encontrado: {caminho}")
    return caminho

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
