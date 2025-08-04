"""Escreva um programa que leia a velociadade de um carro
e se ele ultrapassar 80km/h mostre uma mensagem dizendo que
ele foi multado a multa vai custar 7 reais por cada km acima do limite"""
vel = int(input('Digite a velocidade de seu carro: '))
if vel > 80:
    mul = (vel -80) * 7
    print('Você está a cima da velocidade de 80km/h com {} a cima e sua multa será de R${:.2f} ' .format((vel-80),mul))
else:
    print('Você está com a velocidade compatível com a via')