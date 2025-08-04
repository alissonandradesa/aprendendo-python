"""Escreva um programa que faça o computador
pensar em um numero inteiro entre 0 e 5
e peça para o usuario tentar descobrir
qual foi o numero escolhido pelo computador
o programa deverá escrever na tela de o usuario
venceu ou perdeu"""
from random import randint
from time import sleep
print('-[]-' * 20)
n = randint(0,5)
num = int(input('Descubra qual número o computador sorteou de 0 a 5: '))
print('-[]-' * 20)
print('Processando...')
sleep(3)
if n == num:
    print('Você acertou, Parabéns!')
else:
    print('Você errou, tente novamente.')
print(n)