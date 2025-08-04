n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
d = n1 / n2
p = n1 * n2
e = n1 ** n2
di = n1 // n2
r = n1 % n2
print( 'A soma é {}, \n a divisão é {:.3f} \n o produto é {}, '
       '\n a potencia é {} \n a divisão inteira é: {} \n e o resto é: {} '
       .format(s, d, p, e, di, r))