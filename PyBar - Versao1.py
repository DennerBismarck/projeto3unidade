import os

#Função do menu principal
def menuPrincipal():
    os.system('clear')
    print("======================================\n=========== MENU PRINCIPAL ===========\n======================================\n")
    print("\t1 - Funcionários")
    print("\t2 - Produtos")
    print("\t3 - Pedidos")
    print("\t0 - Sair")
    print("\n======================================")
    escolha = input("Digite sua opção: ")
    return escolha
#Programa inicial principal

opcao = menuPrincipal()
while opcao != 0:
    if(opcao == "1"):
        print("=============== Menu Funcionários ===============")
        print("Ainda em desenvolvimento...")
    elif(opcao == "2"):
        print("=============== Menu Produtos ===============")
        print("Ainda em desenvolvimento...")
    elif(opcao == "3"):
        print("=============== Menu Pedidos ===============")
        print("Ainda em desenvolvimento...")
    else:
        print("Opção inválida!")
    input("Digite qualquer tecla para continuar")
    opcao = menuPrincipal()

