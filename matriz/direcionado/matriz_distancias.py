class Grafo:

    def __init__(self, vertices, rotulos):
        self.vertices = vertices
        self.rotulos = rotulos
        self.grafo = [[0]*self.vertices for i in range(self.vertices)]
        self.mapeamento = {rotulo: i for i, rotulo in enumerate(rotulos)}

    def adiciona_aresta(self, u, v, peso):
        if u in self.mapeamento and v in self.mapeamento:
            i, j = self.mapeamento[u], self.mapeamento[v]
            self.grafo[i][j] = peso
        else:
            print("Um dos rótulos dos vértices não existe.")

    def remove_aresta(self, u, v):
        if u in self.mapeamento and v in self.mapeamento:
            i, j = self.mapeamento[u], self.mapeamento[v]
            self.grafo[i][j] = None
        else:
            print("Um dos rótulos dos vértices não existe.")

    def checagem_adjacencia_vertice(self, u, v):
        if u in self.mapeamento and v in self.mapeamento:
            i, j = self.mapeamento[u], self.mapeamento[v]
            return self.grafo[i][j] is not None
        else:
            print("Um dos rótulos dos vértices não existe.")
            return False

    def chegagem_adjacencia_aresta(self, u1, v1, u2, v2):
        if u1 in self.mapeamento and v1 in self.mapeamento and u2 in self.mapeamento and v2 in self.mapeamento:
            i1, j1, i2, j2 = self.mapeamento[u1], self.mapeamento[v1], self.mapeamento[u2], self.mapeamento[v2]
        if i1 == i2 or i1 == j2 or j1 == i2 or j1 == j2:
            return True
        else: 
            return False
        
    def contagem_arestas(self):
        cont = 0

        for i in range(self.vertices):
            for j in range(self.vertices):
                if self.grafo[i][j] != 0:
                    cont = cont + 1
        print(cont)
        return cont
    
    def contagem_vertices(self):
        cont = 0

        for i in range(self.vertices):
            cont = cont + 1
        print(cont)
        return cont
        
    # def contagem_arestas(self):
    #     contador = sum(1 for i in range(self.vertices) for j in range(self.vertices) if self.grafo[i][j] is not None)
    #     print(f'Total de arestas: {contador}')
    #     return contador

    def mostra_matriz(self):
        print('Matriz de Adjacencia')
        for i in range(self.vertices):
            print(self.grafo[i])

    def grafo_vazio(self):
        for i in range(self.vertices):
            for j in range(self.vertices):
                if(self.grafo[i][j] != 0):
                    return False
        return True
    
    def grafo_completo(self):
        n = self.contagem_vertices()
        a = self.contagem_arestas()

        nCompleto = (n * ( n-1 )) / 2

        if a == nCompleto:
            return True
        else:
            return False
        

v = int(input('Digite a quantidade de vertices'))
rotulos = [input(f'Rótulo do vértice {i + 1}: ') for i in range(v)]
g = Grafo(v, rotulos)    

a = int(input('Digite a quantidade de arestas'))
for i in range(a):
    u = input('De qual vertice parte esta aresta')
    v = input('Para qual vertice chega esta aresta')
    p = int(input('Qual o peso dessa aresta'))
    g.adiciona_aresta(u,v,p)


while True:
    print('\nMenu:')
    print('1. Adicionar aresta')
    print('2. Remover aresta')
    print('3. Checagem de adjacência entre dois vértices')
    print('4. Checagem de adjacência entre duas arestas')
    print('5. Contar arestas')
    print('6. Mostrar matriz de adjacência')
    print('7. Verificar se o grafo é vazio')
    print('8. Verificar se o grafo é completo')
    print('9. Numero de arestas')
    print('10. Numero de vertices')
    print('11. Numero de arestas')
    print('12. Conectividade')
    print('13. Quantidade de componentes fortemente conexos com Kosaraju')
    print('14. Checagem ponte')
    print('15. Checagem articulação')
    print('0. Sair')
    opcao = int(input('Escolha uma opção: '))

    if opcao == 1:
        u = input('De qual vértice parte esta aresta: ')
        v = input('Para qual vértice chega esta aresta: ')
        p = int(input('Qual o peso dessa aresta: '))
        g.adiciona_aresta(u, v, p)
    elif opcao == 2:
        u = input('De qual vértice parte esta aresta: ')
        v = input('Para qual vértice chega esta aresta: ')
        g.remove_aresta(u, v)
    elif opcao == 3:
        u = input('Digite o primeiro vértice: ')
        v = input('Digite o segundo vértice: ')
        print(g.checagem_adjacencia_vertice(u, v))
    elif opcao == 4:
        u1 = input('Digite o primeiro vértice da primeira aresta: ')
        v1 = input('Digite o segundo vértice da primeira aresta: ')
        u2 = input('Digite o primeiro vértice da segunda aresta: ')
        v2 = input('Digite o segundo vértice da segunda aresta: ')
        print(g.checagem_adjacencia_aresta(u1, v1, u2, v2))
    elif opcao == 5:
        g.contagem_arestas()
    elif opcao == 6:
        g.mostra_matriz()
    elif opcao == 7:
        if g.grafo_vazio() == True:
            print('O grafo é vazio')
        else:
            print('O grafo não é vazio')
    elif opcao == 8:
        if g.grafo_completo() == True:
            print('O grafo é completo')
        else:
            print('O grafo não é completo')
    elif opcao == 10:
        g.contagem_vertices()    
    elif opcao == 11:
        g.contagem_arestas()        
    elif opcao == 0:
        print('Encerrando o programa.')
        break
    else:
        print('Opção inválida. Tente novamente.')
