#Escreva um programa que leia dois números inteiros e compare-os, 
#mostrando na tela uma mensagem:
#-O primeiro valor é maior
#-O segundo valor é maior
#-Não existe valor maior, os dois são iguais
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print('O primeiro valor é maior. {}{}{} > {}{}{}'.format('\033[32m', n1, '\033[m', '\033[31m', n2, '\033[m'))
elif n2 > n1:
    print('O segundo valor é maior. {}{}{} < {}{}{}'.format('\033[31m', n1, '\033[m', '\033[32m', n2, '\033[m'))
else:
    print('Não existe valor maior, os dois são iguais. {}{}{} == {}{}{}'.format('\033[36m', n1, '\033[m', '\033[36  m', n2, '\033[m'))