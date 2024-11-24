from grafo import Grafo
from manipulacao import *  # Supondo que esta função existe e tem verifica_conectividade

def main():
    # Grafo semi-fortemente conexo
    grafo_semi_fortemente_conexo = Grafo(direcionado=True)
    
    # Adicionando vértices
    grafo_semi_fortemente_conexo.adicionar_vertice("0")
    grafo_semi_fortemente_conexo.adicionar_vertice("1")
    grafo_semi_fortemente_conexo.adicionar_vertice("2")
    grafo_semi_fortemente_conexo.adicionar_vertice("3")

    # Adicionando arestas
    grafo_semi_fortemente_conexo.adicionar_aresta("0", "1", "a1")
    grafo_semi_fortemente_conexo.adicionar_aresta("1", "2", "a2")
    grafo_semi_fortemente_conexo.adicionar_aresta("2", "0", "a3")
    grafo_semi_fortemente_conexo.adicionar_aresta("3", "2", "a4")

    print("\nGrafo Semi-Fortemente Conexo:")
    grafo_semi_fortemente_conexo.exibir_lista()
    print("\nConectividade (semi-fortemente conexo):")
    print(verifica_conectividade(grafo_semi_fortemente_conexo))

    # Grafo fortemente conexo
    grafo_fortemente_conexo = Grafo(direcionado=True)
    
    # Adicionando vértices
    grafo_fortemente_conexo.adicionar_vertice("0")
    grafo_fortemente_conexo.adicionar_vertice("1")
    grafo_fortemente_conexo.adicionar_vertice("2")
    grafo_fortemente_conexo.adicionar_vertice("3")

    # Adicionando arestas (fortemente conexo)
    grafo_fortemente_conexo.adicionar_aresta("0", "1", "a1")
    grafo_fortemente_conexo.adicionar_aresta("1", "2", "a2")
    grafo_fortemente_conexo.adicionar_aresta("2", "3", "a3")
    grafo_fortemente_conexo.adicionar_aresta("3", "0", "a4")

    print("\nGrafo Fortemente Conexo:")
    grafo_fortemente_conexo.exibir_lista()
    print("\nConectividade (fortemente conexo):")
    print(verifica_conectividade(grafo_fortemente_conexo))

    # Grafo não direcionado, simplesmente conexo
    grafo_simplesmente_conexo = Grafo(direcionado=False)
    
    # Adicionando vértices
    grafo_simplesmente_conexo.adicionar_vertice("0")
    grafo_simplesmente_conexo.adicionar_vertice("1")
    grafo_simplesmente_conexo.adicionar_vertice("2")
    grafo_simplesmente_conexo.adicionar_vertice("3")

    # Adicionando arestas (simplesmente conexo)
    grafo_simplesmente_conexo.adicionar_aresta("0", "1", "a1")
    grafo_simplesmente_conexo.adicionar_aresta("1", "2", "a2")
    grafo_simplesmente_conexo.adicionar_aresta("2", "3", "a3")
    grafo_simplesmente_conexo.adicionar_aresta("3", "0", "a4")

    print("\nGrafo Simplesmente Conexo (Não Direcionado):")
    grafo_simplesmente_conexo.exibir_lista()
    print("\nConectividade (simplesmente conexo):")
    print(verifica_conectividade(grafo_simplesmente_conexo))

if __name__ == "__main__":
    main()
