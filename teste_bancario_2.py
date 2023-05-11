saldo = 2000.00

opcao = -1

while opcao != 0:
    opcao = int(input("Escolha uma função: \n [1] Extrato \n [2] Sacar \n [0] Sair \n :"))
    if opcao == 1:
        print(saldo)
    if opcao == 2:
        valor = int(input("Digite o valor que deseja sacar: "))
        print(f"Saque realizado. Seu saldo agora é de {saldo - valor}")
        break
    else:
        print("Deslogando. Obrigado por utilizar nosso sistema")
        break