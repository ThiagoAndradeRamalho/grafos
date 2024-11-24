from grafo import Grafo

def quantidade_arestas(grafo):
    total_arestas = 0
    for vertice in grafo.lista:
        total_arestas += len(grafo.lista[vertice])

    if not grafo.direcionado:
        total_arestas //= 2
    
    return total_arestas

def quantidade_vertices(grafo):
    return len(grafo.lista)

def grafo_vazio(grafo):
    return quantidade_arestas(grafo) == 0

def grafo_completo(grafo):
    n = len(grafo.lista)  
    return all(len(grafo.lista[v]) == n - 1 for v in grafo.lista)

def _dfs(grafo, origem, TD, TT, pai, t, ordem_visitados, destino=None, encontrado=None):
    mapa = grafo.mapear_vertices_para_indices()
    u = mapa[origem] 
    TD[u] = t
    ordem_visitados.append(origem)
    t += 1

    for vizinho in grafo.lista[origem]:
        if destino and encontrado[0]: 
            return
        v = mapa[vizinho]
        if TD[v] == -1:
            pai[v] = origem
            _dfs(grafo, vizinho, TD, TT, pai, t, ordem_visitados, destino, encontrado)

    TT[u] = t
    t += 1

    if origem == destino:
        encontrado[0] = True

def obter_vertice_por_rotulo(grafo, rotulo):
    return grafo.rotulos_vertices.get(rotulo, None)

def subgrafo_subjacente(grafo):
    subjacente = Grafo(direcionado=grafo.direcionado)

    for vertice in grafo.lista.keys():
        subjacente.adicionar_vertice(vertice)

    for origem, destinos in grafo.lista.items():
        for destino in destinos:
            if not subjacente.existe_aresta(origem, destino) and not subjacente.existe_aresta(destino, origem):
                subjacente.adicionar_aresta(origem, destino)
    
    return subjacente

def verifica_conectividade(grafo):
    grafo_subjacente = subgrafo_subjacente(grafo) 
    componentes = busca_profundidade_componentes(grafo_subjacente)

    if componentes == 1:
        print("O grafo é simplesmente conexo (S-Conexo).")
    else:
        print(f"O grafo não é simplesmente conexo. Ele possui {componentes} componentes.")
        return "Não Conexo"

    grafo.num_vertices = len(grafo.lista)
    for u in grafo.lista:
        for v in grafo.lista:
            if u != v:
                if not (alcancavel(grafo, u, v) or alcancavel(grafo, v, u)):
                    print(f"O grafo não é semifortemente conexo. Problema nos vértices ({u}, {v}).")
                    return "Simplesmente Conexo"

    print("O grafo é semifortemente conexo (SF-Conexo).")

    for u in grafo.lista:
        for v in grafo.lista:
            if u != v:
                if not (alcancavel(grafo, u, v) and alcancavel(grafo, v, u)):
                    print(f"O grafo não é fortemente conexo. Problema nos vértices ({u}, {v}).")
                    return "Semifortemente Conexo"

    print("O grafo é fortemente conexo (F-Conexo).")
    return "Fortemente Conexo"


def alcancavel(grafo, origem, destino):
    num_vertices = len(grafo.lista)
    TD = [-1] * num_vertices  
    TT = [-1] * num_vertices  
    pai = [None] * num_vertices
    ordem_visitados = []
    encontrado = [False]

    _dfs(grafo, origem, TD, TT, pai, 0, ordem_visitados, destino, encontrado)
    return encontrado[0]

def busca_profundidade_componentes(grafo):
    visitados = set()

    def dfs(v):
        visitados.add(v)
        for vizinho in grafo.lista.get(v, []):
            if vizinho not in visitados:
                dfs(vizinho)

    componentes = 0

    for vertice in grafo.lista.keys():
        if vertice not in visitados:
            dfs(vertice)
            componentes += 1

    return componentes

def naive(grafo):
    pontes = []
    
    subjacente = subgrafo_subjacente(grafo) if grafo.direcionado else grafo

    num_componentes = busca_profundidade_componentes(subjacente)
    print("Componentes iniciais:", num_componentes)
    
    for u in grafo.lista.keys():
        for v in grafo.lista[u]:
            if grafo.direcionado or u < v:
                subjacente.remover_aresta(u, v)
                n = busca_profundidade_componentes(subjacente)
                print(f"Sem a aresta ({u}, {v}):", n)
                
                if n > num_componentes:
                    pontes.append((u, v))
                
                subjacente.adicionar_aresta(u, v)
    
    return pontes

