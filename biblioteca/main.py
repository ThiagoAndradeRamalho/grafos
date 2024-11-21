from grafo import Grafo
from manipulacao import *

# def main():
#     grafo = GrafoListaAdjacencia(3, True)
#     grafo.adicionar_aresta(0, 1)
#     grafo.adicionar_aresta(0, 3)
#     grafo.adicionar_aresta(1, 2)
#     grafo.adicionar_aresta(2, 3)
#     # print(grafo.direcionado)
#     # print(grafo.exibir_lista)
#     # grafo.remover_aresta(1, 2)
#     # print(grafo.lista)  # Deve exibir {1: [], 2: [3], 3: [2]}
#     print("Encontrando caminho euleriano (Algoritmo de Fleury)...")
#     caminho = fleury(grafo)
#     print(f"Caminho euleriano encontrado: {caminho}")
#     # print("Detectando pontes usando o método naive...")
#     # pontes = naive(grafo)
#     # print(f"Pontes encontradas: {pontes}")


def menu():
    print("\nMenu de Operações no Grafo")
    print("1 - Adicionar aresta")
    print("2 - Remover aresta")
    print("3 - Exibir representação")
    print("4 - Rotular vértice")
    print("5 - Rotular aresta")
    print("6 - Ponderar vértice")
    print("7 - Ponderar aresta")
    print("8 - Checar adjacência entre vértices")
    print("9 - Checar adjacência entre arestas")
    print("10 - Verificar existência de aresta")
    print("11 - Checar quantidade de vértices")
    print("12 - Checar quantidade de arestas")
    print("13 - Verificar se o grafo é vazio")
    print("14 - Verificar se o grafo é completo")
    print("15 - Verificar conectividade (simplesmente conexo, semi-forte, forte)")
    print("16 - Detectar componentes fortemente conexos (Kosaraju)")
    print("17 - Detectar pontes (Naive)")
    print("18 - Detectar pontes (Tarjan)")
    print("19 - Detectar articulações")
    print("20 - Encontrar caminho euleriano (Algoritmo de Fleury)")
    print("21 - Exportar grafo para arquivo (Gephi)")
    print("22 - Exibir vértices")
    print("23 - Exibir arestas")
    print("24 - Buscar em Profundidade (DFS)")
    print("25 - Sair")

