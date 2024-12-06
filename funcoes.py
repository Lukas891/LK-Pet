import os

usuarios = [['Lucas', '123', 'A']] 
pets = []
clientes = []
atendimentos = []
servicos = []

def clear():
    if os.name == 'nt': #linux
        os.system('cls')
    elif os.name == 'posix': #windows
        os.system('clear')

def voltar_menus():    
    print("1. Menu Usuários")
    print("2. Menu Clientes")
    print("3. Menu Pets")
    print("4. Menu Serviços")
    print("5. Voltar")

    opcaoMenu = int(input("Digite o número da opção desejada:\n"))
 
def voltar_principal():
    print("\nSEJA BEM-VINDO(A) AO PET LOVER!")
    print("\n----------MENU----------")
    print("1. Cadastros.")
    print("2. Atendimentos.")
    print("3. Consultas/Relatórios.")
    print("4. Sair.\n")

    opcao = int(input("Digite a opção que você deseja:\n"))
    clear()

    while True:
        if opcao == 1: #Cadastro
            
            while True:
                print("1. Usuários")
                print("2. Clentes")
                print("3. Pets")
                print("4. Serviços")
                print("5. Voltar")
                opcao1 = int(input("Digite a opção que você deseja cadastrar:\n"))

                if opcao1 == 1: #Usuários
                    cadastro_usuarios()
                
                elif opcao1 == 2: #Clientes
                    cadastro_cliente()

                elif opcao1 == 3: #Pets
                    cadastrar_pet()

                elif opcao1 == 4: #Serviços
                    cadastrar_servico()      

                elif opcao1 == 5: #Voltar
                    clear()
                    voltar_cadastros()
                else: 
                    print("Opção inválida!")

#Funções para usuários
def menu_usuarios():
    print("1. Cadastrar (Apenas ADM)")
    print("2. Atualizar (Próprio usuário)")
    print("3. Apagar (Apenas ADM)")
    print("4. Consultar")
    print("5. Voltar")

def cadastro_usuarios():

        if len(usuarios) == 0:
            print("Cadastre um novo usuário, pois não temos nenhum cadastrado.")
            nomeusuario = input("Nome do novo usuário: ")
            senha = input("Digite a senha: ")
            usuarios.append([nomeusuario, senha, 'U'])  # Adiciona com permissão 'A' (Administrador)
            print("Usuário cadastrado com sucesso!")
        else:
            nomeusuario = input("Digite o nome do novo usuário: ")
            senha = input("Digite a senha: ")
            usuarios.append([nomeusuario, senha, 'U'])
            print("Usuário cadastrado com sucesso!")

def login_usuario():
    
    while True:
        login = False
        if len(usuarios)==1:
            nomeUsuario = input('Digite o nome de Login:')
            senha = input('Digite sua senha:')
            for i in range(len(usuarios)):
                if nomeUsuario == usuarios[i][0]:
                    if senha == usuarios[i][1]:
                            print('Administrador autenticado!')
                            login = True
        if login:
            break 
        else:
            nomeUsuario = input('Digite o nome de Login:')
            senha = input('Digite sua senha:')
            usuarios.append([nomeUsuario,senha,'U'])
            print("Usuário cadastrado!")
            continue  
        

    


def consultar_usuario():
    if len(usuarios) == 0:
        print("Sem funcionários cadastrados.")
        return
    print("Funcionários cadastrados: ")
    for i in usuarios:
        print(f"Nome: {i[0]}, Senha: {i[1]}, Tipo: {i[2]}")

#Funções para pets...
def menu_pets():
    print("1. Cadastrar (Apenas ADM)")
    print("2. Atualizar (Próprio usuário)")
    print("3. Apagar (Apenas ADM)")
    print("4. Consultar")
    print("5. Voltar")

def cadastrar_pet():
    nomepet = input("Digite o nome do pet: ")
    donocpf = input("Digite o CPF do dono: ")
    especiepet = input("Digite a espécie do pet: ")
    racapet = input("Digite a raça do pet: ")
    
    pets.append([nomepet, donocpf, especiepet, racapet])
    print("Pet cadastrado com sucesso!")

