print('''
Bem vindo a Enquete de qual é o melhor sistema operacional
Escola entre os Sistemas Operacionais:
1 - Linux
2 - Windows
3 - Mac
4 - Unix
5 - Outros
''')
# COntador
pessoas = int(input('Quantas pessoas iram votar?'))
contador = 0
# vARIAVEIS
linux = 0
windows = 0
mac = 0
unix = 0
outros = 0

while contador < pessoas:
    contador += 1
    voto = int(input('Digite o numero do seu sistema Favorito:'))

    if voto == 1:
        print('Seu voto foi para o Linux')
        linux += 1
    elif voto == 2:
        print('Seu voto foi para Windows')
        windows += 1
    elif voto == 3:
        print('Seu voto foi para MAC')
        mac += 1
    elif voto == 4:
        print('Seu voto foi para Unix')
        unix += 1
    elif voto == 5:
        print('Seu voto foi para outros')
        outros += 1
    else:
        print('Digito Invalido')


print(''' O placar atual é de:
Linux = {}
Windows = {}
Mac = {}
Unix = {}
Outros = {}
'''.format(linux, windows, mac, unix, outros))
