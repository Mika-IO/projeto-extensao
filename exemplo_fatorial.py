# Função recursiva para calcular o fatorial de um número
def fatorial_recursivo(n):
    if n < 0:
        return "Erro: n deve ser um número inteiro não negativo"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * fatorial_recursivo(n - 1)

# Função iterativa para calcular o fatorial de um número
def fatorial_iterativo(n):
    if n < 0:
        return "Erro: n deve ser um número inteiro não negativo"
    fatorial = 1
    for i in range(2, n + 1):
        fatorial *= i
    return fatorial

# Testando as funções de fatorial
n = 5
print(f"Fatorial de {n} (recursivo):", fatorial_recursivo(n))
print(f"Fatorial de {n} (iterativo):", fatorial_iterativo(n))
