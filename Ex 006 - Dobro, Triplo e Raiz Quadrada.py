#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e 
#raiz quadrada.
num = int(input('Digite um número inteiro: '))
d = num*2
t = num*3
r = pow(num, (1/2))
print('O dobro de {} = {}'.format(num, d))
print('O triplo de {} = {}'.format(num, t))
print('A raiz quadrada de {} = {:.1f}'.format(num, r))