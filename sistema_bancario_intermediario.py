menu = '''
======MENU=======

[d] Depositar
[s] Sacar
[e] Extrato
[o] Quantos saques eu fiz?
[h] Ajuda
[q] Sair

'''
menu_ajuda = '''
========= AJUDA =========
Está enfrentando algum problema? Não se preocupe, iremos te ajudar.
Escolha a opção que represente seu problema:

[1] Não consigo sacar
[2] Coloquei um valor, mas aparece um erro
[3] Não consigo mais realizar nenhuma operação de saque
[4] Desejo falar com um(a) atendente.
=========================
'''

faq1 = '''
Ao inserir o valor do saque, garanta que o valor inserido seja válido
e que seu saldo seja maior que o valor de saque.
Ex: Se seu saldo é de R$2000.00, não será possível sacar R$3000.0

Para verificar seu saldo atual, escolha a opção "Extrato"
'''

faq2 = '''
Ao inserir um valor, certifique-se que ele esteja no formato R$xxxx.xx
para realizar a separação de reais para sentavos utilize o ponto ".", ao invés
da vírgula ",". Se mesmo assim o problema continuar, entre em contato com um(a)
atendente para que possamos verificar.
'''
faq3 = '''
Certifique-se de que você não excedeu a quantidade de operações de saque po dia.

Obs: o limite é de 3 saques por dia ;)
'''

faq_atendente = '''
Sinto muito por não poder te ajudar :(
Mas tudo bem, estou aprendendo ainda, espero poder resolver seu problema na próxima.
Estou te encaminhando para um(a) atendente
'''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input (menu)
    if opcao == "d":
        valor = float(input("Digite o valor que deseja depositar: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito de R$ {valor:.2f} realizado.\n"
        else:
            print("Erro! Operção inválida. POr favor, tente novamente.")
            
        print("Depositando...")
        print(f"Depósito realizado com sucesso. Seu saldo atual é de {saldo}")
                
    elif opcao == "s":
        valor = float(input("Insira o valor que deseja sacar: "))
        
        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite
        
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Operção inválida: seu saldo é inferior ao valor de saque. Tente novamente.")
        
        elif excedeu_limite:
            print("Operação inválida: o valor excede o limite de saque por operação.")
        
        elif excedeu_saques:
            print("Operação inválida: a quantia de saques foram excedidas.")
            
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque de R$: {valor:.2f} realizado"
            numero_saques += 1
        else:
            print("Operção inválida. Verifique se o valor inserido é válido.")
              
    elif opcao == "e":
        
        print("\n======Extrato======")
        print("Não há registro de movimentações realizadas." if not extrato else extrato)
        print(f"O saldo atual é de: R$ {saldo:.2f}")
        print("===================")
        
    elif  opcao == "h":
        opcao == input(menu_ajuda)
        if opcao == 1:
            print(faq1)
        elif opcao == 2:
            print(faq2)
        elif opcao == 3:
            print(faq3)
        elif opcao == 4:
            print(faq_atendente)
            
    elif opcao == "o":
        print(numero_saques)
    elif opcao == "q":
        print("""Obrigado por utilizar nosso sistema bancário.
Deslogando... Até mais.""")
        break

    else:
        print("Opção inválida. Verifique se a opção inserida está correta.")
 