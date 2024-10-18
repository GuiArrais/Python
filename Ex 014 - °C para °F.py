#Escreva um programa que converta uma temperatura digitada em °C e 
#converta para °F.
c = float(input('Digite a temperatura em °C: '))
f = (c*1.8) + 32
print('{}°C equivale a {:.1f}°F'.format(c, f))
#C = (F - 32) / 1.8