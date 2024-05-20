# Importa o módulo Decimal da biblioteca decimal
from decimal import Decimal

# Exemplo de operações com inteiros, floats e Decimals em Python

# Operações com inteiros
soma_inteiros = 7 + 3
print("Soma de inteiros:", soma_inteiros)

# Operações com floats
soma_floats = 6.5 + 3.2
print("Soma de floats:", soma_floats)

# Operações com Decimals
soma_decimals = Decimal('10.1') + Decimal('20.2')
print("Soma de Decimals:", soma_decimals)

# Multiplicação com diferentes tipos
multiplicacao_mista = 5 * Decimal('3.5')
print("Multiplicação mista (int * Decimal):", multiplicacao_mista)

# Divisão com floats
divisao_floats = 8.4 / 2.1
print("Divisão com floats:", divisao_floats)

# Exponenciação com inteiros
exponenciacao_inteiros = 2 ** 5
print("Exponenciação com inteiros:", exponenciacao_inteiros)

# Módulo com inteiros
modulo_inteiros = 9 % 4
print("Módulo com inteiros:", modulo_inteiros)

# Precisão com Decimals em operações financeiras
juros = Decimal('0.05') * Decimal('1000.00')
print("Cálculo de juros com Decimal:", juros)
