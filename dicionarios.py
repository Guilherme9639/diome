pessoa = {"nome": "Guilherme", "idade": 23}

#pessoa = dict(nome="Guilherme", idade=23)

pessoa["telefone"] = "3333-1234"

print(pessoa["idade"])

#pessoa.clear() # VAI APAGAR todo o dicionario

copia = pessoa.copy() #para copiar e alterar

#para adicionar novas chaves de uma vez so
#dict.fromkeys(["nome", "telefone"]) # vai retornar com none
#dict.fromkeys(["nome", "telefone"], "vazio") # vai retornar de padrão o valor que colocar na frente

#print(pessoa.fromkeys(["email"], "vazio"))

resultado = pessoa.get("telefone", {})

pessoa.items() #retorna o que tem dentro do dicionario

pessoa.keys() #saber todas as chaves que um dicionario tem

#pessoa.pop() # remove o valor - se o valor não tiver no dicionario ele retorna erro, ao ter duvida, colocar uma "mensagem de erro"

pessoa.values() #saber todos os valores do dicionario

#resultados = "guilherme@gmail.com" in pessoa

#resultados = "idade" in pessoa["guilherme@gmail"]

del pessoa["telefone"]

print(pessoa)


pessoa.setdefault("email", "cardozo@gmail.com")

print(pessoa)
print(resultado)


