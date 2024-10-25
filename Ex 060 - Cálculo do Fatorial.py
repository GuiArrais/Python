#Faça um programa que leia um número qualquer e mostre na tela o seu 
#fatorial.
from math import factorial
num = int(input('Digite um número para calcular seu fatorial: '))
f = factorial(num)
print('{}{}!{} >>> '.format('\033[35m', num, '\033[m'), end='')
while num > 0:
    print(num,end='')
    print(' x ' if num > 1 else ' = ', end='')
    num = num-1
print('{}{}{}'.format('\033[35m', f, '\033[m'))