# Fatorial recursivo
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n-1)

# Teste
for i in range(7):
    print(f"{i}! = {fatorial(i)}")

# Fibonacci recursivo
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

# Teste
for n in [0, 1, 5, 10]:
    print(f"Fibonacci({n}) = {fibonacci(n)}")

# Soma acumulada recursiva
def soma_acumulada(n):
    if n == 0:
        return 0
    return n + soma_acumulada(n-1)

print(f"Soma acumulada até 10 = {soma_acumulada(10)}")
