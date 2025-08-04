"""Crie um programa que leia o nome completo
de uma pessoa e mostre:
1- nome com todas as letras maiúsculas
2- nome com todas as letras minúsculas
3- quantas letras ao todo sem espaços
quantas letras tem o primeiro nome"""
import string
nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em maíusculo é {} ' .format(nome.upper()))
print('Seu nome em minúsculo é {} ' .format(nome.lower()))
print('Seu nome ao todo tem {} letras ' .format((len(nome) - nome.count(' '))))
print('seu primeiro nome tem {} letras ' .format(nome.find(' ')))
separa = nome.split()
print('Seu peimeiro nome é {}  e ele tem {} letras' .format(separa[0], nome.find(' ')))