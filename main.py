import os

def exibir_menu():
    print("Menu de Opções:\n")
    print("1- Cadastrar novo usuário")
    print("2- Listar usuários cadastrados")
    print("3- Cadastrar novo animal")
    print("4- Listar animais cadastrados")
    print("5- Sair\n")

    opcao_escolhida = int(input("Digite a opção desejada:\n"))
    os.system('cls')

    escolher_opcao(opcao_escolhida)

def escolher_opcao(opcao_menu):
    if opcao_menu == 1:
        cadastrar_usuario()
    elif opcao_menu == 2:
        listar_usuarios()
    elif opcao_menu == 3:
        cadastrar_animal()
    elif opcao_menu == 4:
        listar_animais()
    elif opcao_menu == 5:
        print("Saindo do programa...")
        os.system('cls')
    else:
        print("Opção inválida. Tente novamente.")
        exibir_menu()

def cadastrar_usuario():
    nome_usuario = input("Digite o nome do usuário: ")
    email_usuario = input("Digite o email do usuário: ")
    telefone_usuario =  input("Digite o telefone do usuário: ")
    print(f"Seja bem-vindo(a) ao patitas, {nome_usuario}! Seu novo amiguinho está esperando por você :)")

def listar_usuarios():
    print("Lista de usuários cadastrados:")

def cadastrar_animal():
    nome_animal = input("Digite o nome do animal: ")
    especie_animal = input("Digite a espécie do animal: ")
    idade_animal = input("Digite a idade do animal: ")
    print(f"O animal {nome_animal} foi cadastrado com sucesso!")

def listar_animais():
    print("Lista de animais cadastrados:")

    exibir_menu()