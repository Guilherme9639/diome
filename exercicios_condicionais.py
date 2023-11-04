saldo = 2000.0
saque = float(input("Informe o valor do saque:"))
if saldo >= saque:
    print("Saque realizado com sucesso")
if saldo < saque:
    print("Seu saque não pode ser efetuado")



if saldo >= saque:
    print("saque realizado com sucesso")
else:
    print("Saldo Insuficiente")  


opcao = int(input("Informe uma opção: [1] Sacar \n[2] Extrato:"))

if opcao == 1:
    valor = float(input("Informe a quantia para o saque: "))

elif opcao == 2:
    print("Exibindo o extrato...")

else:
    print("Opção Inválida")


#elif = quando precisamos de dar mais de uma opção alem do else que finaliza aquele if.