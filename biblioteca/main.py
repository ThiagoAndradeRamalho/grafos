from grafo import Grafo
from manipulacao import *

def main():

    # num_vertices = int(input("Digite o número de vértices para o grafo aleatório: "))
    # num_arestas = int(input("Digite o número de arestas para o grafo aleatório: "))
    # direcionado = input("O grafo é direcionado? (s/n): ").strip().lower() == "s"
    # grafo_aleatorio = gerar_grafo_aleatorio(num_vertices,num_arestas, direcionado)
    # grafo_aleatorio.exibir_lista()
    # grafo_aleatorio.exibir_matriz_adjacencia()

    grafo = Grafo(True)

    # grafo.adicionar_vertice("s")
    # grafo.adicionar_vertice("a")
    # # grafo.adicionar_vertice("b")
    # # grafo.adicionar_vertice("t")
    # grafo.adicionar_aresta('s','a', 'e1')
    # grafo.adicionar_aresta('b','a', 'e2')
    
    # grafo.remover_aresta(rotulo='e1')
    # grafo.adicionar_aresta('a','s', 'e2')
    # grafo.adicionar_aresta('s','a', 'e3')
    # grafo.adicionar_aresta('3','s', 'e5')
    # grafo.adicionar_aresta('3','s', 'e4')
    # grafo.exibir_lista()

    # print(verifica_conectividade(grafo))

    # grafo.exibir_matriz_adjacencia()

    # print(fleury_naive(grafo))

    # pontes = naive(grafo_aleatorio)
    # print(f"Pontes encontradas: {pontes}")

    # grafo_carregado = carregar_grafo_gexf("ab.gexf")
    # grafo_carregado.exibir_lista()
    # try:
    #     nome_arquivo = "aa.gexf"
    #     grafo_importado = importar_de_gexf(nome_arquivo)  # Chamada correta do @classmethod
    #     print("Grafo importado com sucesso!")
    #     grafo_importado.exibir_lista()  # Exibe a lista de adjacência do grafo importado
    # except Exception as e:
    #     print(f"Erro ao importar o grafo: {e}")
    # grafo.exibir_matriz_adjacencia()  
    # grafo.exibir_matriz_incidencia()
    # grafo.checar_adjacencia_vertices('a','s')
    # grafo.checar_adjacencia_arestas("e2", 'e3')
    # print(grafo.existe_aresta('3','t'))
    # print(quantidade_vertices(grafo))
    # print(quantidade_arestas(grafo))
    # print(busca_profundidade_componentes(grafo))

    # print(grafo_vazio(grafo))
    # print(grafo_completo(grafo))
    # print(verifica_conectividade(grafo))
    # print(kosaraju(grafo))
    # print(naive(grafo))
    # print(tarjan(grafo))
    # print("Componentes conexos: ",numero_componentes_conexos(grafo))



    # grafo.adicionar_aresta(0, 1)
    # grafo.adicionar_aresta(0, 3)
    # grafo.adicionar_aresta(1, 2)
    # grafo.adicionar_aresta(2, 3)
    # print(grafo.direcionado)
    # print(grafo.exibir_lista)
    # grafo.remover_aresta(1, 2)
    # print(grafo.lista)  # Deve exibir {1: [], 2: [3], 3: [2]}
    # print("Encontrando caminho euleriano (Algoritmo de Fleury)...")
    # caminho = fleury(grafo)
    # print(f"Caminho euleriano encontrado: {caminho}")
    # print("Detectando pontes usando o método naive...")
    # pontes = naive(grafo)
    # print(f"Pontes encontradas: {pontes}")


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
    print("17 - Detectar pontes ")
    print("18 - Detectar pontes (Tarjan)")
    print("19 - Detectar articulações")
    print("20 - Encontrar caminho euleriano (Algoritmo de Fleury)")
    print("21 - Exportar grafo para arquivo (Gephi)")
    print("22 - Exibir vértices")
    print("23 - Exibir arestas")
    print("24 - Buscar em Profundidade (DFS)")
    print("26 - Importar arquivo")
    print("25 - Adicionar vertice")
    print("0 - Encerrar")

def main():

    num_vertices = int(input("Digite o número de vértices do grafo: "))
    direcionado = input("O grafo é direcionado? (s/n): ").strip().lower() == 's'
    grafo = Grafo(direcionado=direcionado, num_vertices=num_vertices)

    while True:
        menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':  
            print("Digite as arestas para adicionar no formato (u, v). Digite 'FIM' para encerrar.")
            while True:
                entrada = input("Digite a aresta (ou 'FIM' para encerrar): ").strip()
                if entrada.upper() == "FIM":
                    break
                try:
                    # Remove parênteses e espaços extras
                    entrada = entrada.replace("(", "").replace(")", "").replace(" ", "")
                    partes = entrada.split(",")
                    
                    if len(partes) != 2:
                        raise ValueError("A entrada deve conter dois valores separados por vírgula.")
                    
                    u, v = partes
                    rotulo = input("Digite o rótulo da aresta (ou pressione Enter para não rotular): ").strip()
                    grafo.adicionar_aresta(u, v, rotulo if rotulo else None)
                except ValueError as e:
                    print(f"Entrada inválida! {e}")


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
            ponderar_vertice(vertice, peso)
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
            componentes = kosaraju(grafo)
            if componentes is not None:
                print("Componentes Fortemente Conexas:")
                for i, componente in enumerate(componentes, start=1):
                    print(f"Componente {i}: {componente}")
            else:
                print("O algoritmo Kosaraju não pode ser executado para este tipo de grafo.")

        
        elif opcao == '17':  
            print("Detectando pontes usando o método naive...")
            pontes = naive(grafo)
            print(f"Pontes encontradas: {pontes}")
        
        elif opcao == '18':  
            print("Detectando pontes usando o método de Tarjan...")
            pontes = tarjan(grafo)
            print(f"Pontes encontradas: {pontes}")
        
        elif opcao == '19':
            v = int(input("Digite o vértice v: "))
            print("Detectando articulações...")
            if checar_articulacao(grafo, v):
                print(f"O vértice {v} é uma articulação!")
            else:
                print(f"O vértice {v} não é uma articulação.")

        elif opcao == '20':
            resultado = fleury_modificado(grafo)

            if resultado == "Não é euleriano":
                print("O grafo não é euleriano (possui mais de dois vértices de grau ímpar).")
            elif resultado == "Semi-euleriano":
                print("O grafo é semi-euleriano (possui exatamente dois vértices de grau ímpar).")
            else:
                print(f"Ciclo euleriano encontrado: {resultado}")


        elif opcao == '21':  
            nome_arquivo = input("Digite o nome do arquivo (com extensão .gexf): ").strip()
            salvar_grafo_gexf(grafo, nome_arquivo)

        elif opcao == '26':  
            nome_arquivo = input("Digite o nome do arquivo GEXF para carregar: ").strip()
            try:
                grafo_carregado = carregar_grafo_gexf(nome_arquivo)
                grafo_carregado.exibir_lista() 
                print(f"Grafo carregado com sucesso a partir de {nome_arquivo}.")
            except Exception as e:
                print(f"Erro ao carregar o grafo: {e}")
            
        elif opcao == '22':
            exibir_vertices(grafo)
        
        elif opcao == '23':
            exibir_arestas(grafo)

        elif opcao == '24':
            busca_profundidade(grafo)

        elif opcao == '25':  # Nova opção para adicionar vértice
            vertice = input("Digite o nome do vértice: ").strip()
            grafo.adicionar_vertice(vertice)

        elif opcao == '0':  
            print("Encerrando o programa.")
            break
        

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()