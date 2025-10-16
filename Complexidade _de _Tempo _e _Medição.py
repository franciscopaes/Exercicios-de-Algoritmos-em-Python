# Comparando tempos de pesquisa em listas grandes
import time
import random

# --- Função pesquisa sequencial ---
def pesquisa_sequencial(lista, valor):
    comparacoes = 0
    for i, elemento in enumerate(lista):
        comparacoes += 1
        if elemento == valor:
            # print(f"Valor encontrado no índice {i} após {comparacoes} comparações")
            return i
    # print(f"Valor não encontrado após {comparacoes} comparações")
    return -1

# --- Função pesquisa binária (lista deve estar ordenada) ---
def pesquisa_binaria(lista, valor):
    esquerda, direita = 0, len(lista) - 1
    comparacoes = 0
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        comparacoes += 1
        if lista[meio] == valor:
            # print(f"Valor encontrado no índice {meio} após {comparacoes} comparações")
            return meio
        elif lista[meio] < valor:
            esquerda = meio + 1
        else:
            direita = meio - 1
    # print(f"Valor não encontrado após {comparacoes} comparações")
    return -1

# --- Função para medir tempo ---
def medir_tempo(lista, valor):
    # Pesquisa sequencial
    start = time.time()
    pesquisa_sequencial(lista, valor)
    fim_seq = time.time()
    
    # Pesquisa binária (lista precisa estar ordenada)
    lista_ordenada = sorted(lista)
    start_bin = time.time()
    pesquisa_binaria(lista_ordenada, valor)
    fim_bin = time.time()
    
    print(f"Sequencial: {fim_seq - start:.6f} s | Binária: {fim_bin - start_bin:.6f} s")

# --- Teste com listas grandes ---
tamanhos = [10_000, 100_000, 1_000_000]
for n in tamanhos:
    lista = random.sample(range(1, n*2), n)
    print(f"\nLista com {n} elementos:")
    medir_tempo(lista, lista[-1])
