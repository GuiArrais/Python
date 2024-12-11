#Faça um programa que ajude um jogador da MEGA SENA a criar palpites. 
#O programa vai perguntar quantos jogos serão gerados e vai sortear 
#6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma 
#lista composta.
from random import randint
from time import sleep
total = list()
dados = []
quant = int(input('Quantos jogos você quer gerar: '))
for c in range(0,quant): #Quantidade de jogos
    for n in range(0,6): #Quantidade de números sorteados (6)
        while len(dados) < 6:
            num = int(randint(1,60))
            if num not in dados: #Se o número já existir em dados, sorteia outro número
                dados.append(num)
    total.append(dados[:])
    dados.clear()
print('-='*3, f'SORTEANDO {quant} JOGOS', '=-'*3)
cont = 1
for c in total:
    print(f'Jogo {cont}: {c}')
    sleep(1)
    cont += 1
print('<'*10, f'BOA SORTE', '>'*10)