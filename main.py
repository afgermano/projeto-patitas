import os

def limpar_tela():
    os.system('cls')


def listar_menu(animais):
    """
    Exibe o menu principal e controla o fluxo das opções que o usuário irá escolher
    """
    while True:
        print('PATITAS! - SEU MELHOR AMIGO ESTÁ AQUI!')
        print('*' * 40)
        print('1 - Cadastrar animal')
        print('2 - Listar animais cadastrados')
        print('3 - Alterar exibição do animal')
        print('4 - Sair')

        try:
            opcao = int(input('Escolha uma opção do menu: '))

            if opcao == 1:
                cadastrar_novo_animal(animais)
            elif opcao == 2:
                listar_animais_cadastrados(animais)
            elif opcao == 3:
                alterar_status_de_exibicao(animais)
            elif opcao == 4:
                sair_do_patitas()
                break
            else:
                print('Opção inválida! Tente novamente.\n')

        except ValueError:
            print('Digite um número válido!\n')


def cadastrar_novo_animal(animais):
    """
    Cadastra um novo animal
    """
    nome = input('Nome do animal: ')
    especie = input('Espécie do animal: ')

    while True:
        try:
            idade = int(input('Idade do animal (em meses): '))
            break
        except ValueError:
            print('Digite uma idade válida.')
    descricao = input('Fale um pouco sobre nosso novo amigo: ')

    dados_novo_animal = {
        'nome': nome,
        'especie': especie,
        'idade': idade,
        'descricao': descricao,
        'status': True
    }

    animais.append(dados_novo_animal)

    print(f'\nVamos dar boas vidas ao nosso novo amigo {nome}! 🐾\n')
    input('Pressione ENTER para voltar ao menu...')
    limpar_tela()


def listar_animais_cadastrados(animais):
    """
    Lista todos os animais cadastrados
    """
    if not animais:
        print('Nenhum animal cadastrado ainda.\n')
    else:
        print('Animais Cadastrados:\n')
        print('*' * 40)

        for animal in animais:
            print(
                f"Nome: {animal['nome']} | "
                f"Espécie: {animal['especie']} | "
                f"Idade: {animal['idade']} meses | "
                f"Descrição: {animal['descricao']} |"
                f"Status animal: {animal['status']}"
            )
            print('*' * 40)

    input('\nPressione ENTER para voltar ao menu...')
    limpar_tela()

def alterar_status_de_exibicao(animais):
    nome_animal = input('Digite o nome do nosso amiguinho: ')
    animal_encontrado = False

    for animal in animais:
        if nome_animal == animal['nome']:
            animal_encontrado = True
            animal['status'] = not animal['status']
            
            if animal['status']:
                print(f'O animal {nome_animal} será exibido no sistema!')
            else:
                print(f'O animal {nome_animal} foi retirado da exibição')
        
    if not animal_encontrado:
        print(f'{nome_animal} não foi encontrado ☹ ')
        
    input('\nPressione ENTER para voltar ao menu...')
    limpar_tela()


def sair_do_patitas():
    """
    Finaliza o sistema
    """
    limpar_tela()
    print('Obrigada por usar o Patitas! 🐶🐱')


def main():
    animais = [
        {'nome': 'Mike', 'especie': 'Cachorro', 'idade': 4, 'descricao': 'Ele é bricalhão e carinhoso', 'status': True}
    ]
    listar_menu(animais)


if __name__ == '__main__':
    main()