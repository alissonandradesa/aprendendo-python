import math
from math import radians

a = float(input('Informe um ângulo: '))
s = math.sin(radians(a))
c = math.cos((radians(a)))
t = math.tan((radians(a)))
print('Para o ângulo {:.2f} teremos o Seno {:.2f}, o Coseno {:.2f} e a Tangente{:.2f}' .format(a, s, c, t))