def main():

    num_vertices = int(input("Digite o número de vértices do grafo: "))
    
    direcionado = input("O grafo é direcionado? (s/n): ").strip().lower() == 's'
    grafo = Grafo(num_vertices, direcionado)

    while True:
        menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':  
            u = int(input("Digite o vértice de origem: "))
            v = int(input("Digite o vértice de destino: "))
            grafo.adicionar_aresta(u, v)
            print(f"Aresta entre {u} e {v} adicionada na lista de adjacência.")

        elif opcao == '2':  
            print("\nPosições onde você pode remover arestas (lista de adjacência):")
            u = int(input("Digite o vértice de origem: "))
            v = int(input("Digite o vértice de destino: "))
            grafo.remover_aresta(u, v)
            print(f"Aresta entre {u} e {v} removida da lista de adjacência.")

        elif opcao == '3':
            tipo = input("Qual tipo de representação deseja visualizar? \n1 - Matriz de Incidência \n2 - Matriz de Adjacência \n3 - Lista de Adjacência ").strip()
            
            if tipo == "1":
                print("Matriz de Incidencia")
                grafo.exibir_matriz_incidencia()
            elif tipo == "2":
                print("Matriz de Adjacência")
                grafo.exibir_matriz_adjacencia()
            elif tipo == "3":
                print("Lista de Adjacência")
                grafo.exibir_lista()
            
        elif opcao == '4':  
            vertice = int(input("Digite o vértice que deseja rotular: "))
            rotulo = input("Digite o novo rótulo: ")
            rotular_vertice(grafo, vertice, rotulo)
            print(f"Vértice {vertice} rotulado como '{rotulo}'.")

        elif opcao == '5':  
            u = int(input("Digite o vértice de origem da aresta: "))
            v = int(input("Digite o vértice de destino da aresta: "))
            rotulo = input("Digite o novo rótulo: ")
            rotular_aresta(grafo, u, v, rotulo)
            print(f"Aresta entre {u} e {v} rotulada como '{rotulo}'.")


        elif opcao == '6':  
            vertice = int(input("Digite o vértice que deseja ponderar: "))
            peso = float(input("Digite o novo peso: "))
            ponderar_vertice(grafo, vertice, peso)
            print(f"Vértice {vertice} ponderado com peso '{peso}'.")

        elif opcao == '7':  
            u = int(input("Digite o vértice de origem da aresta: "))
            v = int(input("Digite o vértice de destino da aresta: "))
            peso = float(input("Digite o novo peso: "))
            ponderar_aresta(grafo, u, v, peso)
            print(f"Aresta entre {u} e {v} ponderada com peso '{peso}'.")

        elif opcao == '8':  
            u = int(input("Digite o primeiro vértice: "))
            v = int(input("Digite o segundo vértice: "))
            adjacente = checar_adjacencia_vertices(grafo, u, v)
            print("Vértices adjacentes." if adjacente else "Vértices não são adjacentes.")
        
        elif opcao == '9':  
            u = int(input("Digite o índice da primeira aresta: "))
            v = int(input("Digite o índice da segunda aresta: "))
            adjacente = checar_adjacencia_arestas(grafo, u, v)
            print("Arestas adjacentes." if adjacente else "Arestas não são adjacentes.")

        elif opcao == '10':  
            u = int(input("Digite o vértice de origem: "))
            v = int(input("Digite o vértice de destino: "))
            existe = existe_aresta(grafo, u, v)
            print("Aresta existe." if existe else "Aresta não existe.")
        
        elif opcao == '11':  
            print(f"Quantidade de vértices: {quantidade_vertices(grafo)}")
        
        elif opcao == '12':  
            print(f"Quantidade de arestas: {quantidade_arestas(grafo)}")
        
        elif opcao == '13':  
            print("O grafo está vazio." if grafo_vazio(grafo) else "O grafo não está vazio.")
        
        elif opcao == '14':  
            print("O grafo é completo." if grafo_completo(grafo) else "O grafo não é completo.")
        
        elif opcao == '15':  
            conectividade = verifica_conectividade(grafo)
            print(f"Conectividade: {conectividade}")
        
        elif opcao == '16':  
            componentes = grafo.detectar_componentes_fortemente_conexos()
            print(f"Componentes fortemente conexos: {componentes}")
        
        elif opcao == '17':  
            print("Detectando pontes usando o método naive...")
            pontes = naive(grafo)
            print(f"Pontes encontradas: {pontes}")
        
        elif opcao == '18':  
            print("Detectando pontes usando o método de Tarjan...")
            pontes = grafo.detectar_pontes_tarjan()
            print(f"Pontes encontradas: {pontes}")
        
        elif opcao == '19':  
            print("Detectando articulações...")
            articulacoes = grafo.detectar_articulacoes()
            print(f"Articulações encontradas: {articulacoes}")
        
        elif opcao == '20':  
            print("Encontrando caminho euleriano (Algoritmo de Fleury)...")
            caminho = fleury(grafo)
            print(f"Caminho euleriano encontrado: {caminho}")

        elif opcao == '21':  
            formato = input("Digite o formato de exportação (e.g., GEXF, GDF, GML): ")
            grafo.exportar_gephi(formato)
            print(f"Grafo exportado em formato {formato}.")
            
        elif opcao == '22':
            exibir_vertices(grafo)
        
        elif opcao == '23':
            exibir_arestas(grafo)

        elif opcao == '24':
            busca_profundidade(grafo)

        elif opcao == '25':  
            print("Encerrando o programa.")
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
