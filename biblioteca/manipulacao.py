from biblioteca.representacoes.grafo import Grafo

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

