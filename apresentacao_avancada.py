nome = input("Insira seu nome aqui: ")
idade = int(input("Insira sua idade aqui: "))
profissao = input("Insira sua profissão aqui: ")
curso = input("Insira seu curso aqui: ")

opcao = -1

while opcao != 0:
    opcao = int(input("Você está fazendo algum curso auxiliar?: \n [1]Sim \n [2]Não \n : "))
    if opcao == 1:
        curso_aux = input("Qual curso você auxiliar você está fazendo? \n : ")
        print(f"Olá me chamo {nome}. Tenho {idade} anos de idade, atualmente trabalho como {profissao} e estou cursando {curso} de faculdade e {curso_aux} como curso complementar.")
        break
    if opcao == 2: 
        print(f"Olá me chamo {nome}. Tenho {idade} anos de idade, atualmente trabalho como {profissao} e estou cursando {curso}")
        break

