# Notas Medias de Aluno
print('*'*5, 'Olá, bem vindo ao Software de Calculo de Medias', '*'*5, '\n')

registros = int(input('Quantos Alunos você quer registrar? \n'))
i = 0

alunos = []

media_alunos = []

alunos_reprovados = 0
alunos_aprovados = 0
alunos_recuperacao = 0

while i <= registros:
    nome = input('Por favor, Insira o seu nome: \n')
    i += 1
    p1 = float(input('Insira a sua nota do primeiro Bimestre: \n'))
    p2 = float(input('Insira a sua nota do Segundo Bimestre: \n'))
    p3 = float(input('Insira a sua nota do Terceiro Bimestre: \n'))

    notas = (p1, p2, p3)

    media = sum(notas) / 3

    if media >= 7:
        alunos_aprovados += 1
        print('Sua média é {} e você foi aprovado'.format(round(media, 1)))
    elif media >= 3 and media < 7:
        alunos_recuperacao += 1
        print('Sua média é {} e você esta de recuperação'.format(round(media, 1)))
    else:
        alunos_reprovados += 1
        print('Sua media é {} e você está reprovado'.format(round(media, 1)))

    alunos.append(nome.upper())
    media_alunos.append(round(media, 2))

print('Nome dos Alunos - ', alunos)
print('Média dos alunos - ', media_alunos)

print('*'*20)

# Alunos aprovados - Reprovados e em Recuperação

print('{} Alunos foram aprovados.\n'.format(alunos_aprovados))
print('{} Alunos estão de recuperação.\n'.format(alunos_recuperacao))
print('{} Alunos foram reprovados.\n'.format(alunos_reprovados))


print('Fim do Programa')
