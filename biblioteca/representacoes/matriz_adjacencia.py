
# self representa a instancia atual de uma classe, usado para acessar variaveis que pertecenm a classe
# permite que vc acesse os atributos e metodos da classe dentro de suas proprias definicoes
# quando você cria uma instância de uma classe e chama um método dessa instância, o Python passa automaticamente a instância como o primeiro argumento para o método. Esse primeiro argumento é convencionalmente chamado de self.


# map aplica uma função a todos os itens em de uma lista e retorna um iterador dos resultados, map(funcao, iteravel)
# str converte um valor para uma string




class GrafoMatrizAdjacencia:
    def __init__(self, num_vertices, direcionado=False):
        self.num_vertices = num_vertices #inicializa o atributo num_vertices com o valor passado como argumento, armazena o num de verices no grafo 
        self.matriz = [[0] * num_vertices for _ in range(num_vertices)] # cria uma matriz bidimensional (lista de listas) de tamanho num_vertices x num_vertices, onde cada elemento é inicializado com ovalor 0, usada p representar as arestas do grafo
        self.direcionado = direcionado
        
        
        
    def adicionar_aresta(self, u, v):
        self.matriz[u][v] = 1
        if not self.direcionado:
            self.matriz[v][u] = 1

        
        
    def remover_aresta(self, v, u):
        self.matriz[v][u] = 0
        if not self.direcionado:
            self.matriz[u][v] = 0

        
    
    # map(str, linha) aplica a função str a cada elemento de linha, convertendo-os para strings
    # " ".join() junta os elementos de uma lista em uma string, separando-os por um espaço
    def exibir_matriz(self):
        for linha in self.matriz:
            print(" ".join(map(str, linha)))
        
        
    def mostrar_posicoes_livres(self):
        print("Posições sem arestas (livres):")
        livres = [(i, j) for i in range(self.num_vertices) for j in range(i + 1, self.num_vertices) if self.matriz[i][j] == 0] # filtra posicoes onde nao ha aresta 
        if livres:
            for pos in livres:
                print(f"Aresta ausente entre {pos[0]} e {pos[1]}")
        else:
            print("Todas as posições já possuem arestas.")

    def mostrar_posicoes_ocupadas(self):
        print("Posições com arestas (ocupadas):")
        ocupadas = [(i, j) for i in range(self.num_vertices) for j in range(i + 1, self.num_vertices) if self.matriz[i][j] == 1]
        if ocupadas:
            for pos in ocupadas:
                print(f"Aresta presente entre {pos[0]} e {pos[1]}")
        else:
            print("Nenhuma posição possui arestas no momento.")
