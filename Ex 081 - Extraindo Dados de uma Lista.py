#Crie um programa que vai ler vários números e 
#colocar em uma lista. 
#Depois disso, mostre: 
# Quantos números foram digitados;
# A lista de valores ordenada de forma decrescente;
# Se o valor 5 foi digitado e está ou não na lista.
cont = 0
pos = 1
lista = []
num = int(input(f'Digite o {pos}° valor: '))
lista.append(num)
cont += 1
opção = input('Deseja adicionar mais números? [S/N]\n').upper()[0]
while True:
    if opção == 'N':
        break
    elif opção == 'S':
        pos += 1
        num = int(input(f'Digite o {pos}° valor: '))
        lista.append(num)
        cont += 1
        opção = input('Deseja adicionar mais números? [S/N]\n').upper()[0]
    else:
        while 'S' != opção != 'N':
            print('Desculpe, não entendi.')
            opção = input('Deseja adicionar mais números? [S/N]\n').upper()[0]
print('-'*30)
print(lista)
print(f'Foram digitados {'\033[33m'}{cont}{'\033[m'} números')
listaReverse = lista[:]
listaReverse.sort(reverse=True)
print(f'Lista em ordem {'\033[4m'}decrescente{'\033[m'}: {listaReverse}')
for c in range (0, len(lista)):
    if lista[c] == 5:
        print(f'Há um número {'\033[32m'}5{'\033[m'} na posição {'\033[36m'}{c+1}{'\033[m'}')
    else:
        c += 1
if 5 not in lista:
    print(f'O número {'\033[31m'}5{'\033[m'} não foi digitado')
    
