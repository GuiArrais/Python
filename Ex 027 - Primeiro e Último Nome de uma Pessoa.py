#Faça um programa que leia o nome completo de uma pessoa, mostrando
#em seguida o primeiro e o último nome separadamente.
nome = input('Digite seu nome completo: ').strip()
nome = nome.split()
num = len(nome)
print('Primeiro:', nome[0])
print('Último:', nome[num-1])