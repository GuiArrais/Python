#Refaça o desafio 035 dos triângulos, acrescentando o recurso de 
#mostrar que tipo de triângulo será formado:
#-Equilátero: todos os lados iguais
#-Isósceles: dois lados iguais
#-Escaleno: todos os lados diferentes
r1 = int(input('Digite o comprimento da primeira reta: '))
r2 = int(input('Digite o comprimento da segunda reta: '))
r3 = int(input('Digite o comprimento da terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima {}PODEM{} formar um triângulo.'.format('\033[32m', '\033[m'))
    if r1 == r2 == r3:
        print('As retas formarão um triângulo {}equilátero.{}'.format('\033[36m', '\033[m'))
    elif (r1 == r2 and r1 != r3) or (r1 == r3 and r1 != r2) or (r2 == r3 and r2 != r1):
        print('As retas formarão um triângulo {}isósceles.{}'.format('\033[36m', '\033[m'))
    else:
        print('As retas formarão um triângulo {}escaleno.{}'.format('\033[36m', '\033[m'))
else:
    print('Os segmentos acima {}NÃO PODEM{} formar um triângulo.'.format('\033[31m', '\033[m'))