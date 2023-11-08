lista = [1, 2, 3, 4]
lista.append(5) #insere o valor que colocar dentro do parenteses dentro da lista ja criada


print(lista)

lista.clear() #significa limpar aquela lista

print(lista)

le = lista.copy() #copia a lista onde assim vc pode mudar a nova lista que criou sem modificar a anterior

print(lista)

cores = ["vermelho", "azul", "verde", "azul"]

cores.count("azul") #vai trazer o numero de vezes que aquilo que pedimos se repete dentro da lista

cores.extend("vermelho", "laranja") #atualiza a lista com mais de uma informação

cores.index("verde") #traz o indice de ocorrencia de um item dentro da lista

cores.pop(0) #retira o elemento da lista por posição

cores.remove("verde") #remove o eletemento pelo nome

cores.reverse() #coloca ao contrario a lista

cores.sort() #ordena alfabeticamente a lista

len(cores)  #pega o tamanho do que você colocar entre parenteses

sorted(cores, key=lambda x: len(x)) #função que faz a mesma coisa que o sort

frutas = ["laranja", "maca", "uva"]
print(frutas)

letras = list("python")
print(letras)

numeros = list(range(10))
print(numeros)

carro = ["Ferrari", "F8", 42000]
print(carro)

matriz = [
    [1, "a", 2]
    [2, "a", 1]
    ["a", 1, 2]
]

print(matriz[0])

print(matriz[0][0])

print(matriz[0][-1])

print(matriz[-1][-1])

