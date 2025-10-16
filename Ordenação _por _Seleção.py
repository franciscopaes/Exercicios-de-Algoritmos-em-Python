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

# Teste
numeros = [64, 25, 12, 22, 11]
ordenacao_selecao(numeros.copy())

# Comparação com sorted()
import time
import random

lista = random.sample(range(1, 2000), 1000)

start = time.time()
ordenacao_selecao(lista.copy())
fim_sel = time.time()

start2 = time.time()
sorted(lista.copy())
fim_sorted = time.time()

print(f"Tempo seleção: {fim_sel - start:.6f} s | Tempo sorted: {fim_sorted - start2:.6f} s")
