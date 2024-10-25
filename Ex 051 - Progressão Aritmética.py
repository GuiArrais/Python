#Desenvolva um programa que leia o primeiro termo e a razão de uma 
#PA. No final, mostre os 10 primeiros termos dessa progressão.
n = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão dessa PA: '))
for c in range (0, 10):
    print(n, end=(' → '))
    n = n+r
print('Acabou')