import random

# --- Função soma acumulada recursiva ---
def soma_lista_recursiva(lista):
    """Retorna a soma de todos os elementos da lista usando recursão"""
    if not lista:  # Caso base: lista vazia
        return 0
    return lista[0] + soma_lista_recursiva(lista[1:])

# --- Quicksort recursivo ---
def quicksort(lista):
    """Ordena uma lista usando quicksort recursivo"""
    if len(lista) <= 1:
        return lista
    pivo = lista[0]
    menores = [x for x in lista[1:] if x <= pivo]
    maiores = [x for x in lista[1:] if x > pivo]
    return quicksort(menores) + [pivo] + quicksort(maiores)

# --- Pesquisa binária recursiva ---
def pesquisa_binaria_rec(lista, valor, esquerda=0, direita=None, comparacoes=0):
    """Retorna índice do valor e número de comparações"""
    if direita is None:
        direita = len(lista) - 1
    if esquerda > direita:
        return -1, comparacoes
    meio = (esquerda + direita) // 2
    comparacoes += 1
    if lista[meio] == valor:
        return meio, comparacoes
    elif lista[meio] < valor:
        return pesquisa_binaria_rec(lista, valor, meio+1, direita, comparacoes)
    else:
        return pesquisa_binaria_rec(lista, valor, esquerda, meio-1, comparacoes)

# --- Fatorial recursivo ---
def fatorial(n):
    """Calcula fatorial de n recursivamente"""
    if n <= 1:
        return 1
    return n * fatorial(n-1)

# --- Fibonacci recursivo ---
def fibonacci(n):
    """Retorna o n-ésimo termo da sequência de Fibonacci"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

# --- Programa principal ---
# Gerar lista com 20 números aleatórios entre 1 e 200
lista = random.sample(range(1, 201), 20)
print("Lista original:", lista)

# Soma acumulada recursiva
soma_total = soma_lista_recursiva(lista)
print("Soma acumulada dos elementos (recursiva):", soma_total)

# Ordenação com quicksort
lista_ordenada = quicksort(lista)
print("Lista ordenada com Quicksort:", lista_ordenada)

# Pesquisa binária recursiva do valor 100
indice, comparacoes = pesquisa_binaria_rec(lista_ordenada, 100)
if indice != -1:
    print(f"Valor 100 encontrado no índice {indice} após {comparacoes} comparações")
else:
    print(f"Valor 100 não encontrado após {comparacoes} comparações")

# Fatorial do maior número da lista
maior = max(lista)
fatorial_maior = fatorial(maior)
print(f"Fatorial do maior número ({maior}): {fatorial_maior}")

# n-ésimo Fibonacci, n = tamanho da lista
n = len(lista)
fib_n = fibonacci(n)
print(f"{n}-ésimo termo da sequência de Fibonacci: {fib_n}")

# --- Análise de complexidade ---
print("\n--- Complexidade das funções ---")
print("Soma recursiva: O(n) -> percorre todos os elementos da lista")
print("Quicksort: O(n log n) média, O(n²) pior caso -> divide e conquista")
print("Pesquisa binária recursiva: O(log n) -> divide lista ao meio")
print("Fatorial recursivo: O(n) -> n chamadas recursivas")
print("Fibonacci recursivo simples: O(2^n) -> recursão exponencial")
