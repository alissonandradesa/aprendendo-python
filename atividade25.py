"""crie um programa que leia um nome
de uma pessoa e diga se ela tem silva no nemo"""
nome =  str(input('Digite seu nome completo: ')).strip()
print('Seu nome tem Silva: {} '.format('silva' in nome.lower()))