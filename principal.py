from funcoes import *

while True:
    login = False
    nomeUsuario = input('\nDigite o nome do usuário:')
    senha = input('Digite sua senha:')
    for i in range(len(usuarios)):
            if nomeUsuario == usuarios[i][0]:
               if senha == usuarios[i][1]:
                if usuarios[i][2] == 'A':
                    print('\n***Administrador autenticado!***')
                login = True
                break
    if login == False:
        print("Usuário não encontrado \n\nCadastre-se:\n")
        nomeUsuario = input('Digite seu CPF ou E-mail: ')
        senha = input('Crie uma senha:')
        usuarios.append([nomeUsuario,senha,'U'])
        print("\n***Você logou como Usuário!***")
        login = True
    if login:
       break
    else:
        print("Usuário invalido")
    
while True:

    print("\n-------MENU LK PET------")
    print("1. Cadastros.")
    print("2. Atendimentos.")
    print("3. Consultas/Relatórios.")
    print("4. Sair.")
    print("------------------------")

    opcao = int(input("Digite a opção que você deseja:\n"))
    clear()

    if opcao == 1: #CRUD
                print("1. Menu Usuários (ADM)")
                print("2. Menu Clientes")
                print("3. Menu Pets")
                print("4. Menu Serviços (ADM)")
                print("5. Voltar")

                opcaoMenu = int(input("Digite o número da opção desejada:\n"))
                clear()
                if opcaoMenu == 1: #Usuários
                        menu_usuarios()
                        
                        opcaoUsuario = int(input("Digite o número da opção desejada:\n"))
                        
                        if opcaoUsuario == 1: #CADASTRAR #apenas adm
                            for i in range(len(usuarios)):
                                if usuarios[i][2] == 'U':
                                    print("Apenas ADM pode executar essa função!")
                                elif usuarios[i][2] == 'A':
                                    cadastro_usuarios()
                                    break
                                              
                        elif opcaoUsuario == 2: #ATUALIZAR
                            for i in range(len(usuarios)):
                                if usuarios[i][0] == nomeUsuario:
                                    if usuarios[i][1] == senha:
                                        nomeUsuario = input("Digite o nome do funcionário para atualizar: ")
                                        novaSenha = input("Digite a nova senha: ")
                                        for i in range(len(usuarios)):
                                            usuarios[i][1] = novaSenha 
                                        print("Atualização realizada com sucesso!")
                                    else:
                                        print("Usuário ou senha inválidos para atualizar!")

                        elif opcaoUsuario == 3:
                            while True:
                                nomeusuario = input("Digite o nome do Usuário para remove-lo: ")
                                for i in range(len(usuarios)):
                                    if nomeusuario == usuarios[i][0]:
                                        del usuarios[i]
                                        print("Usuário removido com sucesso!")
                                        break
                                    elif len(usuarios) == 0:
                                        print("Não há Usuários cadastrados.") 
                                        
                        elif opcaoUsuario == 4:
                            consultar_usuario()
                        elif opcaoUsuario == 5:
                            voltar_menus()
                        elif opcaoUsuario == 6:
                            print(usuarios)
                        else:
                            print("Opção inválida!") 

                elif opcaoMenu == 2: #Clientes
                    while True:
                        menu_clientes()
                                        
                        opcaoCliente = int(input("Digite o número da opção desejada:\n"))

                        #apenas adm
                        if opcaoCliente == 1:
                            for i in range(len(usuarios)):
                                if usuarios[i][2] == 'U':
                                    print("Apenas ADM pode executar essa função!")
                                elif usuarios[i][2] == 'A':
                                    cadastro_cliente()
                                else:
                                    break 
                        elif opcaoCliente == 2:
                            atualizar_cliente() #proprio usuario
                        elif opcaoCliente == 3 and tipo == "A":
                            apagar_cliente()   
                        elif opcaoCliente == 4:
                            consultar_cliente()
                        elif opcaoCliente == 5:
                            voltar_menus()
                        else:
                            print("Opção inválida!")  

                elif opcaoMenu == 3: #Pets
                    menu_pets()

                    opcaoPets = int(input("Digite o número da opção desejada:\n"))

                    if opcaoPets == 1 and tipo == "A":
                        cadastrar_pet() #apenas adm
                        
                    elif opcaoPets == 2:
                        atualizar_pet() #proprio usuario
                    elif opcaoPets == 3 and tipo == "A":
                        apagar_pet()   
                    elif opcaoPets == 4:
                        consultar_pet()
                    elif opcaoPets == 5:
                        voltar_menus()
                    else:
                        print("Opção inválida!")

                elif opcaoMenu == 4: #Serviços
                    menu_servicos()

                    opcaoPets = int(input("Digite o número da opção desejada:\n"))

                    if opcaoPets == 1 and tipo == "A":
                        cadastrar_servico() #apenas adm
                    elif opcaoPets == 2:
                        atualizar_servico() #proprio usuario
                    elif opcaoPets == 3 and tipo == "A":
                        apagar_servico()   
                    elif opcaoPets == 4:
                        consultar_servico()
                    elif opcaoPets == 5:
                        voltar_menus()
                    else:
                        print("Opção inválida!")
    
                elif opcaoMenu == 5: #Voltar
                    voltar_principal()

                else: 
                    print("Opção inválida!")

    if opcao == 2: #Atendimentos
            
        print("1. Iniciar.")
        print("2. Agendar.")
        print("3. Remarcar.")
        print("4. Voltar ao Menu Principal.\n")

        opcao = int(input("Digite a opção que você deseja:\n"))
        clear()

        if opcao == 1: #Consultas/Relatórios

            if opcao == 1: 
                iniciar_atendimento()
                
            elif opcao == 2:
                agendar_atendimento()

            elif opcao == 3:
                remarcar_atendimento()

            elif opcao == 4:
                voltar_principal() 
            else: 
                print("Opção inválida!")

    if opcao == 3: #Consultas/Relatorios
        consulta_relatorio_1()

    if opcao == 4: #Sair
        print("Você chegou no final do PetLove! <3")
        break
        
    


    