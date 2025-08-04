from random import randint
n = randint (0,10)
print('-=' * 20)
print("""Acabei de pensar um número de 0 a 10
Será que você consegue adivinhar?""")
acertou = False
c = 0
while not acertou:
    num = int(input('Dê seu palpite: '))
    c += 1
    if n == num:
        acertou = True
    else:
        if n > num:
            print('-=' * 25)
            print('mais... Tente mais uma vez: ')
        elif n < num:
            print('menos... Tente novamente: ')
print(f'Você acertou! parabéns!!! foram {c} tentativas')
