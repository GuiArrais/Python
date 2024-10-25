#Crie um programa que leia vários números inteiros pelo teclado. No 
#final da execução, mostre a média entre todos os valores e qual foi 
#o maior e o menor valores lidos. O programa deve perguntar ao 
#usuário se ele quer ou não continuar a digitar valores.
cont = 1
soma = 0
opção = 'S'
num = int(input('Digite um número: '))
maior = num
menor = num
soma += num
opção = input('Quer digitar mais valores? (S/N) ')
while opção in "Ss":
    num = int(input('Digite um número: '))
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    soma += num
    cont += 1
    opção = input('Quer digitar mais valores? (S/N) ')
print('Média: {}{}{}'.format('\033[1;34m', (soma/cont), '\033[m'))
print('Maior número: {}{}{} \nMenor número: {}{}{}'.format('\033[34m', maior, '\033[m', '\033[34m', menor, '\033[m'))

