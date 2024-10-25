#Melhore o jogo do desafio 028 onde o computador vai "pensar" em um 
#número entre 0 e 10. Só que agora o jogador vai tentar advinhar 
#até acertar, mostrando no final quantos palpites foram necessários 
#para vencer.
from random import randint
computer = randint(0, 10)
cont = 0
print('Estou pensando em um número entre 0 e 10. \nTente advinhar... ')
num = int(input('Número: '))
while num != computer:
    if num < computer:
        print('{}Mais...{} Tente novamente.'.format('\033[31m', '\033[m'))
    else:
        print('{}Menos...{} Tente novamente.'.format('\033[31m', '\033[m'))
    num = int(input('Número: '))
    cont = cont+1
print('{}Você acertou, parabéns{}'.format('\033[32m', '\033[m'))
print('Foram necessários {}{}{} palpites até você acertar.'.format('\033[33m', cont, '\033[m'))