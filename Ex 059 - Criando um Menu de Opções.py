#Crie um programa que leia dois valores e mostre um menu na tela:
#[1] Somar
#[2] Multiplicar
#[3] Maior
#[4] Novos números
#[5] Sair do programa
#Seu programa deverá realizar a operação solicitada no programa
from time import sleep
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opção = 6
while opção != 5:
    sleep(1)
    print('-=-'*20)
    print('\nValor 1: {}{}{} \nValor 2: {}{}{}'.format('\033[36m', n1, '\033[m', '\033[36m', n2, '\033[m'))
    print('{}Escolha uma opção:{}'.format('\033[4m', '\033[m'))
    sleep(1)
    opção = int(input('\033[32m[1] Somar\033[m \n\033[33m[2] Multiplicar\033[m \n\033[34m[3] Maior\033[m \n\033[35m[4] Novos números\033[m \n\033[31m[5] Sair do programa\033[m\n'))
    if opção == 1:
        print('{} + {} = {}'.format(n1, n2, (n1+n2)))
    elif opção == 2:
        print('{} x {} = {}'.format(n1, n2, (n1*n2)))
    elif opção == 3:
        if n1 > n2:
            print('{} é maior que {}'.format(n1, n2))
        elif n2 > n1:
            print('{} é maior que {}'.format(n2, n1))
        else:
            print('{} e {} são iguais'.format(n2, n1))
    elif opção == 4:
        print('Escolha novos números...')
        novo1 = int(input('Digite o primeiro valor: '))
        n1 = novo1
        novo2 = int(input('Digite o segundo valor: '))
        n2 = novo2
    elif opção < 1 or opção > 5:
        print('{}Opção inválida.{} Tente novamente.'.format('\033[31m', '\033[m'))
        sleep(1)
print('{}Saindo do programa...{}'.format('\033[7m', '\033[m'))
sleep(3)
    
        