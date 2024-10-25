#Faça um programa que jogue par ou ímpar com o computador. O jogo só 
#será interrompido quando o jogador perder, mostrando o total de 
#vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
from time import sleep
cont = 0
while True:
    computer = randint(0, 10)
    ip = input('Escolha: Par ou Ímpar? ').upper().strip()

    while ip != 'PAR' and ip != 'IMPAR': #Caso a pessoa não escolha nem par, nem ímpar
        print(f'{'\033[31m'}Opção inválida.{'\033[m'} Tente novamente...')
        sleep(1)
        ip = input('Escolha: Par ou Ímpar? ').upper().strip()

    if ip == 'PAR':
        num = int(input('Escolha um número: '))
        if (num+computer) % 2 == 0:
            print(f'{'\033[34m'}Você{'\033[m'}         x       {'\033[7m'}Computador{'\033[m'}')
            sleep(1)
            print(f'{'\033[1m'}Par{'\033[m'}          x       {'\033[4m'}Ímpar{'\033[m'}')
            sleep(1)
            print(f'{num}            x       {computer}')
            sleep(1)
            print(f'{'\033[32m'}Você ganhou.{'\033[m'} {num} + {computer} = {'\033[33m'}{num+computer}{'\033[m'}')
            cont += 1
        else:
            print(f'{'\033[34m'}Você{'\033[m'}         x       {'\033[7m'}Computador{'\033[m'}')
            sleep(1)
            print(f'{'\033[1m'}Par{'\033[m'}          x       {'\033[4m'}Ímpar{'\033[m'}')
            sleep(1)
            print(f'{num}            x       {computer}       = {'\033[33m'}{num+computer}{'\033[m'}')
            sleep(1)
            print(f'{'\033[31m'}Computador ganhou.{'\033[m'} {num} + {computer} = {'\033[33m'}{num+computer}{'\033[m'}')
            break
######################################################################################################
    if ip == 'IMPAR':
        num = int(input('Escolha um número: '))
        if (num+computer) % 2 == 1:
            print(f'{'\033[34m'}Você{'\033[m'}         x       {'\033[7m'}Computador{'\033[m'}')
            sleep(1)
            print(f'{'\033[4m'}Ímpar{'\033[m'}        x       {'\033[1m'}Par{'\033[m'}')
            sleep(1)
            print(f'{num}            x       {computer}')
            sleep(1)
            print(f'{'\033[32m'}Você ganhou.{'\033[m'} {num} + {computer} = {'\033[33m'}{num+computer}{'\033[m'}')
            cont += 1
        else:
            print(f'{'\033[34m'}Você{'\033[m'}         x       {'\033[7m'}Computador{'\033[m'}')
            sleep(1)
            print(f'{'\033[4m'}Ímpar{'\033[m'}        x       {'\033[1m'}Par{'\033[m'}')
            sleep(1)
            print(f'{num}            x       {computer}')
            sleep(1)
            print(f'{'\033[31m'}Computador ganhou.{'\033[m'} {num} + {computer} = {'\033[33m'}{num+computer}{'\033[m'}')
            break
print(f'Você ganhou {'\033[32m'}{cont}{'\033[m'} vezes consecutivas')
    