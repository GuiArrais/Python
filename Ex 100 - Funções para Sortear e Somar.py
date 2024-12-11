#Faça um programa que tenha uma lista chamada números e duas funções 
#chamadas sorteia() e somaPar(). A primeira função vai sortear 5 
#números e vai colocá-los dentro da lista e a segunda função vai 
#mostrar a soma entre todos os valores sorteados pela função 
#anterior.
from random import randint
from time import sleep
números = []
def sorteia():
    for c in range(0,5):
        num = randint(0,100)
        números.append(num)
        
        
def somaPar():
    soma = 0
    for c in números:
        if c % 2 == 0:
            soma += c
    for s in sorted(números):
        sleep(0.5)
        if s % 2 == 0:
            print(f'{'\033[32m'}{s}{'\033[m'}',end=' ',flush=True)
        else:
            print(s,end=' ',flush=True)
    print(f'\nA soma dos números pares = {soma}')
    
        
print('Sorteando 5 valores...')
sorteia()
somaPar()