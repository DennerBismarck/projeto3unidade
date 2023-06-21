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

#Menu geral utilizado nas telas de CRUD
def menuCRUD(nome_funcao):
    os.system('clear')
    print("======================================\n=========== MENU %s ===========\n======================================\n"%(nome_funcao.upper()))
    print("\t1 - Registrar novo %s" %(nome_funcao))
    print("\t2 - Editar %s" %(nome_funcao))
    print("\t3 - Buscar por %s"%(nome_funcao))
    print("\t4 - Deletar %s"%(nome_funcao))
    print("\t5 - Listar todos os %ss"%(nome_funcao))
    print("\t0 - Voltar")
    print("\n======================================")
    escolha = input("Digite sua opção: ")
    return escolha

#Programa inicial principal
opcao_menu_principal = menuPrincipal()
while opcao_menu_principal != "0":

    if(opcao_menu_principal == "1"):
        opcao_menu_secundario = menuCRUD("fucionário")
        while opcao_menu_secundario !="0":    
            if opcao_menu_secundario == "1":
                print("EM DESENVOLVIMENTO")
            elif opcao_menu_secundario == "2":
                print("EM DESENVOLVIMENTO")
            elif opcao_menu_secundario == "3":
                print("EM DESENVOLVIMENTO")
            elif opcao_menu_secundario == "4":
                print("EM DESENVOLVIMENTO")   
            elif opcao_menu_secundario == "5":
                print("EM DESENVOLVIMENTO")
            input("Pressione ENTER para continuar")
            opcao_menu_secundario = menuCRUD("funcionário")

    elif(opcao_menu_principal == "2"):
        opcao_menu_secundario = menuCRUD("produto")
        while opcao_menu_secundario !="0":    
            if opcao_menu_secundario == "1":
                print("EM DESENVOLVIMENTO")
            elif opcao_menu_secundario == "2":
                print("EM DESENVOLVIMENTO")
            elif opcao_menu_secundario == "3":
                print("EM DESENVOLVIMENTO")
            elif opcao_menu_secundario == "4":
                print("EM DESENVOLVIMENTO")   
            elif opcao_menu_secundario == "5":
                print("EM DESENVOLVIMENTO")
            input("Pressione ENTER para continuar")
            opcao_menu_secundario = menuCRUD("produto")

    elif(opcao_menu_principal == "3"):
        opcao_menu_secundario = menuCRUD("pedido")
        while opcao_menu_secundario !="0":    
            if opcao_menu_secundario == "1":
                print("EM DESENVOLVIMENTO")
            elif opcao_menu_secundario == "2":
                print("EM DESENVOLVIMENTO")
            elif opcao_menu_secundario == "3":
                print("EM DESENVOLVIMENTO")
            elif opcao_menu_secundario == "4":
                print("EM DESENVOLVIMENTO")   
            elif opcao_menu_secundario == "5":
                print("EM DESENVOLVIMENTO")
            input("Pressione ENTER para continuar")
            opcao_menu_secundario = menuCRUD("pedido")

    elif(opcao_menu_principal == "4"):
        infoProjeto()

    else:
        print("Opção inválida!")
    input("Pressione ENTER para continuar")
    opcao_menu_principal = menuPrincipal()

