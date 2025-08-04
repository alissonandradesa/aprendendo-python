salario = float(input('Digite o valor do salário R$: '))
if salario <= 1250.00:
    aumento = salario + (salario * (15/100))
else:
    aumento = salario + (salario * (10/100))
print('Seu novo salario é R$: {:.2f} reais'.format(aumento))