import random
import time

# --- Ordenação por Seleção ---
def ordenacao_selecao(lista):
    n = len(lista)
    for i in range(n):
        minimo = i
        for j in range(i+1, n):
            if lista[j] < lista[minimo]:
                minimo = j
        if minimo != i:
            lista[i], lista[minimo] = lista[minimo], lista[i]
    return lista

# --- Quicksort recursivo ---
def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivo = lista[0]
    menores = [x for x in lista[1:] if x <= pivo]
    maiores = [x for x in lista[1:] if x > pivo]
    return quicksort(menores) + [pivo] + quicksort(maiores)

# --- Pesquisa Sequencial ---
def pesquisa_sequencial(lista, valor):
    comparacoes = 0
    for i, elemento in enumerate(lista):
        comparacoes += 1
        if elemento == valor:
            return i, comparacoes
    return -1, comparacoes

# --- Pesquisa Binária ---
def pesquisa_binaria(lista, valor):
    esquerda, direita = 0, len(lista) - 1
    comparacoes = 0
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        comparacoes += 1
        if lista[meio] == valor:
            return meio, comparacoes
        elif lista[meio] < valor:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1, comparacoes

# --- Programa principal ---
# Gerar lista aleatória
lista = random.sample(range(1, 10001), 1000)
valor = 1000

# Ordenação e medição de tempo
# Seleção
start_sel = time.time()
lista_sel = lista.copy()
ordenacao_selecao(lista_sel)
fim_sel = time.time()

# Quicksort
start_qs = time.time()
lista_qs = quicksort(lista.copy())
fim_qs = time.time()

# Sorted
start_sorted = time.time()
lista_sorted = sorted(lista.copy())
fim_sorted = time.time()

# Busca
# Sequencial
indice_seq, comp_seq = pesquisa_sequencial(lista_sorted, valor)
# Binária
indice_bin, comp_bin = pesquisa_binaria(lista_sorted, valor)

# --- Mostrar resultados ---
print("\n--- Tabela de Tempos de Ordenação ---")
print(f"{'Método':<15} {'Tempo (s)':<10}")
print(f"{'Seleção':<15} {fim_sel - start_sel:<10.6f}")
print(f"{'Quicksort':<15} {fim_qs - start_qs:<10.6f}")
print(f"{'Sorted()':<15} {fim_sorted - start_sorted:<10.6f}")

print("\n--- Resultados da Busca ---")
print(f"{'Método':<20} {'Índice':<10} {'Comparações':<10}")
print(f"{'Sequencial':<20} {indice_seq:<10} {comp_seq:<10}")
print(f"{'Binária':<20} {indice_bin:<10} {comp_bin:<10}")
