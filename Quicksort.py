# Ordenação por Seleção
def ordenacao_selecao(lista):
    n = len(lista)
    for i in range(n):
        minimo = i
        for j in range(i+1, n):
            if lista[j] < lista[minimo]:
                minimo = j
        if minimo != i:
            print(f"Trocando {lista[i]} por {lista[minimo]}")
            lista[i], lista[minimo] = lista[minimo], lista[i]
    return lista

# Quicksort recursivo
def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivo = lista[0]
    menores = [x for x in lista[1:] if x <= pivo]
    maiores = [x for x in lista[1:] if x > pivo]
    return quicksort(menores) + [pivo] + quicksort(maiores)

# Comparação de tempo
import random
import time

lista = random.sample(range(1, 100_000), 10_000)
start = time.time()
ordenacao_selecao(lista.copy())
fim_sel = time.time()

start2 = time.time()
quicksort(lista.copy())
fim_qs = time.time()

print(f"Seleção: {fim_sel:.6f}s | Quicksort: {fim_qs:.6f}s")

# O Quicksort é considerado mais eficiente em média que o método da ordenação por seleção porque utiliza a técnica de dividir e conquistar. Enquanto a ordenação por seleção percorre toda a lista repetidamente para encontrar o menor elemento a cada passo, o Quicksort escolhe um pivô, divide a lista em duas sublistas (uma com elementos menores e outra com elementos maiores que o pivô) e ordena recursivamente essas sublistas.

