#Aula08 - Desafio 020 - ORDEM DE APRESENTAÇÃO

import random

alunos = ('Lucas', 'Mateus', 'Corno', 'Aluno', 'Eu')
contador = 1

while True:
    for i in alunos:
        print(contador)
        k = random.random(i)
        print(f'{contador} - {k}')
    break
print()