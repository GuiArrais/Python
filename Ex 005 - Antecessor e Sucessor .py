#Faça um programa que leia um número inteiro e mostre na tela o seu 
#sucessor e o seu antecessor.
num = int(input('Digite um número inteiro: '))
print('Seu antecessor é {}'.format(num-1))
print('Seu sucessor é {}'.format(num+1))
print('{} <<< {} >>> {}'.format((num-1), num, (num+1)))