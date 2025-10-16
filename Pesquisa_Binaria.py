# Pesquisa Sequencial
def pesquisa_sequencial(lista, valor):
    comparacoes = 0
    for i, elemento in enumerate(lista):
        comparacoes += 1
        if elemento == valor:
            print(f"Valor encontrado no índice {i} após {comparacoes} comparações")
            return i
    print(f"Valor não encontrado após {comparacoes} comparações")
    return -1

# Pesquisa Binária (lista deve estar ordenada)
def pesquisa_binaria(lista, valor):
    esquerda, direita = 0, len(lista) - 1
    comparacoes = 0
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        comparacoes += 1
        if lista[meio] == valor:
            print(f"Valor encontrado no índice {meio} após {comparacoes} comparações")
            return meio
        elif lista[meio] < valor:
            esquerda = meio + 1
        else:
            direita = meio - 1
    print(f"Valor não encontrado após {comparacoes} comparações")
    return -1

# Comparação de tempo
import time

lista100 = list(range(1, 101))

# Teste pesquisa sequencial
start = time.time()
pesquisa_sequencial(lista100, 100)
end = time.time()
print(f"Tempo pesquisa sequencial: {end - start:.6f} s")

# Teste pesquisa binária
start = time.time()
pesquisa_binaria(lista100, 100)
end = time.time()
print(f"Tempo pesquisa binária: {end - start:.6f} s")
