#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas;
#O nome com todas as letras minúsculas;
#Quantas letras ao todo (sem considerar espaço);
#Quantas letras tem o primeiro nome.
nome = input('Digite seu nome completo: ')
print('Maiúsculo:',nome.upper())
print('Minúsculo:',nome.lower())
print('Quantas letras ao todo (sem considerar espaço):', len(nome)-nome.count(' '))
print('Quantas letras tem o primeiro nome:', nome.find(' '))