# Função recursiva para calcular o n-ésimo número de Fibonacci
def fibonacci_recursivo(n):
    if n <= 0:
        return "Erro: n deve ser um número inteiro positivo"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

# Função iterativa para calcular a sequência de Fibonacci até o n-ésimo termo
def fibonacci_iterativo(n):
    if n <= 0:
        return "Erro: n deve ser um número inteiro positivo"
    sequencia = [0, 1]
    for i in range(2, n):
        sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia[:n]

# Testando as funções de Fibonacci
n = 10
print(f"O {n}-ésimo número de Fibonacci (recursivo):", fibonacci_recursivo(n))
print(f"Sequência de Fibonacci até o {n}-ésimo termo (iterativo):", fibonacci_iterativo(n))
