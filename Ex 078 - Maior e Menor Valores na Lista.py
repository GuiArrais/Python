#Faça um programa que leia 5 valores numéricos e 
#guarde-os em uma lista.
#No final, mostre qual foi o maior e o menor valor 
#digitado e as suas respectivas posições na lista.
lista = []
maior = menor = 0
for c in range(0,5):
    lista.append(int(input(f'Digite o {c+1}º valor: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print(lista)
print(f'O {'\033[4m'}MAIOR{'\033[m'} valor é {'\033[34m'}{maior}{'\033[m'} na posição: ',end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}...',end='')
print()
print(f'O {'\033[4m'}MENOR{'\033[m'} valor é {'\033[36m'}{menor}{'\033[m'} na posição: ',end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}...',end='')
print()