from datetime import date
cont = 0
cont1 = 0
for c in range(1, 8):
    ano = int(input(f'Digite o ano em que a {c}ª nasceu: '))
    idade = date.today().year - ano
    if idade <= 21:
        cont += 1
    else:
        cont1 += 1
print(f'{cont} pessoas Menor de idade \n{cont1} Maior de idade')
