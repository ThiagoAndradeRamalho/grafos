from listaAdjacencia import Grafo  

def main():
    grafo = Grafo(0)
    print("Lista de Adjacência Inicial: \n")
    grafo.exibir_lista_adjacencia()
    
    qtd_vertices = int(input("Informe o número de vértices para adicionar ao grafo: "))

    grafo.adicionar_vertices(qtd_vertices)

    print("\nLista de Adjacência Após Adicionar Vértices:")
    grafo.exibir_lista_adjacencia()
    
    grafo.adicionar_aresta()
    
    print("\nLista de Adjacência Após Adicionar arestas:")
    grafo.exibir_lista_adjacencia()
    
    grafo.ponderar_e_rotular_vertices()
    grafo.exibir_com_rotulos_e_pesos_vertices()
    
    grafo.ponderar_e_rotular_arestas()
    grafo.exibir_com_rotulos_e_pesos()
    
    grafo.checar_adjacencia_vertices()
    grafo.checar_adjacencia_arestas()
if __name__ == "__main__":
    main()
