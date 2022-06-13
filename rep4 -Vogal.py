print('*'*5, 'Escreva uma letra e direi se é vogal ou consoante', '*'*5, '\n')
letra = str(input('Digite uma letra: \n'))

letra.upper()

# vogais
vogais = ['A', 'E', 'I', 'O', 'U']

if letra in vogais:
    print('Sua letra é uma vogal')
else:
    print('Sua letra é uma consoante')

print('*'*20)
