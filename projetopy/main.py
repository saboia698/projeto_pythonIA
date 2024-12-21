import json

def criar_arquivo_json():
    usuarios = [
        {"nome": "João", "idade": 25},
        {"nome": "Maria", "idade": 30}
    ]
    with open("usuarios.json", "w") as arquivo:
        json.dump(usuarios, arquivo, indent=4)
    print("Arquivo JSON criado com sucesso!")

def adicionar_usuario():
    try:
        with open("usuarios.json", "r") as arquivo:
            usuarios = json.load(arquivo)
        
        nome = input("Digite o nome do usuário: ")
        idade = int(input("Digite a idade do usuário: "))
        novo_usuario = {"nome": nome, "idade": idade}

        usuarios.append(novo_usuario)

        with open("usuarios.json", "w") as arquivo:
            json.dump(usuarios, arquivo, indent=4)
        print("Usuário adicionado com sucesso!")
    except FileNotFoundError:
        print("Arquivo não encontrado. Crie o arquivo primeiro.")
    except ValueError:
        print("Por favor, insira uma idade válida.")

def exibir_usuarios():
    try:
        with open("usuarios.json", "r") as arquivo:
            usuarios = json.load(arquivo)

        print("Usuários registrados:")
        for usuario in usuarios:
            print(f"Nome: {usuario['nome']}, Idade: {usuario['idade']}")
    except FileNotFoundError:
        print("Arquivo não encontrado. Crie o arquivo primeiro.")

def excluir_usuario():     ##Implementação de excluir usuario
    try:
        with open("usuarios.json", "r") as arquivo:
            usuarios = json.load(arquivo)

        nome_remover = input("Digite o nome do usuário a ser excluído: ")
        usuario_encontrado = False
        
        for usuario in usuarios:
            if usuario['nome'].lower() == nome_remover.lower():
                usuarios.remove(usuario)
                usuario_encontrado = True
                break
        
        if usuario_encontrado:
            with open("usuarios.json", "w") as arquivo:
                json.dump(usuarios, arquivo, indent=4)
            print(f"Usuário {nome_remover} excluído com sucesso!")
        else:
            print(f"Usuário {nome_remover} não encontrado.")
    except FileNotFoundError:
        print("Arquivo não encontrado. Crie o arquivo primeiro.")

def editar_usuario():   ##Implementação de editar usuario
    try:
        with open("usuarios.json", "r") as arquivo:
            usuarios = json.load(arquivo)

        nome_editar = input("Digite o nome do usuário a ser editado: ")
        usuario_encontrado = False
        
        for usuario in usuarios:
            if usuario['nome'].lower() == nome_editar.lower():
                usuario_encontrado = True
                print(f"Usuário encontrado: {usuario['nome']}, Idade: {usuario['idade']}")
                
                novo_nome = input(f"Digite o novo nome (deixe em branco para manter '{usuario['nome']}'): ")
                if novo_nome:
                    usuario['nome'] = novo_nome
                
                try:
                    nova_idade = int(input(f"Digite a nova idade (deixe em branco para manter {usuario['idade']}): "))
                    usuario['idade'] = nova_idade
                except ValueError:
                    print("Idade não modificada. Valor inválido.")
                
                break
        
        if usuario_encontrado:
            with open("usuarios.json", "w") as arquivo:
                json.dump(usuarios, arquivo, indent=4)
            print("Usuário editado com sucesso!")
        else:
            print(f"Usuário {nome_editar} não encontrado.")
    except FileNotFoundError:
        print("Arquivo não encontrado. Crie o arquivo primeiro.")

def buscar_usuario():    ##Implementação de buscar usuario
    try:
        with open("usuarios.json", "r") as arquivo:
            usuarios = json.load(arquivo)

        nome_buscar = input("Digite o nome do usuário a ser buscado: ")
        usuario_encontrado = False
        
        for usuario in usuarios:
            if usuario['nome'].lower() == nome_buscar.lower():
                usuario_encontrado = True
                print(f"Usuário encontrado: Nome: {usuario['nome']}, Idade: {usuario['idade']}")
                break
        
        if not usuario_encontrado:
            print(f"Usuário {nome_buscar} não encontrado.")
    except FileNotFoundError:
        print("Arquivo não encontrado. Crie o arquivo primeiro.")

print("Bem-vindo ao Gerenciador de Usuários JSON!")
while True:
    print("\nEscolha uma opção:")
    print("1. Criar arquivo JSON")
    print("2. Adicionar usuário")
    print("3. Exibir usuários")
    print("4. Excluir usuário")
    print("5. Editar usuário")
    print("6. Buscar usuário")
    print("7. Sair")

    opcao = input("Digite sua escolha: ")

    if opcao == "1":
        criar_arquivo_json()
    elif opcao == "2":
        adicionar_usuario()
    elif opcao == "3":
        exibir_usuarios()
    elif opcao == "4":
        excluir_usuario()
    elif opcao == "5":
        editar_usuario()
    elif opcao == "6":
        buscar_usuario()
    elif opcao == "7":
        print("Saindo... Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")
