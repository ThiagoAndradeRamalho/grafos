# main.py

from grafo import Grafo
from manipulacao import *  # Supondo que esta função existe e tem verifica_conectividade


def main():
    # Criação de um grafo direcionado com 7 vértices
    grafo_direcionado = Grafo(direcionado=True)

    # Adicionando vértices com rótulos como strings representando os números
    grafo_direcionado.adicionar_vertice("A")
    grafo_direcionado.adicionar_vertice("B")
    grafo_direcionado.adicionar_vertice("2")
    grafo_direcionado.adicionar_vertice("3")
    grafo_direcionado.adicionar_vertice("4")
    grafo_direcionado.adicionar_vertice("5")
    grafo_direcionado.adicionar_vertice("6")
    
    grafo_direcionado.rotular_vertice(0, "teste")  # Rótulo do vértice "0" como "teste"

    # Adicionando arestas com rótulos de a1 a a7 usando rótulos de vértices
    grafo_direcionado.adicionar_aresta("A", "B", "a1")  # Usando os rótulos diretamente
    grafo_direcionado.adicionar_aresta("2", "3", "a2")
    grafo_direcionado.adicionar_aresta("3", "4", "a3")
    grafo_direcionado.adicionar_aresta("4", "5", "a4")
    grafo_direcionado.adicionar_aresta("5", "6", "a5")
    grafo_direcionado.adicionar_aresta("6", "2", "a6")
    grafo_direcionado.adicionar_aresta("6", "A", "a7")

    print("Fleury com naive: ", fleury_naive(grafo_direcionado))

    # print("\nGrafo Direcionado:")
    # grafo_direcionado.exibir_lista()
    # grafo_direcionado.exibir_matriz_adjacencia()
    # grafo_direcionado.exibir_matriz_incidencia()

    # # Criação de um grafo não direcionado com 7 vértices
    # grafo_nao_direcionado = Grafo(direcionado=False)



    # # Adicionando vértices com rótulos como strings representando os números
    # grafo_nao_direcionado.adicionar_vertice("A")
    # grafo_nao_direcionado.adicionar_vertice("1")
    # grafo_nao_direcionado.adicionar_vertice("C")
    # grafo_nao_direcionado.adicionar_vertice("3")
    # grafo_nao_direcionado.adicionar_vertice("4")
    # grafo_nao_direcionado.adicionar_vertice("5")
    # grafo_nao_direcionado.adicionar_vertice("6")

    # # Adicionando arestas para o grafo não direcionado
    # grafo_nao_direcionado.adicionar_aresta("0", "1")
    # grafo_nao_direcionado.adicionar_aresta("1", "2")
    # grafo_nao_direcionado.adicionar_aresta("2", "3")
    # grafo_nao_direcionado.adicionar_aresta("3", "4")
    # grafo_nao_direcionado.adicionar_aresta("4", "5")
    # grafo_nao_direcionado.adicionar_aresta("5", "6")
    # grafo_nao_direcionado.adicionar_aresta("6", "0")
    

    # print("\nGrafo Não Direcionado:")
    # grafo_nao_direcionado.exibir_lista()
    # grafo_nao_direcionado.exibir_matriz_adjacencia()
    # grafo_nao_direcionado.exibir_matriz_incidencia()

    
    
    # salvar_grafo_gexf(grafo_direcionado, 'oi.gexf')
if __name__ == "__main__":
    main()
