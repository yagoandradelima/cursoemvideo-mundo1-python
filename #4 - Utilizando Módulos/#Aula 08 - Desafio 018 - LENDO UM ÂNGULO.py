#Aula 08 - Desafio 018 - LENDO UM ÂNGULO

import math

ang = int(input('Digite o ângulo: '))
seno = math.sin(ang)
coss = math.cos(ang)

print(f'O seno de {ang} é {math.ceil(seno)} e o cosseno é {math.ceil(coss)}')