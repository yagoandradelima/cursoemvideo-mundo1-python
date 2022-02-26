#Aula09 - Manipulando Strings

frase = 'Curso em Vídeo Python'

#Dentro de uma frase, cada caracter é como se fosse um local de uma lista. eu posso fatiar a lista normalmente.

#Fatiando um único caractere
print(frase[6])
print()

#Fatiando um intervalo definido
print(frase[9:15])
print()

#Fatiando um intervalo com final 1 valor acima do máximo
print(frase[9:21])
print()

#Fatiando um intervalo sem início definido
print(frase[:9])
print()

#Fatiando sem final definido
print(frase[10:])
print()

#Fatiando com saltos durante o intervalo
#O número 2 significa quantos caracteres ele vai pular até o próximo print
print(frase[2:17:2])
print()

#Fatiando tudo com final indefinido e saltos
print(frase[7::3])
print()

#Desconbrindo o comprimendo de caracteres da frase
print(len(frase))
print()

#Printando um contador de determinado caracter
print(frase.count('o'))
print()

#Contagem em um intervalo fatiado
print(frase.count('o',0,13))
print()

#Encontrando uma cadeia de caractere(ou o que eu colocar no ())
#Ele retorna o primeiro intervalo onde começou o que eu procuro
#Se ele não encontrar, ele retorn -1 (não existe)
print(frase.find('deo'))
print()

#Questionamentos futuros para recursos de repetição
#Ele retorna booleano
'Curso' in frase

#Reposicionar e trocar
#Ele trocou Python por Android
frase.replace('Python', 'Android')
print(frase)



