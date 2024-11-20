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
            print(f"Nova árvore DFS iniciada no vértice {u}")
            t = _dfs(grafo, u, TD, TT, pai, t, ordem_visitados)

    if componentes == 1:
        print("O grafo é conexo.")
    else:
        print(f"O grafo não é conexo. Ele tem {componentes} componentes conectados.")

    print("Tempo de Descoberta: ", TD)
    print("Tempo de Término: ", TT)
    print("Predecessores: ", pai)
    print("Ordem de visitação dos vértices:", ordem_visitados)

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
    if isinstance(grafo, GrafoListaAdjacencia):
        return grafo.lista[u]
    elif isinstance(grafo, GrafoMatrizAdjacencia):
        return [v for v in range(grafo.num_vertices) if grafo.matriz[u][v] != 0]
    elif isinstance(grafo, GrafoMatrizIncidencia):
        return [v for v in range(grafo.num_vertices) if any(grafo.matriz[u][e] != 0 for e in range(grafo.num_arestas))]
    else:
        print("Tipo de grafo desconhecido.")
        return []

def subgrafo_subjacente(grafo):
    if isinstance(grafo, GrafoListaAdjacencia):
        grafo_subjacente = GrafoListaAdjacencia(grafo.num_vertices - 1)
        for u in range(len(grafo.lista)):
            for v in grafo.lista[u]:
                if u < v:
                    grafo_subjacente.adicionar_aresta(u, v)
        return grafo_subjacente

    elif isinstance(grafo, GrafoMatrizAdjacencia):
        grafo_subjacente = GrafoMatrizAdjacencia(grafo.num_vertices)
        for u in range(grafo.num_vertices):
            for v in range(grafo.num_vertices):
                if grafo.matriz[u][v] != 0:
                    grafo_subjacente.adicionar_aresta(u, v)
                    grafo_subjacente.adicionar_aresta(v, u)
        return grafo_subjacente

    elif isinstance(grafo, GrafoMatrizIncidencia):
        grafo_subjacente = GrafoMatrizAdjacencia(grafo.num_vertices)
        for e in range(grafo.num_arestas):
            u, v = grafo.obter_extremidades(e)
            if u is not None and v is not None:
                grafo_subjacente.adicionar_aresta(u, v)
                grafo_subjacente.adicionar_aresta(v, u)
        return grafo_subjacente

    else:
        raise ValueError("Representação de grafo desconhecida.")

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


def naive(grafo):

    pontes = []

    if grafo.direcionado:
        subjacente = subgrafo_subjacente(grafo)

        numComponentes = busca_profundidade(subjacente)
        
        for u in range(grafo.num_vertices):
            for v in grafo.lista[u]:
                if u < v:
                    subjacente.remover_aresta(u, v)
                    n = busca_profundidade(subjacente)
                    if n > numComponentes:
                        pontes.append((u, v))
                
                subjacente.adicionar_aresta(u,v)
        
        return pontes

def fleury(grafo):
    # verificar número de vértices de grau ímpar
    vertices_grau_impar = [u for u in range(grafo.num_vertices) if grafo.grau(u) % 2 != 0]
    if len(vertices_grau_impar) > 2:
        raise ValueError("O grafo não possui caminho euleriano (mais de dois vértices de grau ímpar).")

    grafo_aux = grafo.duplicar_grafo()

    u = vertices_grau_impar[0] if vertices_grau_impar else 0 # escolhe vértice inicial

    caminho = []
    while any(grafo_aux.lista):  # enquanto ainda houver arestas no grafo auxiliar
        pontes = naive(grafo_aux)
        arestas = grafo_aux.lista[u]

        for v in arestas:
            if (u, v) not in pontes and (v, u) not in pontes:  # escolher aresta não ponte, se possível
                break
        else:
            # Se todas as arestas forem pontes, escolher a única disponível
            v = arestas[0]

        # Registrar aresta no caminho e removê-la do grafo
        caminho.append((u, v))
        grafo_aux.remover_aresta(u, v)
        u = v  # Caminhar para o próximo vértice

    return caminho