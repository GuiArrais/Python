#Crie um programa que leia uma frase qualquer e diga se ela é um 
#palíndromo, desconsiderando os espaços.
#APOS A SOPA
frase = input('Digite uma frase qualquer: ')
frase1 = frase.strip() #Tira os espaços inúteis
frase1 = frase1.upper() #Deixa tudo em maiúsculo
frase1 = ''.join(frase1.split()) #Retira os espaços do meio
frase2 = frase1[::-1]
if frase1 == frase2:
    print('{}É um palíndromo{}'.format('\033[32m', '\033[m'))
    print('{} = {}'.format(frase, frase[::-1]))
else:
    print('{}Não é um palíndromo{}'.format('\033[31m', '\033[m'))
    