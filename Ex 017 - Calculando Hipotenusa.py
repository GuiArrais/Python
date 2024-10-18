#Faça um programa que leia o comprimento do cateto oposto e do 
#cateto adjacente de um triângulo retângulo, calcule e mostre o 
#comprimento da hipotenusa.

#from math import sqrt
#from math import pow
#h = sqrt((pow(co, 2))+(pow(ca, 2)))
from math import hypot
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
h = hypot(co, ca)
print('O valor da hipotenusa = {:.2f}'.format(h))
 