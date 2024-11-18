from LAPT2 import GrafoLA
from MAPT2 import GrafoMA
from MIPT2 import GrafoMI

def main():
    # Escolher a estrutura do grafo
    print("Qual estrutura deseja utilizar para representação do seu grafo?")
    print("1 - Lista de Adjacência")
    print("2 - Matriz de Adjacência")
    print("3 - Matriz de Incidência")
    
    escolha = int(input("Escolha a opção (1/2/3): ").strip())

    if escolha == 1:
        grafo = GrafoLA(0)  # Instancia Grafo com lista de adjacência
    elif escolha == 2:
        grafo = GrafoMA(0)  # Instancia Grafo com matriz de adjacência
    elif escolha == 3:
        grafo = GrafoMI(0)  # Instancia Grafo com matriz de incidência
    else:
        print("Opção inválida. Encerrando.")
        return

    # Exibir a estrutura inicial
    print("\nEstrutura inicial do grafo:")
    if isinstance(grafo, GrafoLA):
        print("Lista de Adjacência Inicial: \n")
        grafo.exibir_lista_adjacencia()
    elif isinstance(grafo, GrafoMA):
        print("Matriz de Adjacência Inicial: \n")
        grafo.exibir_matriz_adjacencia()
    elif isinstance(grafo, GrafoMI):
        print("Matriz de Incidência Inicial: \n")
        grafo.exibir_matriz_incidencia()

    # Adicionar vértices
    qtd_vertices = int(input("Informe o número de vértices para adicionar ao grafo: "))
    grafo.adicionar_vertices(qtd_vertices)

    print("\nEstrutura após adicionar vértices:")
    if isinstance(grafo, GrafoLA):
        grafo.exibir_lista_adjacencia()
    elif isinstance(grafo, GrafoMA):
        grafo.exibir_matriz_adjacencia()
    elif isinstance(grafo, GrafoMI):
        grafo.exibir_matriz_incidencia()

    # Perguntar se o grafo será direcionado
    resposta = input("Deseja que o grafo seja direcionado? (s/n): ").strip().lower()
    direcionado = resposta == 's'

    # Adicionar arestas
    print("\nDigite as arestas no formato 'vertice1 vertice2'. Digite 'FIM' para encerrar.")
    while True:
        entrada = input("Aresta: ").strip()
        if entrada.lower() == 'fim':
            print("Encerrando a adição de arestas.")
            break

        try:
            vertice1, vertice2 = map(int, entrada.split())
            grafo.adicionar_aresta(vertice1, vertice2)  # Passando os vértices para adicionar a aresta
            print(f"Aresta {'direcionada' if direcionado else 'não direcionada'} adicionada entre {vertice1} e {vertice2}.")
        except ValueError:
            print("Entrada inválida. Certifique-se de digitar dois números inteiros ou 'FIM' para encerrar.")
        except Exception as e:
            print(f"Erro: {e}")

    # Agora montamos a matriz de incidência
    grafo.montar_matriz_incidencia()

    print("\nEstrutura após adicionar as arestas e montar a matriz de incidência:")
    if isinstance(grafo, GrafoLA):
        grafo.exibir_lista_adjacencia()
    elif isinstance(grafo, GrafoMA):
        grafo.exibir_matriz_adjacencia()
    elif isinstance(grafo, GrafoMI):
        grafo.exibir_matriz_incidencia()

    # Encontrar as pontes usando o algoritmo de Tarjan
    pontes = grafo.encontrar_pontes_tarjan()
    print("Pontes encontradas:")
    for ponte in pontes:
        print(ponte)


if __name__ == "__main__":
    main()
