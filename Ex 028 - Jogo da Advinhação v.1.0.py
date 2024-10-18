#Escreva um programa que faça o computador "pensar" em um número 
#inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi
#o número escolhido pelo computador.
#programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep
import colorama
computador = randint(0, 5) #Computador escolhe um número
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-'*20)
jogador = int(input('Eu pensei no número: ')) #Jogador tenta advinhar
print('\033[7mPROCESSANDO...\033[m')
sleep(3)
if jogador == computador:
    print('\033[32mParabéns.\033[m Você conseguiu me vencer.')
else:
    print('\033[31mVocê perdeu!\033[m Eu pensei no número \033[1;32m{}\033[m e não no número \033[1;31m{}\033[m\n\n'.format(computador, jogador))


