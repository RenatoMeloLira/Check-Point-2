from funcoes import *
#### LISTA #####
vazamento = {"JOAO":["joao@gmail.com", "joazinho123", 588566597, 85795896987, 45646465879799865464657897], "RENATO":["renato@gmail.com", "rm8569", 56698987, 45878996587, 322365445464657897]}
#### VALIDAÇÂO ####
resp = "S"
opcao = 0
######### MENU #########
while resp == "S":
    print("\033[1;97m")
    print("-------------------- Bem Vindo---------------------")
    print("--------- Consulta de Vazamento de Dados-----------")
    print("\n                   OPÇÕES\n")
    print("      [1] Cadastrar Dados Pessoais")
    print("      [2] Exibir Banco de Dados")
    print("      [3] Buscar Nome no Banco de Dados")
    print("      [4] Excluir Pessoa do Banco de Dados")
    print("      [5] Sair")
    print("")

    opcao = int(input("Escolha uma Opcao: "))

    ##### OPÇÕES #########
    if opcao == 1:
        cadastropessoa(vazamento)
    elif opcao == 2:
        exibirdados(vazamento)
    elif opcao == 3:
        buscarnome(vazamento)
    elif opcao == 4:
        excluirpessoa(vazamento)
    elif opcao == 5:
        print("Obrigado por utilizar nossa ferramenta, volte sempre :)")
        exit()
    else:
        print("\nOpcao invalida!\n")
