import os

#Função do menu principal
def menuPrincipal():
    os.system('clear')
    print("======================================\n=========== MENU PRINCIPAL ===========\n======================================\n")
    print("\t1 - Funcionários")
    print("\t2 - Produtos")
    print("\t3 - Pedidos")
    print("\t4 - Informações do projeto")
    print("\t0 - Sair")
    print("\n======================================")
    escolha = input("Digite sua opção: ")
    return escolha

#Função para printar as informações do projeto
def infoProjeto():
    print("PyBar: Um sistema de gestão para bares e restaurantes!")
    print("Matéria: DCT1101 - ALGORITMOS E LÓGICA DE PROGRAMAÇÃO")
    print("Docente: Flavius da Luz e Gorgonio")
    print("Discente: Denner Bismarck de Lucena França")
    print("GitHub: https://github.com/DennerBismarck/projeto3unidade")

#Programa inicial principal
opcao = menuPrincipal()
while opcao != "0":
    if(opcao == "1"):
        print("=============== Menu Funcionários ===============")
        print("Ainda em desenvolvimento...")
    elif(opcao == "2"):
        print("=============== Menu Produtos ===============")
        print("Ainda em desenvolvimento...")
    elif(opcao == "3"):
        print("=============== Menu Pedidos ===============")
        print("Ainda em desenvolvimento...")
    elif(opcao == "4"):
        infoProjeto()
    else:
        print("Opção inválida!")
    input("Pressione ENTER para continuar")
    opcao = menuPrincipal()