def atualizar_pet():
    if not pets:
        print("Não há pets cadastrados.")
        return
    nomepet = input("Digite o nome do pet para atualizar: ")
    for i in range(len(pets)):
        if pets[i][0] == nomepet:
            novonome = input("Digite o novo nome do pet: ")
            donocpf = input("Digite o novo CPF do dono: ")  
            pets[i] = [novonome, donocpf, pets[i][3], pets[i][4]]
            print("Pet atualizado com sucesso!")
            return
    print("Pet não encontrado.") 

def apagar_pet():
    if not pets:
        print("Não há pets cadastrados.")
        return
    nomepet = input("Digite o nome do pet para remover: ")
    for i in range(len(pets)):
        if pets[i][0] == nomepet:
            del pets[i]
            print("Pet removido com sucesso!")
            return
    print("Pet não encontrado.")

def consultar_pet():
    if not pets:
        print("Não há pets cadastrados.")
        return
    else:
        pet = input("Digite o nome do pet para consultar: ")
    
        pet_encontrado = False  
        for pet in pets:  
            if pet == pets[0]:  
                print(f"Nome: {pet[0]}, Dono: {pet[1]}, Espécie: {pet[2]}, Raça: {pet[3]}")
                pet_encontrado = True
                break
        if not pet_encontrado:
            print("Pet não encontrado.")

#Funçôes Atendimento...
def iniciar_atendimento():
    if not pets:
        print("Não há pets cadastrados para atendimento.")
        return
    nomepet = input("Digite o nome do pet para iniciar o atendimento: ")
    for pet in pets:
        if pet[0] == nomepet:
            dono = pet[1]
            servico = input("Digite o serviço prestado: ")
            datatendimento = input("Digite a data do atendimento (DD/MM/AAAA): ")
            atendimentos.append([nomepet, dono, servico, datatendimento])
            print("Atendimento iniciado com sucesso!")
            return
    print("Pet não encontrado.")

def agendar_atendimento():
    if not pets:
        print("Não há pets cadastrados para agendamento.")
        return
    nomepet = input("Digite o nome do pet para agendar o atendimento: ")
    for pet in pets:
        if pet[0] == nomepet:
            dono = pet[1]
            datagendada = input("Digite a data para agendar o atendimento (DD/MM/AAAA): ")
            atendimentos.append([nomepet, dono, "Agendado", datagendada])
            print("Atendimento agendado com sucesso!")
            return
    print("Pet não encontrado.")

def remarcar_atendimento():
    if not atendimentos:
        print("Não há atendimentos agendados.")
        return
    nomepet = input("Digite o nome do pet para remarcar o atendimento: ")
    for atendimento in atendimentos:
        if atendimento[0] == nomepet:
            novadata = input("Digite a nova data para o atendimento (DD/MM/AAAA): ")
            atendimento[3] = novadata
            print("Atendimento remarcado com sucesso!")
            return
    print("Pet não encontrado ou sem atendimentos agendados.")

#Função consulta/Relatório..
def consulta_relatorio_1():
    if not atendimentos:
        print("Não há atendimentos registrados.")
        return
    print("Relatório de Todos os Atendimentos:")
    for atendimento in atendimentos:
        print(f"Pet: {atendimento[0]}, Dono: {atendimento[1]}, Serviço: {atendimento[2]}, Data: {atendimento[3]}")

#Funções para serviços..
def menu_servicos():
    print("1. Cadastrar (Apenas ADM)")
    print("2. Atualizar (Próprio usuário)")
    print("3. Apagar (Apenas ADM)")
    print("4. Consultar")
    print("5. Voltar")

def cadastrar_servico():   
    opcao1 = int(input("Digite a opção que você deseja cadastrar:\n"))

    nomeservico = input("Digite o tipo do serviço: ")
    precoservico = float(input("Digite o preço do serviço: "))
    
    servicos.append([nomeservico, precoservico])
    print("Serviço cadastrado com sucesso!")

