#Faça um programa que leia um número inteiro e diga se ele é ou não 
#um número primo.
cont = 0
num = int(input('Digite um número: '))
for c in range (1, num+1):
    if num % c == 0:
        cont += 1
        print('\033[1;32m', end=' ')
    else:
        print('\033[31m', end=' ')
    print(c, end=' ')
if cont <= 2:
    print('\n{}{}{}{} é um número primo? {}SIM{}'.format('\033[m', '\033[33m', num, '\033[m', '\033[1;32m', '\033[m'))
else:
    print('\n{}{}{}{} é um número primo? {}NÃO{}'.format('\033[m', '\033[33m', num, '\033[m', '\033[1;31m', '\033[m'))
