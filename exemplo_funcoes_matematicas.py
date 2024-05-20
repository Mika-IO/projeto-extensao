# Função para somar dois números
def soma(a, b):
    return a + b

# Função para subtrair dois números
def subtracao(a, b):
    return a - b

# Função para multiplicar dois números
def multiplicacao(a, b):
    return a * b

# Função para dividir dois números
def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b

# Função para calcular a exponenciação
def exponenciacao(base, expoente):
    return base ** expoente

# Função para calcular a raiz quadrada usando o método de Newton-Raphson
def raiz_quadrada(numero, precisao=1e-10):
    if numero < 0:
        return "Erro: número negativo"
    aproximacao = numero / 2.0
    while True:
        melhor_aproximacao = (aproximacao + numero / aproximacao) / 2.0
        if abs(aproximacao - melhor_aproximacao) < precisao:
            return melhor_aproximacao
        aproximacao = melhor_aproximacao

# Função para calcular o seno de um ângulo (em radianos) usando a série de Taylor
def seno(angulo, termos=10):
    seno_aproximado = 0
    for n in range(termos):
        termo = ((-1)**n) * (angulo**(2*n + 1)) / fatorial(2*n + 1)
        seno_aproximado += termo
    return seno_aproximado

# Função para calcular o cosseno de um ângulo (em radianos) usando a série de Taylor
def cosseno(angulo, termos=10):
    cosseno_aproximado = 0
    for n in range(termos):
        termo = ((-1)**n) * (angulo**(2*n)) / fatorial(2*n)
        cosseno_aproximado += termo
    return cosseno_aproximado

# Função para calcular o logaritmo natural usando a série de Taylor
def logaritmo(numero, termos=100):
    if numero <= 0:
        return "Erro: número não positivo"
    n = (numero - 1) / (numero + 1)
    logaritmo_aproximado = 0
    for k in range(termos):
        termo = (1 / (2 * k + 1)) * (n**(2 * k + 1))
        logaritmo_aproximado += termo
    return 2 * logaritmo_aproximado

# Função para calcular o fatorial
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

# Testando as funções matemáticas
a = 10
b = 5
angulo = 3.14159 / 6  # 30 graus em radianos

print("Soma:", soma(a, b))
print("Subtração:", subtracao(a, b))
print("Multiplicação:", multiplicacao(a, b))
print("Divisão:", divisao(a, b))
print("Exponenciação:", exponenciacao(a, 2))
print("Raiz quadrada de 25:", raiz_quadrada(25))
print("Seno de 30 graus:", seno(angulo))
print("Cosseno de 30 graus:", cosseno(angulo))
print("Logaritmo natural de 10:", logaritmo(a))
