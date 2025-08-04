"""Programa que leia o nome completo de uma pessoa e
mostre em seguida o primeiro e o último nome separadamente
ex Ana Maria de Souza
primeiro = Ana
último = Souza"""
nome = str(input('Digite seu nome Completo: '))
n = nome.split()
print('Seu primeiro nome é {} e seu ultimo nome é {} ' .format(n[0], n[len(n) - 1]))