def fleury(grafo):
    vertices_grau_impar = [u for u in range(grafo.num_vertices) if grafo.grau(u)[0] % 2 != 0]
    print("Vértices com grau ímpar:", vertices_grau_impar)
    
    if len(vertices_grau_impar) > 2:
        raise ValueError("O grafo não possui caminho euleriano (mais de dois vértices de grau ímpar).")

    grafo_aux = grafo.duplicar_grafo()

    u = vertices_grau_impar[0] if vertices_grau_impar else 0

    caminho = []

    while any(len(arestas) > 0 for arestas in grafo_aux.lista):
        print(f"Vértice atual: {u}, Arestas disponíveis: {grafo_aux.lista[u]}")

        arestas = grafo_aux.lista[u]

        if not arestas:
            print(f"Vértice {u} sem arestas. Encerrando busca neste ramo.")
            break

        for v in arestas[:]:
            print(f"Tentando a aresta ({u}, {v})")
            grafo_aux.remover_aresta(u, v)

            if busca_profundidade_componentes(grafo_aux) == 1 or len(arestas) == 1:
                print(f"Aresta ({u}, {v}) removida. Atualizando caminho.")
                caminho.append((u, v))
                u = v
                break
            else:
                grafo_aux.adicionar_aresta(u, v)

        else:
            v = arestas[0]
            grafo_aux.remover_aresta(u, v)
            print(f"Todas as arestas são pontes. Removendo ({u}, {v}).")
            caminho.append((u, v))
            u = v

        print(f"Caminho até agora: {caminho}")

    print(f"Caminho euleriano encontrado: {caminho}")
    return caminho

def dfs(grafo, v, visitado):
    visitado[v] = True
    for vizinho in grafo.lista[v]:
        if not visitado[vizinho]:
            dfs(grafo, vizinho, visitado)

    def construir_reverso(grafo):
        grafo_reverso = Grafo(direcionado=True)
        for u in grafo.lista:
            for v in grafo.lista[u]:
                grafo_reverso.adicionar_aresta(v, u)
        return grafo_reverso

    visitados = {vertice: False for vertice in grafo.lista}
    stack = []
    for vertice in grafo.lista:
        if not visitados[vertice]:
            dfs(grafo, vertice, visitados, stack)

    grafo_reverso = construir_reverso(grafo)

    visitados = {vertice: False for vertice in grafo_reverso.lista}
    cfc = []
    while stack:
        vertice = stack.pop()
        if not visitados[vertice]:
            componente = []
            dfs(grafo_reverso, vertice, visitados, componente)
            cfc.append(componente)

    return cfc

def numero_componentes_conexos(grafo):
    visitados = {vertice: False for vertice in grafo.lista}

    def dfs(vertice):
        visitados[vertice] = True
        for vizinho in grafo.lista[vertice]:
            if not visitados[vizinho]:
                dfs(vizinho)

    componentes = 0
    for vertice in grafo.lista:
        if not visitados[vertice]:
            componentes += 1
            dfs(vertice)
    
    return componentes

def checar_ponte(grafo, u, v):
    copia = Grafo(grafo.num_vertices, direcionado=False)
    copia.lista = [adjacentes[:] for adjacentes in grafo.lista]
    if v in copia.lista[u]:
        copia.lista[u].remove(v)
    if u in copia.lista[v]:
        copia.lista[v].remove(u)
        

    componentes_antes = numero_componentes_conexos(grafo)
    componentes_depois = numero_componentes_conexos(copia)
    return componentes_depois > componentes_antes

