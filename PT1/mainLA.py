from PT1.listaAdjacencia import Grafo

def main():
    grafo = Grafo(0)
    print("Lista de Adjacência Inicial: \n")
    grafo.exibir_lista_adjacencia()

    qtd_vertices = int(input("Informe o número de vértices para adicionar ao grafo: "))
    grafo.adicionar_vertices(qtd_vertices)
    print("\nLista de Adjacência Após Adicionar Vértices:")
    grafo.exibir_lista_adjacencia()

    resposta = input("Deseja que o grafo seja direcionado? (s/n): ").strip().lower()
    direcionado = resposta == 's'

    print("\nDigite as arestas no formato 'vertice1 vertice2'. Digite 'FIM' para encerrar.")
    while True:
        entrada = input("Aresta: ").strip()
        if entrada.lower() == 'fim':
            print("Encerrando a adição de arestas.")
            break

        try:
            vertice1, vertice2 = map(int, entrada.split())
            grafo.adicionar_aresta(vertice1, vertice2, direcionado)
            print(f"Aresta {'direcionada' if direcionado else 'não direcionada'} adicionada entre {vertice1} e {vertice2}.")
        except ValueError:
            print("Entrada inválida. Certifique-se de digitar dois números inteiros ou 'FIM' para encerrar.")
        except Exception as e:
            print(f"Erro: {e}")

    print("\nLista de Adjacência Após Adicionar e/ou Remover Arestas:")
    grafo.exibir_lista_adjacencia()

    grafo.ponderar_e_rotular_vertices()
    grafo.exibir_com_rotulos_e_pesos_vertices()

    grafo.ponderar_e_rotular_arestas()
    grafo.exibir_com_rotulos_e_pesos()

    while True:
        print("\nEscolha uma operação:")
        print("1. Verificar adjacência entre vértices")
        print("2. Verificar adjacência entre arestas")
        print("3. Verificar existência de uma aresta")
        print("4. Contar vértices e arestas")
        print("5. Verificar se o grafo está vazio")
        print("6. Verificar se o grafo é completo")
        print("7. Verificar conectividade do grafo")
        print("8. Checagem de quantidade de componentes fortemente conexos com Kosaraju")
        print("9. Checar se uma aresta é uma ponte por rótulo")
        print("10. Checar se uma aresta é uma ponte por vértices")
        print("11. Encontrar todas as pontes (Tarjan)")
        print("12. Sair")

        escolha = input("Digite sua escolha: ").strip()

        if escolha == "1":
            vertice1 = int(input("Digite o primeiro vértice: "))
            vertice2 = int(input("Digite o segundo vértice: "))
            try:
                adjacente = grafo.checar_adjacencia_vertices(vertice1, vertice2)
                print(f"{vertice1} e {vertice2} são adjacentes." if adjacente else f"{vertice1} e {vertice2} não são adjacentes.")
            except ValueError as e:
                print(f"Erro: {e}")
        elif escolha == "2":
            try:
                aresta1 = tuple(map(int, input("Digite a primeira aresta no formato 'vertice1 vertice2': ").split()))
                aresta2 = tuple(map(int, input("Digite a segunda aresta no formato 'vertice1 vertice2': ").split()))
                adjacente = grafo.checar_adjacencia_arestas(aresta1, aresta2)
                print(f"As arestas {aresta1} e {aresta2} são adjacentes." if adjacente else f"As arestas {aresta1} e {aresta2} não são adjacentes.")
            except ValueError:
                print("Erro: Entrada inválida.")
        elif escolha == "3":
            vertice1 = int(input("Digite o primeiro vértice da aresta: "))
            vertice2 = int(input("Digite o segundo vértice da aresta: "))
            try:
                existe = grafo.checar_existencia_aresta(vertice1, vertice2)
                print(f"A aresta entre {vertice1} e {vertice2} existe." if existe else f"A aresta entre {vertice1} e {vertice2} não existe.")
            except ValueError as e:
                print(f"Erro: {e}")
        elif escolha == "4":
            print(f"O grafo possui {grafo.contar_vertices()} vértices e {grafo.contar_arestas()} arestas.")
        elif escolha == "5":
            vazio = grafo.checar_vazio()
            print("O grafo está vazio." if vazio else "O grafo não está vazio.")
        elif escolha == "6":
            completo = grafo.checar_completo()
            print("O grafo é completo." if completo else "O grafo não é completo.")
        elif escolha == "7":
            conectividade = grafo.checar_conectividade()
            print(f"O grafo é {conectividade}.")
        elif escolha == "8":
            componentes = grafo.kosaraju()
            print(f"Componentes fortemente conexos encontrados: {componentes}")
        elif escolha == "9":
            rotulo = input("Digite o rótulo da aresta para verificar se é uma ponte: ").strip()
            grafo.checar_pontes_por_rotulo(rotulo)
        elif escolha == "10":
            vertice1 = int(input("Digite o primeiro vértice da aresta: "))
            vertice2 = int(input("Digite o segundo vértice da aresta: "))
            grafo.checar_pontes_por_vertices(vertice1, vertice2)
        elif escolha == "11":
            pontes = grafo.encontrar_pontes_tarjan()
            print("Pontes encontradas:")
            for ponte in pontes:
                print(ponte)
        elif escolha == "12":
            print("Encerrando o programa.")
            break
        else:
            print("Escolha inválida. Tente novamente.")

if __name__ == "__main__":
    main()
