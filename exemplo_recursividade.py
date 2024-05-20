# Função recursiva para calcular a soma de uma lista de números
def soma_lista(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + soma_lista(lista[1:])

# Função recursiva para encontrar o maior elemento em uma lista
def maior_elemento(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        maior_do_resto = maior_elemento(lista[1:])
        return lista[0] if lista[0] > maior_do_resto else maior_do_resto

# Função recursiva para verificar se uma string é um palíndromo
def eh_palindromo(string):
    if len(string) <= 1:
        return True
    elif string[0] != string[-1]:
        return False
    else:
        return eh_palindromo(string[1:-1])

# Testando as funções recursivas
lista_numeros = [1, 2, 3, 4, 5]
string_palindromo = "radar"
string_nao_palindromo = "python"

print(f"Soma da lista {lista_numeros}:", soma_lista(lista_numeros))
print(f"Maior elemento da lista {lista_numeros}:", maior_elemento(lista_numeros))
print(f"A string '{string_palindromo}' é um palíndromo?:", eh_palindromo(string_palindromo))
print(f"A string '{string_nao_palindromo}' é um palíndromo?:", eh_palindromo(string_nao_palindromo))
