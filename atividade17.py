import math
from math import hypot

co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do catete adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}  ' .format(hi))