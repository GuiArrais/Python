#Crie um programa que leia vários números inteiros pelo teclado. O 
#programa só vai parar quando o usuário digitar o valor 999, que é a 
#condição de parada. No final, mostre quantos números foram 
#digitados e qual foi a soma entre eles (desconsiderando o flag).
cont = 0
soma = 0
num = 0
while num != 999:
    num = int(input('Digite um número. [999 para papar]: '))
    if num != 999:
        soma += num
        cont += 1
print('Você digitou {}{}{} números que somados dão um total de {}{}{}'.format('\033[2;32m', cont, '\033[m', '\033[2;32m', soma, '\033[m'))