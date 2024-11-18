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

   
    t = _dfs(grafo, 0, TD, TT, pai, t, ordem_visitados)
    
    
    if all(t > 0 for t in TD):
        print("O grafo é conexo.")
    else:
        print("O grafo não é conexo.")

    print("Tempo de Descoberta: ", TD)
    print("Tempo de Término: ", TT)
    print("Predecessores: ", pai)
    print("Ordem de visitação dos vértices:", ordem_visitados)

def _dfs(grafo, u, TD, TT, pai, t, ordem_visitados):
    t += 1
    TD[u] = t  
    print(f"Visitando vértice {u}, TD[{u}] = {TD[u]}")
    ordem_visitados.append(u)

    
    for v in vizinhos(grafo, u):
        if TD[v] == 0:  
            print(f"Aresta de árvore: ({u}, {v})")
            pai[v] = u  
            t = _dfs(grafo, v, TD, TT, pai, t, ordem_visitados)  

    t += 1
    TT[u] = t  
    print(f"Término do vértice {u}, TT[{u}] = {TT[u]}")
    
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
