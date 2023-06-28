import os, pickle, datetime

#Criando os dicionários utilizados nos módulos
funcionarios = {}
produtos = {}
pedidos = {}


#Bloco de código carregando o "banco de dados" dos arquivos .dat

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
    if(nome_funcao == "pedido"):
        print("\t1 - Registrar novo %s" %(nome_funcao))
        print("\t2 - Menu %ss" %(nome_funcao))
        print("\t0 - Voltar")
    else:    
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
    print("\nPESQUISAR FUNCIONÁRIO")
    cpf_pesquisado = input("\nInforme o cpf do funcionário que deseja pesquisar: ")
    if cpf_pesquisado in funcionarios:
        print("Nome: ", funcionarios[cpf_pesquisado][0])
        print("CPF: ", cpf_pesquisado)
        print("Cargo: ", funcionarios[cpf_pesquisado][1])
        return funcionarios[cpf_pesquisado]
    else:
        print("CPF não encontrado!")

def editarFuncionario():
    print("\nEDITAR FUNCIONÁRIO")
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
    print("\nDELETAR FUNCIONÁRIO")
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
        print("=====================\nNome: %s\nCpf: %s\nCargo: %s"%(funcionarios[funcionario][0], funcionario, funcionarios[funcionario][1]))


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
    print("\nBUSCAR PRODUTO")
    nome_pesquisado = input("\nInforme o nome do produto que deseja pesquisar: ")
    if nome_pesquisado in produtos:
        print("Nome:", nome_pesquisado)
        print("Preço: R$%.2f" %(produtos[nome_pesquisado][0]))
        print("Descrição:", produtos[nome_pesquisado][1])
        return produtos[nome_pesquisado]
    else:
        print("Nome não encontrado!")

def editarProduto():
    print("\nEDITAR PRODUTO")
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
    print("\nDELETAR PRODUTO")
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
    print("LISTAGEM DE PRODUTOS")
    for produto in produtos:
        print("=====================\nNome:%s\nPreço: R$%.2f\nDescrição: %s"%(produto, produtos[produto][0], produtos[produto][1]))

############################################################################################
#CRUD de Pedidos
def cadastrarPedido():
    print("\nCADASTRO DE PEDIDOS")
    #Criação de uma chave primária com auto incremento
    aux = 0
    for i in pedidos:
        aux = i
        print (aux)
    chave = aux+1

    print ("chave é: ",chave)
    funcionario = pesquisarFuncionario()
    #Implementar um sistema para somente garçons poderem ser responsáveis pela comanda (?)
    produto = pesquisarProduto()
    hora_do_pedido = datetime.datetime.now()
    valor_da_comanda = produto[0]
    #Depois implementar módulos com dicionários separados para exercerem a função de produtos_dos_pedidos, para calcularmos o valor total do pedido... 
    #...e poder ter mais de um produto por comanda
    pedidos[chave] = [funcionario[1], produto, valor_da_comanda,hora_do_pedido]


    tb_pedidos = open("bd_pedidos.dat", "wb")
    pickle.dump(pedidos,tb_pedidos)
    tb_pedidos.close()

    print("Pedido cadastrado com sucesso!")


#Para o Read de pedidos, fez-se um modelo diferente, tendo em vista a natureza desse módulo, é inviável pesquisar por informações específicas...
#...por isso, optou-se por listar todos os códigos e datas e horas dos pedidos e perguntar qual o usuário deseja ver informações mais aprofundadas. 
#O Update e o Delete também foram implementados neste mesmo menu.
def listar_e_pesquisar_pedidos():
    print("\nMENU LISTAGEM DE PEDIDOS")
    for pedido in pedidos:
        print("=====================\nCódigo:%s\nData e hora: %s\n====================="%(pedido, pedidos[pedido][3]))
    cod_pesquisado = int(input("\nInforme o código da comanda que você deseja consultar: "))
    if cod_pesquisado in pedidos:
        print("Código:", cod_pesquisado)
        print("Funcionário:", pedidos[cod_pesquisado][0])
        print("Produtos:", pedidos[cod_pesquisado][1])
        print("Valor total: R$%.2f" %(pedidos[cod_pesquisado][2]))
        print("Data e hora do pedido:", pedidos[cod_pesquisado][3])    
        escolha_menu_pedidos = input("Digite S se deseja realizar alguma ação com este pedido e N se deseja voltar: ")
        while(escolha_menu_pedidos.upper() != "N"):
            if(escolha_menu_pedidos.upper() == "S"):
                escolha_menu_pedidos_UpdateOrDelete = input("Digite 1 se deseja editar o pedido, 2 se deseja deletar o pedido ou 0 se deseja sair: ")
                while(escolha_menu_pedidos_UpdateOrDelete != "0"):
                    if(escolha_menu_pedidos_UpdateOrDelete == "1"):
                        print("EDITAR PEDIDO")
                        funcionario = pesquisarFuncionario()
                        produto = pesquisarProduto()
                        valor_da_comanda = produto[0]
                        pedidos[cod_pesquisado] = [funcionario[1], produto, valor_da_comanda]

                        tb_pedidos = open("bd_pedidos.dat", "wb")
                        pickle.dump(pedidos,tb_pedidos)
                        tb_pedidos.close()

                    elif(escolha_menu_pedidos_UpdateOrDelete == "2"):
                        del pedidos[cod_pesquisado]
                        print("Pedido deletado com sucesso!")

                        tb_pedidos = open("bd_pedidos.dat", "wb")
                        pickle.dump(pedidos,tb_pedidos)
                        tb_pedidos.close()
                    else:
                        print("Digite uma opção válida!")
                    escolha_menu_pedidos_UpdateOrDelete = input("Digite 1 se deseja editar o pedido, 2 se deseja deletar o pedido ou 0 se deseja sair: ")
            else:
                print("Digite uma opção válida!")
            escolha_menu_pedidos = input("Digite S se ainda deseja realizar alguma ação com este pedido e N se deseja voltar: ")

    else:
        print("Erro!")


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
                cadastrarPedido()
            elif opcao_menu_secundario == "2":
                listar_e_pesquisar_pedidos()
            input("Pressione ENTER para continuar")
            opcao_menu_secundario = menuCRUD("pedido")

    elif(opcao_menu_principal == "4"):
        infoProjeto()

    else:
        print("Opção inválida!")
    input("Pressione ENTER para continuar")
    opcao_menu_principal = menuPrincipal()

