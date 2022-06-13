# Programa de Detecção de caracter

sexo = str(input('''Qual o sexo que você se identifica?
Selecione entre: 
F para Feminino
M para Masculino
NB para Não-Binário\n'''))
sexo = sexo.upper()
if sexo == 'F':
    print('Voce escolhe o sexo Feminino')
elif sexo == 'M':
    print('Voce escolheu o sexo Masculino')
elif sexo == 'NB':
    print('Você escolheu Não-Binario')
else:
    print('O caracter selecionado é invalido, tente novamente')
