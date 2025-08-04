"""Faça um programa que leia o nome de uma cidade
e diga se a cidade começa ou não com o nome santo"""
c = str(input('Informe o nome da sua cidade: ')).strip()
print(c[:5].lower() == 'santo')
