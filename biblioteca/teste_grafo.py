import time
from manipulacao import gerar_grafo_aleatorio, tarjan, naive


def medir_tempo(func, *args):
    inicio = time.time()
    resultado = func(*args)
    fim = time.time()
    return fim - inicio, resultado

def rodar_testes():
    print("Iniciando testes...")  # Confirmação de execução
    tamanhos = [100, 1000, 10000, 100000]  # Lista com os tamanhos dos grafos a serem testados
    
    # Lista para armazenar os resultados
    resultados = []

    for tamanho in tamanhos:
        # Calcula a quantidade de arestas como metade da quantidade de vértices
        num_arestas = tamanho // 2  
        print(f"\nGerando grafo com {tamanho} vértices e {num_arestas} arestas...")

        grafo = gerar_grafo_aleatorio(tamanho, num_arestas, direcionado=False)

        print("Executando Tarjan...")
        tempo_tarjan, _ = medir_tempo(tarjan, grafo)
        print(f"Tarjan para {tamanho} vértices: {tempo_tarjan:.4f} segundos")

        print("Executando Naive...")
        tempo_naive, _ = medir_tempo(naive, grafo)
        print(f"Naive para {tamanho} vértices: {tempo_naive:.4f} segundos")

        # Armazena os resultados do teste
        resultados.append({
            "vertices": tamanho,
            "arestas": num_arestas,
            "tempo_tarjan": tempo_tarjan,
            "tempo_naive": tempo_naive
        })

    # Exibir resumo dos resultados
    print("\nResumo dos testes:")
    print(f"{'Vértices':<10}{'Arestas':<10}{'Tarjan (s)':<15}{'Naive (s)':<15}")
    print("-" * 50)
    for res in resultados:
        print(f"{res['vertices']:<10}{res['arestas']:<10}{res['tempo_tarjan']:<15.4f}{res['tempo_naive']:<15.4f}")

if __name__ == "__main__":
    rodar_testes()
