#Faça um programa que calcule a soma de todos os números ímpares que 
#são múltiplos de três e que se encontram no intervalo de 1 até 500.
soma = 0
cont = 0
for c in range (1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print('São {} valores somados, dando um total de {}'.format(cont, soma))