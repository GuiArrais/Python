#Escreva um programa que leia um número inteiro qualquer e peça para 
#o usuário escolher qual será a base de conversão:
#-1 para binário
#-2 para octal
#-3 para hexadecimal
from time import sleep
num = int(input('\nDigite um número: ')) #Escolher número
print('Escolha qual será a base de conversão:') #Binário, Octal ou Hexadecimal
opção = int(input('{}[1] Binário{} \n{}[2] Octal{} \n{}[3] Hexadecimal{}\n'.format('\033[33m', '\033[m', '\033[34m', '\033[m', '\033[35m', '\033[m')))
#Aviso de opção inválida
if opção < 1 or opção > 3:
    sleep(3)
    print('Opção inválida. Tente novamente.')
    opção = int(input('{}[1] Binário{} \n{}[2] Octal{} \n{}[3] Hexadecimal{}\n'.format('\033[33m', '\033[m', '\033[34m', '\033[m', '\033[35m', '\033[m')))
if opção == 1: #BINARIO
    binario = bin(num)[2:]
    print('O número {}{}{} em binário = {}{}{}'.format('\033[33m', num, '\033[m', '\033[33m', binario, '\033[m'))
elif opção == 2: #OCTAL
    octal = oct(num)[2:]
    print('O número {}{}{} em octal = {}{}{}'.format('\033[34m', num, '\033[m', '\033[34m', octal, '\033[m'))
elif opção == 3: #HEXADECIMAL
    hexadecimal = hex(num)[2:]
    print('O número {}{}{} em hexadecimal = {}{}{}'.format('\033[35m', num, '\033[m', '\033[35m', hexadecimal.upper(), '\033[m'))
    

