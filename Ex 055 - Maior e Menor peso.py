#Faça um programa que leia o peso de cinco pessoas. No final, mostre 
#qual foi o maior e o menor peso lidos.
num = float(input('Digite o peso da 1ª pessoa: '))
maiorPeso = num
menorPeso = num
for c in range (1, 5):
    num = float(input('Digite o peso da {}ª pessoa: '.format(c+1)))
    if num > maiorPeso:
        maiorPeso = num
    if num < menorPeso:
        menorPeso = num
print('Maior peso: {:.1f} kg'.format(maiorPeso))
print('Menor peso: {:.1f} kg'.format(menorPeso))