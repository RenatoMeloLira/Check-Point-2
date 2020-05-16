#Cadastro da Pessoa
def cadastropessoa(vaza):
    resp = "S"
    while resp =="S":
        nome = input("\nDigite o Nome: ").upper()
        from getpass import getpass
        vaza[nome] = [input("Digite o e-mail: "), getpass("Senha do Email: "), int(input("RG: ")), int(input("CPF: ")), int(input("CERTIDÃO: "))]
        print("\nINFORMAÇÕES ADICIONADA COM SUCESSO NO BANCO DE DADOS!!!")
        resp = input("Deseja cadastrar mais uma pessoa? ").upper()
    
 
#Exibir Dados Pessoais
def exibirdados(vaza):
    for nome, lista in vaza.items():
        print("\nNome...........", nome)
        print("Email......... ", lista[0])
        print("Senha......... ", lista[1])
        print("RG............ ", lista[2])
        print("CPF........... ", lista[3])
        print("CERTIDÃO...... ", lista[4])       
    temporaria = input("Precione ENTER para voltar ao MENU")
 
#Buscar Nome no Banco de Dados
def buscarnome(vaza):
    busca = input("\nDigite o Nome: ").upper()
    if vaza.get(busca) != None:
        lista = vaza.get(busca)
        print("\nEmail......... ", lista[0])
        print("Senha......... ", lista[1])
        print("RG............ ", lista[2])
        print("CPF........... ", lista[3])
        print("CERTIDÃO...... ", lista[4])
    else:
        print("{} Não encontrado no banco de dados!!!".format(busca))
    temporaria = input("\nPrecione ENTER para voltar ao MENU")
 
 
#Excluir Pessoa no Banco de Dados
def excluirpessoa(vaza):
    deletar = input("\nQual nome deseja excluir? ").upper()
    if vaza.get(deletar) != None:
        del vaza[deletar]
    else:
        print(" {} Não encontrado!".format(deletar))
