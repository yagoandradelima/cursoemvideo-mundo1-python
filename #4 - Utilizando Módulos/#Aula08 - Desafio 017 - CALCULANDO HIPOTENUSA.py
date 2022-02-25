#Aula08 - Desafio 017
import math

catOposto = float(input('Digite o tamanho do cateto oposto: '))
catAdj = float(input('Digite o tamanho do cateto adjacente: '))
hip = (catOposto**2) + (catAdj**2)
hipo = float(math.sqrt(hip))
print(f'O valor da hipotenusa é {hipo:.2f}')
print('Fim do programa')