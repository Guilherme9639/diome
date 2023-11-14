saldo_atual = float(input("Informe aqui o seu saldo: "))
valor_deposito = float(input("Informe aqui o seu valor de deposito: "))
valor_retirada = float(input("Informe aqui o valor que quer sacar: "))

def saldo(valor_deposito, valor_retirada):
    global saldo_atual
    return saldo_atual + valor_deposito - valor_retirada
 
novo_saldo = saldo(valor_deposito,valor_retirada)
    
    
print('Saldo atualizado na conta: %.1f'%(novo_saldo))

