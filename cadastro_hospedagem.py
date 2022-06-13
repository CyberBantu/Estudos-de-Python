# Cadastro De grupo

print('*'*5, 'Olá bem Vindo ao Hotel Bantu, vou te solicitar algumas Informações', '*'*5)

rep = int(input('Quantas pessoas são para a Hospetagem?'))
i = 0
grupo = []
while i < rep:
    i += 1
    nome = input('Qual é o seu nome?\n')
    if nome == '':
        print('Nome Invalido')
        break
    else:
        print('Olá {}!'.format(nome))
    # coletando idade
    idade = int(input('Qual a sua idade?\n'))
    if idade < 18:

        print('{}, você não tem idade o suficiênte para fazer o cadastro.\n'.format(nome))

        break
    else:

        print('Você tem a idade permitida\n')
    # Coletando Cidade

    cidade_nascimento = input('Qual a cidade que voce nasceu?\n')

    if cidade_nascimento == '':
        print('Sua Cidade é Invalidade.\n')
        break

    grupo.append(nome)


print(grupo)
