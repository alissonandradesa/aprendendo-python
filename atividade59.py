num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro numero: '))
print("""[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos numeros
[5] Sair do programa""")
c = False
while not c:
    opcao = int(input('Escolha uma opção:'))
    if opcao == 1:
        soma = num1 + num2
        print(f'A soma é {soma}')
    elif opcao == 2:
        mult = num1 * num2
        print(f'A mutiplicação é {mult}')
    elif opcao == 3:
        if num1 > num2:
            print(f'{num1} é maior que {num2}')
        else:
            print(f'{num2} é maior que {num1}')
    elif opcao == 4:
        print('Escolha novos numeros')
        num1 = float(input('Digite um número: '))
        num2 = float(input('Digite outro numero: '))
    elif opcao == 5:
        c = True
    else:
        print('Opção invalida!')
print('Saiu do programa')
