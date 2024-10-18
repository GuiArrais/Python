#Faça um programa que leia a largura e a altura de uma parede em 
#metros, calcule a sua área e a quantidade de tinta necessária para 
#pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m^2.
largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura*altura
print('Sua parede tem a dimensão de {}x{} e sua área é de {:.1f}m^2.'.format(largura, altura, area))
tinta = area/2
print('Para pitar essa parede, será necessário {:.1f} litros de tinta'.format(tinta))