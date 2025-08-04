from time import sleep
print('-=-' * 20)
print('\33[1;32;30mANALISADOR DE TRIANGULOS')
print('-=-' * 20)
r1 = float(input('\33[7;30mDigite o comprimento da reta 1: '))
r2 = float(input('\33[7;30mDigite o comprimento da reta 2: '))
r3 = float(input('\33[7;30mDigite o comprimento da reta 3: '))
print('Analisando...')
sleep(3)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas podem formar um triangulo')
else:
    print('As retas nao podem formar um triangulo')
