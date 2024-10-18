#Crie um programa que leia um número inteiro e mostre na tela se ele 
#é par ou ímpar.
num = int(input('Digite um número: '))
if num%2 == 0:
    print('{} é par.'.format(num))
else:
    print('{} é ímpar.'.format(num))
