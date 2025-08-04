d = int(input('Quantos dias alugados: '))
k = float(input('Quantos km rodados: '))
c = (d * 60) + (k * 0.15)
print('O aluguel do carro custará R${:.2f}'.format(c))