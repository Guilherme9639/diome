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

nome = "Guilherme"
idade = 23
profissao = "programador"
linguagem = "Python"

print("Olá, olha me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s" % (nome, idade, profissao, linguagem))

