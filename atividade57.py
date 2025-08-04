sexo = str(input('Digite seu sexo [F/M]: '))
while sexo not in 'FfMm':
    sexo = str(input('Dados invalidos, por favor digite o sexo [F/M]: ')).upper().strip()[0]
print(f'O sexo escolhido foi {sexo}')