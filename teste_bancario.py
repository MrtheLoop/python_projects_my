saldo = 2000.00

opcao = int(input("Menu: \n [1] Sacar \n [2] Extrato \n Informe uma opção:"))
if opcao == 1:
    valor = float(input("Informe a quantia para saque: "))
    if valor <= saldo:
        print("Saque realizado com sucesso!")
    else:
        print("Você não possui saldo para realziar essa operação! verifique seu saldo e tente novamente")
    #...
elif opcao == 2:
    print("Exibindo o extrato...")
    print(saldo)
else:
    print("Opção inválida!")