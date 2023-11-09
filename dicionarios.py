pessoa = {"nome": "Guilherme", "idade": 23}

#pessoa = dict(nome="Guilherme", idade=23)

pessoa["telefone"] = "3333-1234"

print(pessoa["idade"])

#pessoa.clear() # VAI APAGAR todo o dicionario

copia = pessoa.copy() #para copiar e alterar

#para adicionar novas chaves de uma vez so
#dict.fromkeys(["nome", "telefone"]) # vai retornar com none
#dict.fromkeys(["nome", "telefone"], "vazio") # vai retornar de padrão o valor que colocar na frente

print(pessoa.fromkeys(["email"], "vazio"))

pessoa.get("chave", {}})

pessoa.items() #retorna o que tem dentro do dicionario




