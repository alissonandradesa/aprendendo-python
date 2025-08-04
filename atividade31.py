km = int(input('Qual a distancia da viagem em km: '))
if km <= 200:
    valor = km * 0.50
    print('Para uma viagem de {}km a passagem custará R${:.2f}'.format(km, valor))
else:
    valor = km * 0.45
    print('Para uma viagem de {}km a pasagem custará R${:.2f}'.format(km, valor))
