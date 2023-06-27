import os, pickle, datetime

#Criando os dicionários utilizados nos módulos
funcionarios = {}
produtos = {}
pedidos = {}


#Bloco de código carregando o "banco de dados" dos arquivos .txt

#P/Funcionários
try:    
    tb_funcionarios = open("bd_funcionarios.dat", "rb")
    funcionarios = pickle.load(tb_funcionarios)
    tb_funcionarios.close()
except:
    tb_funcionarios = open("bd_funcionarios.dat")
    tb_funcionarios.close()

#P/Produtos
try:    
    tb_produtos = open("bd_produtos.dat", "rb")
    produtos = pickle.load(tb_produtos)
    tb_produtos.close()
except:
    tb_produtos = open("bd_produtos.dat")
    tb_produtos.close()

#P/Pedidos
try:    
    tb_pedidos = open("bd_pedidos.dat", "rb")
    pedidos = pickle.load(tb_pedidos)
    tb_produtos.close()
except:
    tb_pedidos = open("bd_pedidos.dat")
    tb_pedidos.close()


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

############################################################################################
#CRUD de funcionários
def cadastrarFuncionario():
    print("\nCADASTRO DE FUNCIONÁRIOS")
    nome = input("Nome: ")
    cpf = input("CPF: ") #Alterar para funcionar com validador depois
    cargo = input("Cargo: ")
    funcionarios[cpf] = [nome,cargo] #Se o cpf for repetido, pode dar erro...


    tb_funcionarios = open("bd_funcionarios.dat", "wb")
    pickle.dump(funcionarios,tb_funcionarios)
    tb_funcionarios.close()

    print("Funcionário cadastrado com sucesso!")

def pesquisarFuncionario():
    cpf_pesquisado = input("\nInforme o cpf do funcionário que deseja pesquisar: ")
    if cpf_pesquisado in funcionarios:
        print("Nome: ", funcionarios[cpf_pesquisado][0])
        print("CPF: ", cpf_pesquisado)
        print("Cargo: ", funcionarios[cpf_pesquisado][1])
    else:
        print("CPF não encontrado!")

def editarFuncionario():
    cpf_pesquisado = input("\nInforme o cpf do funcionário pesquisado: ")
    if cpf_pesquisado in funcionarios:
        nome = input("Digite o novo nome: ")
        cargo = input("Digite o novo cargo: ")
        funcionarios[cpf_pesquisado] = [nome,cargo]
        
        tb_funcionarios = open("bd_funcionarios.dat", "wb")
        pickle.dump(funcionarios,tb_funcionarios)
        tb_funcionarios.close()

    else:
        print("CPF não encontrado!")

def deletarFuncionario():
    cpf_pesquisado = input("\nInforme o cpf do funcionário pesquisado: ")
    if cpf_pesquisado in funcionarios:
        del funcionarios[cpf_pesquisado]
        print("Funcionário deletado com sucesso.")
        tb_funcionarios = open("bd_funcionarios.dat", "wb")
        pickle.dump(funcionarios,tb_funcionarios)
        tb_funcionarios.close()
    else:
        print("CPF não encontrado!")

def listarFuncionarios():
    for funcionario in funcionarios:
        print("=====================\nNome:%s\nCpf: %s\nCargo: %s"%(funcionarios[funcionario][0], funcionario, funcionarios[funcionario][1]))


############################################################################################
#CRUD de Produtos
def cadastrarProduto():
    print("\nCADASTRO DE PRODUTOS")
    nome = input("Nome do produto: ")
    preco = float(input("Preço(0.00): "))
    descricao = input("descricao: ")
    produtos[nome] = [preco,descricao] 


    tb_produtos = open("bd_produtos.dat", "wb")
    pickle.dump(produtos,tb_produtos)
    tb_funcionarios.close()

    print("Produto cadastrado com sucesso!")

def pesquisarProduto():
    nome_pesquisado = input("\nInforme o nome do produto que deseja pesquisar: ")
    if nome_pesquisado in produtos:
        print("Nome:", nome_pesquisado)
        print("Preço: R$%.2f" %(produtos[nome_pesquisado][0]))
        print("Descrição:", produtos[nome_pesquisado][1])
    else:
        print("Nome não encontrado!")

def editarProduto():
    nome_pesquisado = input("\nInforme o nome do produto pesquisado: ")
    if nome_pesquisado in produtos:
        preco = input("Digite o novo preco: ")
        descricao = float(input("Digite a nova descricao: "))
        funcionarios[nome_pesquisado] = [preco,descricao]
        
        tb_produtos = open("bd_produtos.dat", "wb")
        pickle.dump(produtos,tb_produtos)
        tb_produtos.close()

    else:
        print("Produto não encontrado!")

def deletarProduto():
    nome_pesquisado = input("\nInforme o nome do produto que deseja pesquisar: ")
    if nome_pesquisado in produtos:
        del produtos[nome_pesquisado]
        print("Produto deletado com sucesso.")

        tb_produtos = open("bd_produtos.dat", "wb")
        pickle.dump(produtos,tb_produtos)
        tb_produtos.close()
    else:
        print("CPF não encontrado!")

def listarProdutos():
    for produto in produtos:
        print("=====================\nNome:%s\nPreço: R$%.2f\nDescrição: %s"%(produto, produtos[produto][0], produtos[produto][1]))

############################################################################################
#CRUD de Pedidos
def cadastrarPedido():
    print("\nCADASTRO DE PEDIDOS")
    nome = input("Nome do produto: ")
    preco = float(input("Preço(0.00): "))
    descricao = input("descricao: ")
    produtos[nome] = [preco,descricao] 


    tb_produtos = open("bd_produtos.dat", "wb")
    pickle.dump(produtos,tb_produtos)
    tb_funcionarios.close()

    print("Produto cadastrado com sucesso!")


#Programa inicial principal
opcao_menu_principal = menuPrincipal()
while opcao_menu_principal != "0":
    if(opcao_menu_principal == "1"):
        opcao_menu_secundario = menuCRUD("fucionário")
        while opcao_menu_secundario !="0":    
            if opcao_menu_secundario == "1":
                cadastrarFuncionario()
            elif opcao_menu_secundario == "2":
                editarFuncionario()
            elif opcao_menu_secundario == "3":
                pesquisarFuncionario()
            elif opcao_menu_secundario == "4":
                deletarFuncionario()   
            elif opcao_menu_secundario == "5":
                listarFuncionarios()
            input("Pressione ENTER para continuar")
            opcao_menu_secundario = menuCRUD("funcionário")

    elif(opcao_menu_principal == "2"):
        opcao_menu_secundario = menuCRUD("produto")
        while opcao_menu_secundario !="0":    
            if opcao_menu_secundario == "1":
                cadastrarProduto()
            elif opcao_menu_secundario == "2":
                editarProduto()
            elif opcao_menu_secundario == "3":
                pesquisarProduto()
            elif opcao_menu_secundario == "4":
                deletarProduto()  
            elif opcao_menu_secundario == "5":
                listarProdutos()
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

