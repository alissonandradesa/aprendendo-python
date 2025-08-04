"""Programa que leia uma frase
pelo teclado e mostre
1- quantas vexes aparece a letra a
2- em que posição ela aparece a primeira vesz
3- em que posição ela aparece a última vez"""
frase = str(input('Digite uma frase: ')).strip()
print('A letra A aparece {} vezes '.format(frase.lower().count('a')))
print('A primeira vez que a letra A aparece é {}' .format(frase.lower().find('a') + 1))
print('A letra A aparece a ultima vez na posição {} ' .format(frase.lower().rfind('a') + 1))