midade = 0
cont = 0
imaisvelho = 0
nmaisvelho = ''
for c in range(1,5):
    print(f'--------------{c}ª pessoa---------------------')
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite M para masculino e F para feminino: ')).upper()
    midade += idade
    if c == 1 and sexo == 'M':
        imaisvelho = idade
        nmaisvelho = nome
    if sexo == 'M' and idade > imaisvelho:
        imaisvelho = idade
        nmaisvelho = nome
    if sexo == 'F' and idade < 20:
        cont += 1
media = midade / c
print(f"""A média de idade do grupo é {media:.0f}
O homem mais velho é {nmaisvelho.upper()} e sua idade é {imaisvelho}
Existem {cont} mulherer (s) com menos de 20 anos""")