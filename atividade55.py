maior = 0
menor = 1000
for c in range(1,6):
    peso = float(input(f'Digite o peso da {c}ª pessoa em Kg: '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print(f'O maior peso é {maior}kg \nO menor peso é {menor}')