def checar_articulacao(grafo, v):
    copia = Grafo(grafo.num_vertices, grafo.direcionado)
    copia.lista = [adjacentes[:] for adjacentes in grafo.lista]

    # Encontrar o índice do vértice v
    vertices = [str(i) for i in range(grafo.num_vertices)]  # Ajuste conforme a estrutura de seu grafo
    if v not in vertices:
        print(f"O vértice {v} não existe no grafo.")
        return False

    indice_v = vertices.index(v)  # Agora obtemos o índice do vértice v

    # Remover o vértice e as arestas incidentes
    del copia.lista[indice_v]  # Remover o vértice v da lista de adjacências
    for adjacentes in copia.lista:
        if v in adjacentes:
            adjacentes.remove(v)
    
    copia.num_vertices -= 1  # Atualiza o número de vértices

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
    for v in grafo.lista:  # Agora usamos as chaves do dicionário (vértices como strings)
        if v not in tempo_descoberta:
            dfs(v)

    return pontes

def fleury(grafo):
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

def fleury_tarjan(grafo):
    # Identificar as pontes do grafo usando Tarjan
    pontes = set(tarjan(grafo))  # Usar um conjunto para busca eficiente
    graus = [len(grafo.lista[v]) for v in range(grafo.num_vertices)]
    impares = [v for v in range(grafo.num_vertices) if graus[v] % 2 != 0]

    # Verificar se o grafo é euleriano ou semi-euleriano
    if len(impares) > 2:
        return "O grafo não é euleriano."

    caminho = []
    vertice_atual = impares[0] if impares else 0
    stack = [vertice_atual]
    s = set()  # Conjunto para armazenar vértices visitados

    while stack:
        u = stack[-1]
        s.add(u)  # Adiciona o vértice atual ao conjunto S

        # Verificar as arestas disponíveis para escolher a próxima
        arestas_disponiveis = [(u, v) for v in grafo.lista[u] if (u, v) not in pontes and (v, u) not in pontes]
        
        # Se não houver arestas disponíveis que não sejam pontes, usar qualquer outra
        if not arestas_disponiveis:
            if grafo.lista[u]:
                v = grafo.lista[u].pop()
                grafo.lista[v].remove(u)  # Remover a aresta simétrica
                stack.append(v)
            else:
                caminho.append(stack.pop())
        else:
            # Escolher uma aresta que não seja uma ponte
            v = arestas_disponiveis[0][1]
            grafo.lista[u].remove(v)
            grafo.lista[v].remove(u)  # Remover a aresta simétrica
            stack.append(v)

    return caminho


def salvar_grafo_gexf(grafo, nome_arquivo):
    pasta = "arquivos"

    # Verifica se a pasta "arquivos" está no caminho, se não, ajusta o nome do arquivo
    if not nome_arquivo.startswith(pasta):
        nome_arquivo = pasta + "/" + nome_arquivo

    try:
        # Abre o arquivo no modo de escrita e salva os dados
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            arquivo.write('<gexf xmlns="http://www.gexf.net/1.2draft" version="1.2">\n')
            arquivo.write('  <graph mode="static" defaultedgetype="{}">\n'.format(
                "directed" if grafo.direcionado else "undirected"))
            arquivo.write('    <nodes>\n')

            # Escreve os vértices
            for vertice in grafo.lista:
                arquivo.write(f'      <node id="{vertice}" label="{vertice}"/>\n')

            arquivo.write('    </nodes>\n')
            arquivo.write('    <edges>\n')

            # Escreve as arestas
            edge_id = 0
            for u, adjacentes in grafo.lista.items():
                for v in adjacentes:
                    # Evita duplicação para grafos não direcionados
                    if not grafo.direcionado and (v, u) in grafo.rotulos_arestas:
                        continue

                    rotulo = grafo.rotulos_arestas.get((u, v), "sem rótulo")
                    arquivo.write(f'      <edge id="{edge_id}" source="{u}" target="{v}" label="{rotulo}"/>\n')
                    edge_id += 1

            arquivo.write('    </edges>\n')
            arquivo.write('  </graph>\n')
            arquivo.write('</gexf>\n')

        print(f"Grafo salvo no arquivo '{nome_arquivo}'.")

    except Exception as e:
        print(f"Erro ao salvar o grafo: {e}")





def carregar_grafo_gexf(nome_arquivo):

    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()

    grafo = Grafo(direcionado=any('defaultedgetype="directed"' in linha for linha in linhas))

    for linha in linhas:
        linha = linha.strip()
        if linha.startswith("<node"):
            vertice_id = linha.split('id="')[1].split('"')[0]
            rotulo = linha.split('label="')[1].split('"')[0] if 'label="' in linha else "sem rótulo"
            grafo.adicionar_vertice(vertice_id, rotulo)
        elif linha.startswith("<edge"):
            origem = linha.split('source="')[1].split('"')[0]
            destino = linha.split('target="')[1].split('"')[0]
            rotulo = linha.split('label="')[1].split('"')[0] if 'label="' in linha else None
            grafo.adicionar_aresta(origem, destino, rotulo)

    print(f"Grafo carregado do arquivo '{nome_arquivo}'.")
    return grafo

