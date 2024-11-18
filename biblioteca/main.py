from representacoes.matriz_adjacencia import GrafoMatrizAdjacencia
from representacoes.matriz_incidencia import GrafoMatrizIncidencia
from representacoes.lista_adjacencia import GrafoListaAdjacencia
from manipulacao import *

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
    print("Escolha o tipo de representação do grafo:")
    print("1 - Matriz de Adjacência")
    print("2 - Matriz de Incidência")
    print("3 - Lista de Adjacência")
    tipo = input("Digite o número da opção desejada: ").strip()

    num_vertices = int(input("Digite o número de vértices do grafo: "))
    
    if tipo == '1':
        grafo = GrafoMatrizAdjacencia(num_vertices)
        tipo_grafo = "adjacência"
    elif tipo == '2':
        num_arestas = int(input("Digite o número de arestas do grafo: "))
        direcionado = input("O grafo é direcionado? (s/n): ").strip().lower() == 's'
        grafo = GrafoMatrizIncidencia(num_vertices, num_arestas)
        tipo_grafo = "incidência direcionada" if direcionado else "incidência não direcionada"
    elif tipo == '3':
        direcionado = input("O grafo é direcionado? (s/n): ").strip().lower() == 's'
        grafo = GrafoListaAdjacencia(num_vertices, direcionado)
        tipo_grafo = "lista de adjacência direcionada" if direcionado else "lista de adjacência não direcionada"
    else:
        print("Opção inválida! Encerrando o programa.")
        return
    
    while True:
        menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':  
            u = int(input("Digite o vértice de origem: "))
            v = int(input("Digite o vértice de destino: "))
            if tipo == '1':
                grafo.adicionar_aresta(u, v)
                print(f"Aresta entre {u} e {v} adicionada.")
            elif tipo == '2':
                e = int(input("Digite o índice da aresta: "))
                grafo.adicionar_aresta(u, v, e, direcionado)
                print(f"Aresta entre {u} e {v} na posição {e} adicionada.")
            elif tipo == '3':
                grafo.adicionar_aresta(u, v)
                print(f"Aresta entre {u} e {v} adicionada na lista de adjacência.")

        elif opcao == '2':  
            if tipo == '1':
                print("\nPosições onde você pode remover arestas (matriz de adjacência):")
                grafo.mostrar_posicoes_ocupadas()
                u = int(input("Digite o vértice de origem: "))
                v = int(input("Digite o vértice de destino: "))
                grafo.remover_aresta(u, v)
                print(f"Aresta entre {u} e {v} removida.")
                
            elif tipo == '2':
                print("\nPosições ocupadas e arestas na matriz de incidência:")
                grafo.mostrar_arestas_ocupadas() 
                e = int(input("Digite o índice da aresta: "))
                grafo.remover_aresta(e)
                print(f"Aresta na posição {e} removida.")
                
            elif tipo == '3':
                print("\nPosições onde você pode remover arestas (lista de adjacência):")
                u = int(input("Digite o vértice de origem: "))
                v = int(input("Digite o vértice de destino: "))
                grafo.remover_aresta(u, v)
                print(f"Aresta entre {u} e {v} removida da lista de adjacência.")

        elif opcao == '3':  
            print(f"\nRepresentação de {tipo_grafo.capitalize()}:")
            grafo.exibir_matriz() if tipo in ('1', '2') else grafo.exibir_lista()
            
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
            pontes = grafo.detectar_pontes_naive()
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
            caminho = grafo.encontrar_caminho_euleriano()
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
