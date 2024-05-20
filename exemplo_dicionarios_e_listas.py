# Exemplo de operações com listas em Python

# Criação de uma lista
frutas = ["maçã", "banana", "cereja"]
print("Lista de frutas:", frutas)

# Acessando elementos da lista
primeira_fruta = frutas[0]
print("Primeira fruta:", primeira_fruta)

# Adicionando elementos à lista
frutas.append("laranja")
print("Lista após adicionar laranja:", frutas)

# Inserindo elementos em uma posição específica
frutas.insert(1, "morango")
print("Lista após inserir morango na posição 1:", frutas)

# Removendo elementos da lista
frutas.remove("banana")
print("Lista após remover banana:", frutas)

# Removendo o último elemento da lista
ultima_fruta = frutas.pop()
print("Lista após remover a última fruta:", frutas)
print("Última fruta removida:", ultima_fruta)

# Encontrando o índice de um elemento
indice_cereja = frutas.index("cereja")
print("Índice de cereja:", indice_cereja)

# Ordenando a lista
frutas.sort()
print("Lista ordenada:", frutas)

# Exemplo de operações com dicionários em Python

# Criação de um dicionário
pessoas = {"Alice": 25, "Bob": 30, "Charlie": 35}
print("Dicionário de pessoas:", pessoas)

# Acessando valores no dicionário
idade_alice = pessoas["Alice"]
print("Idade de Alice:", idade_alice)

# Adicionando um novo par chave-valor
pessoas["David"] = 40
print("Dicionário após adicionar David:", pessoas)

# Atualizando um valor existente
pessoas["Alice"] = 26
print("Dicionário após atualizar a idade de Alice:", pessoas)

# Removendo um par chave-valor
del pessoas["Bob"]
print("Dicionário após remover Bob:", pessoas)

# Iterando sobre chaves e valores
for nome, idade in pessoas.items():
    print(f"{nome} tem {idade} anos.")

# Verificando se uma chave existe no dicionário
existe_charlie = "Charlie" in pessoas
print("Charlie está no dicionário:", existe_charlie)

# Obtendo todas as chaves e valores
chaves = list(pessoas.keys())
valores = list(pessoas.values())
print("Chaves do dicionário:", chaves)
print("Valores do dicionário:", valores)
