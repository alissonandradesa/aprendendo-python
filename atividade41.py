from datetime import date
ano = int(input('Informe o ano de nascimento do atleta: '))
idade = date.today().year - ano
print('O atleta tem {} anos' .format(idade))
print('Categoria')
if idade <= 9:
    print('MIRIM')
elif idade > 9 and idade <=14:
    print('INFANTIL')
elif idade > 14 and idade <= 19:
    print('JUNIOR')
elif idade > 19 and idade <= 25:
    print('SENIOR')
else:
    print('MASTER')