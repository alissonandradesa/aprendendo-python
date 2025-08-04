din = float(input('Quanto em dinheiro você tem na sua carteira: '))
dol = din // 3.27
sob = din % 3.27
print('Você consegue comprar {} dolares com seus {} reais e sobraram {} reais' .format(dol, din, sob))