def atualizar_servico():
    if not servicos:
        print("Não há serviços cadastrados.")
        return
    nomeservico = input("Digite o tipo do serviço para atualizar: ")
    for i in range(len(servicos)):
        if servicos[i][0] == nomeservico:
            novonome = input("Digite o novo tipo do serviço: ")
            novopreco = float(input("Digite o novo preço do serviço: "))
            servicos[i] = [novonome, novopreco]
            print("Serviço atualizado com sucesso!")
            return
    print("Serviço não encontrado.")

def apagar_servico():
    if not servicos:
        print("Não há serviços cadastrados.")
        return
    nomeservico = input("Digite o tipo do serviço para remover: ")
    for i in range(len(servicos)):
        if servicos[i][0] == nomeservico:
            del servicos[i]
            print("Serviço removido com sucesso!")
            return
    print("Serviço não encontrado.")

def consultar_servico():
    if not servicos:
        print("Não há serviços cadastrados.")
        return
    for servico in servicos:
        print(f"Tipo do serviço: {servico[0]}, Preço: R$ {servico[1]:.2f}")

#Funções direcionadas aos clintes.
def menu_clientes():
    print("1. Cadastrar (Apenas ADM)")
    print("2. Atualizar (Próprio usuário)")
    print("3. Apagar (Apenas ADM)")
    print("4. Consultar")
    print("5. Voltar")

def cadastro_cliente():
            
        if len(clientes) == 0:
            print("Não há clientes cadastrados. Cadastre um cliente.")
            
            nomecliente = input("Digite o nome do novo cliente: ")
            senha = input("Digite a senha: ")
            cpf = int(input("Digite o CPF: "))

            clientes.append([nomecliente, senha, 'C', cpf])
            print("Cliente cadastrado com sucesso!")
    
        else:
            nomecliente = input("Digite o nome do novo cliente: ")
            senha = input("Digite a senha: ")
            cpf = int(input("Digite o CPF: "))
            for i in range (len(clientes)):
                if cpf == clientes[i][3]:
                    print("Clinte já registrado! Cadastre um novo!")
                    return False
            clientes.append([nomecliente, senha, 'C', cpf])
            print("Cliente cadastrado com sucesso!")

def login_cliente():
    global usuario_logado, tipo
    while True:
        nomecliente = input("Digite o cliente para login: ")
        senha = input("Digite a senha: ")
        for i in range(len(clientes)):
            if nomecliente == clientes[i][0] and senha == clientes[i][1]:
                usuario_logado = clientes
                tipo = 'C'
                print("Cliente autenticado.")
                return tipo
        else:
            print("Cliente ou senha inválido!")
            return None

def atualizar_cliente():
    if len(clientes) == 0:
        print("Não há clientes cadastrados.")
        return
    while True:
        nomecliente = input("Digite o nome do cliente para atualizar: ")
        for i in range(len(clientes)):
            if nomecliente == clientes[i][0]:
                novasenha = input("Digite a nova senha: ")
                clientes[i][1] = novasenha

                print("Atualização realizada com sucesso!")
                return True

            else:
                print("Cliente não encontrado.")

def apagar_cliente():
    if len(clientes) == 0:
        print("Não há clientes cadastrados.")
        return 
    while True:
        nomecliente = input("Digite o nome do cliente para remove-lo: ")
        for i in range(len(clientes)):
            if nomecliente == clientes[i][0]:
                del clientes[i]
                print("Cliente removido com sucesso!")
                return True

def consultar_cliente():
    if len(clientes) == 0:
        print("Não há clientes cadastrados.")
        return
    else:
        senhacliente = input("Digite a senha do cliente para consultar: ")
    
        cliente_encontrado = False
        for cliente in clientes:  
            if senhacliente == cliente[1]:  
                print(f"Nome: {cliente[0]}, Senha: {cliente[1]}, Tipo: {cliente[2]}, CPF: {cliente[3]}")
                cliente_encontrado = True
                break
        if not cliente_encontrado:
            print("Cliente não encontrado.")

