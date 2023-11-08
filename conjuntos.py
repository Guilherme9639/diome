set([1,2,3,1,3,4]) #ele retira elementos duplicados de uma lista, mas, não necessariamente na "ordem"

#se colocar entre {}  também aciona a função set

linguagens = {"python", "java", "python", "java"}

print(linguagens)

carros = {1, 2, 1, 5, 6, 5 }

for carro in carros:
    print(carro)
    
conjunto_a = {1, 2, 3}
conjunto_b = {5, 6, 7, 4}

print(conjunto_a.union(conjunto_b)) # junta o conjunto e ordena
conjunto_a.intersection(conjunto_b) # ele vai pegar as partes iguais dos conjuntos, a parte "comum"
conjunto_a.difference(conjunto_b) # ele pega o que tem de diferente de um conjunto 
conjunto_a.symetric_difference(conjunto_b) #junta as diferenças do conjunto
conjunto_a.issubset(conjunto_b) #elementos pertencentes 
conjunto_a.issuperset(conjunto_b) #reporta se um conjunto existe inteiro dentro do outro conjunto
conjunto_a.isdisjoint(conjunto_b) # se retornar true é porque não tem nenhuma informação igual nos conjuntos
conjunto_a.add(10) #adiciona ao conjunto
conjunto_a.remove(0) #remove pela posição
