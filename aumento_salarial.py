# Calcular Aumento dos colaboradores

print('*'*5, 'Olá, bem vindo ao Software de Calculo de Reajuste', '*'*5, '\n')

salario = float(
    input('Insira aqui o seu salario que calcularemos os Reajustes: \n'))

if salario:
    print('Seu salario era de R$ {}'.format(round(salario, 2)))
    if salario <= 280:
        reajuste = (salario * 0.2) + salario
        valor_aumento = salario * 0.2
        print('O seu novo salário é de R${}, foi aplicado reajuste de 20 %, e o valor do aumento de R${}'.format(
            round(reajuste, 2), round(valor_aumento, 2)))
    elif salario > 280 and salario < 700:
        reajuste = (salario * 0.15) + salario
        valor_aumento = salario * 0.15
        print('O seu novo salário é de R${}, foi aplicado reajuste de 15 %, e o valor do aumento de R${}'.format(
            round(reajuste, 2), round(valor_aumento, 2)))
    elif salario > 700 and salario < 1500:
        reajuste = (salario * 0.1) + salario
        valor_aumento = salario * 0.1
        print('O seu novo salário é de R${}, foi aplicado reajuste de 10 %, e o valor do aumento de R${}'.format(
            round(reajuste, 2), round(valor_aumento, 2)))
    else:
        reajuste = (salario * 0.05) + salario
        valor_aumento = salario * 0.05
        print('O seu novo salario é R${}, foi aplicado reajuste de 5 %, e o valor do aumento de {}', format(
            round(reajuste, 2), valor_aumento))
else:
    print('Você precisa digitar um valor')


print('Fim do Programa')
