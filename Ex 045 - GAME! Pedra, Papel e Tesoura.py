#Crie um programa que faça o computador jogar Jokenpô com você.
from random import choice
from time import sleep
print('Escolha um:')
opção = int(input('{}[1] Pedra{} \n{}[2] Papel{} \n{}[3] Tesoura{} \n'.format('\033[33m', '\033[m', '\033[34m', '\033[m', '\033[35m', '\033[m')))
lista = ['Pedra', 'Papel', 'Tesoura']
pc = choice(lista)
sleep(1)
print('\nJo')
sleep(1)
print('\nKen')
sleep(1)
print('\nPô')
sleep(1)
print('Você     x     PC')
#PEDRA
if opção == 1 and pc == 'Pedra':
    print('{}Pedra{}          {}Pedra{}'.format('\033[33m', '\033[m', '\033[33m', '\033[m'))
    print('{}EMPATE{}'.format('\033[33m', '\033[m'))
elif opção == 1 and pc == 'Papel':
    print('{}Pedra{}          {}Papel{}'.format('\033[33m', '\033[m', '\033[34m', '\033[m'))
    print('{}PC GANHOU{}'.format('\033[31m', '\033[m'))
elif opção == 1 and pc == 'Tesoura':
    print('{}Pedra{}          {}Tesoura{}'.format('\033[33m', '\033[m', '\033[35m', '\033[m'))
    print('{}VOCÊ GANHOU{}'.format('\033[32m', '\033[m'))
#PAPEL
elif opção == 2 and pc == 'Pedra':
    print('{}Papel{}          {}Pedra{}'.format('\033[34m', '\033[m', '\033[33m', '\033[m'))
    print('{}VOCÊ GANHOU{}'.format('\033[32m', '\033[m'))
elif opção == 2 and pc == 'Papel':
    print('{}Papel{}          {}Papel{}'.format('\033[34m', '\033[m', '\033[34m', '\033[m'))
    print('{}EMPATE{}'.format('\033[33m', '\033[m'))
elif opção == 2 and pc == 'Tesoura':
    print('{}Papel{}          {}Tesoura{}'.format('\033[34m', '\033[m', '\033[35m', '\033[m'))
    print('{}PC GANHOU{}'.format('\033[31m', '\033[m'))
#TESOURA
if opção == 3 and pc == 'Pedra':
    print('{}Tesoura{}        {}Pedra{}'.format('\033[35m', '\033[m', '\033[33m', '\033[m'))
    print('{}PC GANHOU{}'.format('\033[31m', '\033[m'))
elif opção == 3 and pc == 'Papel':
    print('{}Tesoura{}        {}Papel{}'.format('\033[35m', '\033[m', '\033[34m', '\033[m'))
    print('{}VOCÊ GANHOU{}'.format('\033[32m', '\033[m'))
elif opção == 3 and pc == 'Tesoura':
    print('{}Tesoura{}        {}Tesoura{}'.format('\033[35m', '\033[m', '\033[35m', '\033[m'))
    print('{}EMPATE{}'.format('\033[33m', '\033[m'))