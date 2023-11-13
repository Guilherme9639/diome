def exibir_mensagem():
    print(1, 2, 3)
    
    
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def test(a, b):
    return a * 2 +b * 3

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação é = {resultado}")
    
    
    
exibir_resultado(50, 50, somar)
exibir_resultado(50, 50, subtrair)
exibir_resultado(50, 50, test)

# para usar função na raiz do programa usamos a palabra Global

salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario


print(salario_bonus(500))