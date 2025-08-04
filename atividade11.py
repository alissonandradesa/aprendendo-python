alt = float(input('Digite qual tamanho da altura da parede: '))
lar = float(input('Digite qual tamanho da Largura da parede: '))
are = alt * lar
pin = are / 2
print('Para pintar uma área de {}m², você precisará de {} baldes de tintas' .format(are, pin))