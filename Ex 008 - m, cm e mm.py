#Escreva um programa que leia um valor em metros e o exiba 
#convertido em centímetros e em milímetros.
metros = float(input('Digite um valor em metros: '))
cent = metros * 100
mili = metros * 1000
print('{} metro(s) = {:.0f} centímetro(s) ou {:.0f} milímetro(s)'.format(metros, cent, mili))