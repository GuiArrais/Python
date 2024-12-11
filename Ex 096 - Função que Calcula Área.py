#Faça um programa que tenha uma função chamada área(), que receba 
#as dimensões de um terreno retangular (largura e comprimento) e 
#mostre a área do terreno.
def área(l, c):
    a = l*c
    print(f'A área de um terreno {l}x{c} é de {a} m^2')


#Programa Principal
l = float(input('Largura (M): '))
c = float(input('Comprimento (M): '))
área(l, c)