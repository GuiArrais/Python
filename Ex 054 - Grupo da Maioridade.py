#Crie um programa que leia o ano de nascimento de sete pessoas. No 
#final, mostre quantas pessoas ainda não atingiram a maioridade e 
#quantas já são maiores.
from datetime import date
contMaior = 0
contMenor = 0
for c in range (0, 7):
    c = int(input('Digite a data de nascimento da {}ª pessoa: '.format(c+1)))
    if (date.today().year - c) >= 18:
        contMaior += 1
    if (date.today().year - c) < 18:
        contMenor += 1
print('Pessoas maiores de idade: {}{}{}'.format('\033[32m', contMaior, '\033[m'))
print('Pessoas que ainda não atingiram a maturidade: {}{}{}'.format('\033[31m', contMenor, '\033[m'))