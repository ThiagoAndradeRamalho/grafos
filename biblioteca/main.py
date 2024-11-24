from grafo import Grafo
from manipulacao import *

def main():
    # Criação de um grafo direcionado com 7 vértices
    # grafo_direcionado = Grafo(direcionado=True)

    # # Adicionando vértices com rótulos como strings representando os números
    # grafo_direcionado.adicionar_vertice(0, "0")
    # grafo_direcionado.adicionar_vertice(1, "1")
    # grafo_direcionado.adicionar_vertice(2, "2")
    # grafo_direcionado.adicionar_vertice(3, "3")
    # grafo_direcionado.adicionar_vertice(4, "4")
    # grafo_direcionado.adicionar_vertice(5, "5")
    # grafo_direcionado.adicionar_vertice(6, "6")

    # # Adicionando arestas com rótulos de a1 a a7
    # grafo_direcionado.adicionar_aresta(0, 1, "a1")
    # grafo_direcionado.adicionar_aresta(1, 2, "a2")
    # grafo_direcionado.adicionar_aresta(2, 3, "a3")
    # grafo_direcionado.adicionar_aresta(3, 4, "a4")
    # grafo_direcionado.adicionar_aresta(4, 5, "a5")
    # grafo_direcionado.adicionar_aresta(5, 6, "a6")
    # grafo_direcionado.adicionar_aresta(6, 0, "a7")

    # print("\nGrafo Direcionado:")
    # grafo_direcionado.exibir_lista()

    # # Funções para grafos direcionados
    # print("\nFunções para grafos direcionados:")
    # print("1. Verificar adjacência entre 0 e 1:", grafo_direcionado.checar_adjacencia_vertices(0, 1))
    # print("2. Grau de 1:", grafo_direcionado.grau_do_vertice(1))
    # print("4. Verificar se existe aresta entre 0 e 2:", grafo_direcionado.checagem_de_aresta(0, 2))
    # print("5. Exibindo matriz de adjacência:")
    # grafo_direcionado.exibir_matriz_adjacencia()
    # print("6. Matriz de Incidência para Grafo direcionado:")
    # grafo_direcionado.exibir_matriz_incidencia()

    # Criação de um grafo não direcionado com 7 vértices
    grafo_nao_direcionado = Grafo(direcionado=False)

    # Adicionando vértices com rótulos como strings representando os números
    grafo_nao_direcionado.adicionar_vertice("b")
    grafo_nao_direcionado.adicionar_vertice("c")
    grafo_nao_direcionado.adicionar_vertice("d")
    grafo_nao_direcionado.adicionar_vertice("e")
    grafo_nao_direcionado.adicionar_vertice("f")
    grafo_nao_direcionado.adicionar_vertice("g")
    grafo_nao_direcionado.adicionar_vertice("h")

    # Adicionando arestas com rótulos de a1 a a7
    grafo_nao_direcionado.adicionar_aresta("b", "c", "a1")
    # grafo_nao_direcionado.adicionar_aresta(1, 2, "a2")
    # grafo_nao_direcionado.adicionar_aresta(2, 3, "a3")
    # grafo_nao_direcionado.adicionar_aresta(3, 4, "a4")
    # grafo_nao_direcionado.adicionar_aresta(4, 5, "a5")
    # grafo_nao_direcionado.adicionar_aresta(5, 6, "a6")
    # grafo_nao_direcionado.adicionar_aresta(6, 0, "a7")


    print("\nGrafo Não Direcionado:")
    grafo_nao_direcionado.exibir_lista()
    
    # Funções para grafos não direcionados
    print("\nFunções para grafos não direcionados:")
    print("1. Verificar adjacência entre 0 e 1:", grafo_nao_direcionado.checar_adjacencia_vertices(0, 1))
    print("2. Grau de 3:", grafo_nao_direcionado.grau_do_vertice(3))
    print("3. Verificar se existe aresta entre 2 e 4:", grafo_nao_direcionado.checagem_de_aresta(2, 4))
    print("4. Exibindo matriz de adjacência:")
    grafo_nao_direcionado.exibir_matriz_adjacencia()

    # Exibindo matriz de incidência para o grafo não direcionado
    print("\nMatriz de Incidência para Grafo Não Direcionado:")
    grafo_nao_direcionado.exibir_matriz_incidencia()

if __name__ == "__main__":
    main()
