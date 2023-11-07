curso = "pYtHon"

print(curso.upper()) #tudo maiusculo    

print(curso.lower()) #tudo minusculo

print(curso.title()) #somente o primeiro maiusculo

texto = "   Olá mundo!   "

print(texto.strip()) #corta os espaços

print(texto.lstrip()) #corta o espaço da esquerda

print(texto.rstrip()) #corta os espaços da direita

menu = "Python"

print(menu.center(14)) #adiciona espaço dos lados

print(menu.center(10, "!")) #adociona caracter ao inicio e ao final

print("-".join(menu)) #adicionar caracter ao meio do texto



#Interpolação de Variaveis

#old
nome = "Guilherme"
idade = 23
profissao = "programador"
linguagem = "Python"

print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s" % (nome, idade, profissao, linguagem))

print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}" .format(nome, idade, profissao, linguagem))

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")

#fatiação de string

nome_completo = "Guilherme De Almeida Carodzo"

nome_completo[0] #pega o numero que colocar, lmebrando que se começa no 0

nome_completo[:9] #pega do 0 ao ultimo numero antes do que colocar

nome_completo[10:] #pega o numero descrito até o final da string

nome_completo[10:16]

nome_completo[10:16:2]

nome[:] #strin completa

nome_completo[:: -1] #espelhamento

#string de multiplas linhas

mensagem = f""""
Olá meu nome é {nome}
Eu estou aprendendo Python
"""

#serve para mensagens grandes dentro de uma so string

