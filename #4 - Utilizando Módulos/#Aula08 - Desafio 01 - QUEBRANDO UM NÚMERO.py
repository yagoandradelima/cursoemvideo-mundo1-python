#Aula08 - Desafio 01

import math

num = float(input('Digite um número inteiro real acima de 3 casas após a vírgula: '))
#A função trunc elimina da vírgula pra frente, deixando só a parte real
vis = math.trunc(num)
print(vis)