def gerar_numero_aleatorio(seed):
    seed = (seed * 9301 + 49297) % 233280
    return seed

def gerar_grafo_aleatorio(num_vertices, num_arestas, direcionado=False):
    grafo = Grafo(direcionado=direcionado)
    seed = 123456  

    # Adiciona vértices
    for i in range(num_vertices):
        rotulo_vertice = f"V{i}"  # rótulo único para cada vértice
        grafo.adicionar_vertice(str(i), rotulo=rotulo_vertice)

    max_arestas = num_vertices * (num_vertices - 1) 
    if not direcionado:
        max_arestas //= 2  # grafos não direcionados


    num_arestas = min(num_arestas, max_arestas)

    # Gera arestas aleatórias
    arestas_adicionadas = set() 
    while len(arestas_adicionadas) < num_arestas:
        seed = gerar_numero_aleatorio(seed)
        u = str(seed % num_vertices)  # escolhe um vértice aleatório
        seed = gerar_numero_aleatorio(seed)
        v = str(seed % num_vertices)  # escolhe outro vértice aleatório

        # evita arestas de um vértice para ele mesmo (em grafos simples)
        if u == v:
            continue

        # evita arestas duplicadas em grafos não direcionados
        if not direcionado and (v, u) in arestas_adicionadas:
            continue

        # adiciona a aresta ao grafo
        aresta = (u, v)
        if aresta not in arestas_adicionadas:
            arestas_adicionadas.add(aresta)
            rotulo_aresta = f"A{u}{v}"  # rótulo único para a aresta
            grafo.adicionar_aresta(u, v, rotulo=rotulo_aresta)

    return grafo

def kosaraju(grafo):
    """
    Implementação do algoritmo de Kosaraju para encontrar os componentes fortemente conectados.
    """
    # Passo 1: Realiza DFS no grafo original e empilha os vértices na ordem de término.
    def dfs(grafo, v, visitado, pilha):
        visitado[v] = True
        for vizinho in grafo.lista[v]:
            if not visitado[vizinho]:
                dfs(grafo, vizinho, visitado, pilha)
        pilha.append(v)  # Empilha o vértice ao final da DFS

    # Passo 2: Construa o grafo transposto
    grafo_transposto = obter_transposto(grafo)

    # Passo 3: Realiza DFS no grafo transposto na ordem da pilha
    def dfs_transposto(grafo, v, visitado, componente):
        visitado[v] = True
        componente.append(v)
        for vizinho in grafo.lista[v]:
            if not visitado[vizinho]:
                dfs_transposto(grafo, vizinho, visitado, componente)

    # Fase 1: Empilhar os vértices na ordem de término
    visitado = {v: False for v in grafo.lista}
    pilha = []
    
    for v in grafo.lista:
        if not visitado[v]:
            dfs(grafo, v, visitado, pilha)
    
    # Fase 2: Realizar DFS no grafo transposto, na ordem inversa da pilha
    visitado = {v: False for v in grafo.lista}
    cfc = []  # Lista que armazenará os componentes fortemente conectados

    while pilha:
        v = pilha.pop()
        if not visitado[v]:
            componente = []
            dfs_transposto(grafo_transposto, v, visitado, componente)
            cfc.append(componente)
    
    return cfc  # Retorna a lista de componentes fortemente conectados


def obter_transposto(grafo):
    # Cria um grafo vazio para armazenar o transposto
    transposto = Grafo(direcionado=True)  # Assumindo que o grafo original é direcionado

    # Adiciona os vértices do grafo original no grafo transposto
    for vertice in grafo.lista.keys():
        transposto.adicionar_vertice(vertice)

    # Adiciona as arestas invertidas ao grafo transposto
    for u, destinos in grafo.lista.items():
        for v in destinos:
            transposto.adicionar_aresta(v, u)  # Inverte a direção da aresta

    return transposto
