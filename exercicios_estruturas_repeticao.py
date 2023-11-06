# Estrutura for

texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
        
        
print()

# função built in
# range

for numero in range(0, 51, 5):
    print(numero, end=" ")
    
    
# Comando WHILE = Repetição de codigo varias vezes, se não tenho certeza da quantidade de vezes de execução

opcao = -1

while opcao != 0:
    opcao = int(input("[1] sacar \n[2] Extrato \n[0] Sair \n: "))
    
    if opcao == 1:
        print("Sacando...")
        
    elif opcao == 2:
        print("Exibindo o extrato...")
else:
    print("Obrigado por usar nosso sistema bancário.")
    
    
 # Comando BREAK = cortar o laço de repetição
 
while True:
     numero = int(input("Informe um número: "))
     
     if numero == 10:
         break
     
     print(numero)
 
 

