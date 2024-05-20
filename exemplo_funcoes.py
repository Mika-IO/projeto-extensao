# Exemplo de funções em Python

# Definição de uma função simples
def saudacao():
    print("Olá, mundo!")

# Chamando a função saudacao
saudacao()

# Função com parâmetros
def cumprimentar(nome):
    print(f"Olá, {nome}!")

# Chamando a função cumprimentar com um argumento
cumprimentar("Maria")

# Função com retorno de valor
def soma(a, b):
    return a + b

# Chamando a função soma e armazenando o resultado
resultado = soma(5, 7)
print("Resultado da soma:", resultado)

# Função com parâmetros padrão
def apresentar(nome, idade=30):
    print(f"Meu nome é {nome} e eu tenho {idade} anos.")

# Chamando a função apresentar com e sem o parâmetro idade
apresentar("João")
apresentar("Ana", 25)

# Função com número variável de argumentos (args)
def listar_numeros(*numeros):
    for numero in numeros:
        print(numero)

# Chamando a função listar_numeros com vários argumentos
listar_numeros(1, 2, 3, 4, 5)

# Função com argumentos nomeados variáveis (kwargs)
def exibir_info(**info):
    for chave, valor in info.items():
        print(f"{chave}: {valor}")

# Chamando a função exibir_info com argumentos nomeados
exibir_info(nome="Carlos", idade=40, cidade="São Paulo")
