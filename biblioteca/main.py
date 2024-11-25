from grafo import Grafo
from manipulacao import *  # Supondo que esta função existe e tem verifica_conectividade

def main():
    # Grafo não direcionado
    grafo_nao_direcionado = Grafo(direcionado=False)
    
    # Adicionando vértices
    grafo_nao_direcionado.adicionar_vertice("1")
    grafo_nao_direcionado.adicionar_vertice("2")
    grafo_nao_direcionado.adicionar_vertice("3")
    grafo_nao_direcionado.adicionar_vertice("4")
    grafo_nao_direcionado.adicionar_vertice("5")
    grafo_nao_direcionado.adicionar_vertice("6")
    grafo_nao_direcionado.adicionar_vertice("7")
    
    # Adicionando arestas (não direcionadas)
    grafo_nao_direcionado.adicionar_aresta("1", "2", "a1")
    grafo_nao_direcionado.adicionar_aresta("1", "3", "a2")
    grafo_nao_direcionado.adicionar_aresta("2", "3", "a3")
    grafo_nao_direcionado.adicionar_aresta("2", "4", "a4")
    grafo_nao_direcionado.adicionar_aresta("2", "5", "a5")
    grafo_nao_direcionado.adicionar_aresta("3", "4", "a6")
    grafo_nao_direcionado.adicionar_aresta("3", "6", "a7")
    grafo_nao_direcionado.adicionar_aresta("4", "5", "a8")
    grafo_nao_direcionado.adicionar_aresta("4", "6", "a9")
    grafo_nao_direcionado.adicionar_aresta("5", "6", "b1")
    grafo_nao_direcionado.adicionar_aresta("5", "7", "b2")
    grafo_nao_direcionado.adicionar_aresta("6", "7", "b3")

    print("\nGrafo Não Direcionado:")
    grafo_nao_direcionado.exibir_lista()
    print("\nConectividade (não direcionado):")
    print(verifica_conectividade(grafo_nao_direcionado))

if __name__ == "__main__":
    main()
