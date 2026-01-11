import os

info_patitas = [{}]

def listar_menu():
    print('PATITAS! - SEU MELHOR AMIGO ESTÁ AQUI!')
    print('*' * 40)
    print('1 - Cadastrar Animal')
    print('2 - Listar Animais Cadastrados')
    print('3 - Sair')

def opcao_escolhida_menu():
    opcao_menu = int(input('Escolha uma opção do menu: '))
    if opcao_menu == 1:
        cadastrar_novo_animal()
    elif opcao_menu == 2:
        listar_animais_cadastrados()
    elif opcao_menu == 3:
        sair_do_patitas()
    else:
        print('Opção inválida! Tente novamente.\n')
        os.system('cls')
        listar_menu()

def cadastrar_novo_animal():
    nome = input('Nome do animal; ')
    especie = input('Espécie do animal: ')
    idade = input('Idade do animal:')
    dados_novo_animal = {
        'nome': nome,
        'especie': especie,
        'idade': idade
    }
    info_patitas.append(dados_novo_animal)
    print(f'Vamos dar boas vidas ao nosso novo amigo {nome}!\n')

    print('Aperte qualquer tecla para voltar ao menu principal')
    listar_menu()

def listar_animais_cadastrados():
    print('Animais Cadastrados:\n')
    print('*' * 40)
    for animal in info_patitas:
        nome_animal = animal['nome']
        especie_animal = animal['especie']
        idade_animal = animal['idade']
        print(f'Nome: {nome_animal} | Espécie: {especie_animal} | Idade: {idade_animal}')
        print('*' * 40 + '\n')

def sair_do_patitas():
    print('Obrigada por usar o Patitas!')
    os.system('cls')

def main():
    listar_menu()
    opcao_escolhida_menu()

if __name__ == '__main__':
    main()