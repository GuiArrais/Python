#Crie um programa que vai ler vários números e 
#colocar em uma lista.
#Depois disso, crie duas listas extras que vão 
#conter apenas os valores pares e os valores 
#ímpares digitados, respectivamente.
#Ao final, mostre o conteúdo das três listas 
#geradas.
lista = []
par = []
impar = []
pos = 1
num = int(input(f'Digite o {pos}° valor: '))
lista.append(num)
opção = input('Deseja adicionar mais valores? [S/N]\n').upper()[0]
while True:
    if opção == 'S':
        pos += 1
        num = int(input(f'Digite o {pos}° valor: '))
        lista.append(num)
        opção = input('Deseja adicionar mais valores? S/N\n').upper()[0]
    elif opção == 'N':
        break
    else:
        print('Desculpe, não entendi')
        opção = input('Deseja adicionar mais valores? S/N\n').upper()[0]
for c in range(0, len(lista)):
    if lista[c] % 2 == 0:
        par.append(lista[c])
    else:
        impar.append(lista[c])
    c += 1
print(lista)
print(f'Par: {par}')
print(f'Impar: {impar}')