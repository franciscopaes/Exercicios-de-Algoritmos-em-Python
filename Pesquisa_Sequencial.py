# Pesquisa Sequencial
# Objetivo: Buscar um valor em uma lista verificando elemento por elemento

def pesquisa_sequencial(lista, valor):
    comparacoes = 0  # Contador de comparações
    for i, elemento in enumerate(lista):
        comparacoes += 1
        if elemento == valor:
            print(f"Valor encontrado no índice {i} após {comparacoes} comparações")
            return i
    print(f"Valor não encontrado após {comparacoes} comparações")
    return -1

# Teste
numeros = [5, 8, 2, 9, 1, 6, 7, 3, 0, 4]
pesquisa_sequencial(numeros, 6)
pesquisa_sequencial(numeros, 10)
