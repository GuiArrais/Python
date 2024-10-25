#Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, 
#mostrando os 10 primeiros termos da progressão usando a estrutura 
#while.
cont = 0
n = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão dessa PA: '))
while cont < 10:
    if cont != 9:
        print(n, end=' → ')
    else:
        print(n)
    n += r
    cont += 1
