# Exemplo de manipulação de strings em Python

# Concatenação de strings
saudacao = "Olá" + ", " + "mundo!"
print("Concatenação:", saudacao)

# Interpolação de strings com f-string
nome = "Maria"
mensagem = f"Bem-vinda, {nome}!"
print("Interpolação com f-string:", mensagem)

# Métodos de string
texto = "Python é incrível"
print("Texto em maiúsculas:", texto.upper())
print("Texto em minúsculas:", texto.lower())
print("Texto capitalizado:", texto.capitalize())
print("Texto título:", texto.title())

# Substituição de substrings
novo_texto = texto.replace("incrível", "fantástico")
print("Texto substituído:", novo_texto)

# Divisão e junção de strings
palavras = texto.split()
print("Palavras:", palavras)
texto_junto = ' '.join(palavras)
print("Texto junto:", texto_junto)

# Verificando conteúdo
contem = "Python" in texto
print("Contém 'Python':", contem)

# Formatação de strings
nome = "João"
idade = 30
apresentacao = "Meu nome é {} e eu tenho {} anos.".format(nome, idade)
print("Apresentação formatada:", apresentacao)

# Remoção de espaços em branco
espacos = "   espaços   "
print("Espaços removidos:", espacos.strip())
