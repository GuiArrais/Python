#Crie um programa onde 4 jogadores joguem um dado e tenham 
#resultados aleatórios. Guarde esses resultados em um dicionário. 
#No final, coloque esse dicionário em ordem, sabendo que o vencedor 
#tirou o maior número do dado.
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador 1':randint(1,6),
        'jogador 2':randint(1,6),
        'jogador 3':randint(1,6),
        'jogador 4':randint(1,6)}
ranking = []
print('Valores sorteados')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado')  
    sleep(1)
print('-'*30)
print('== RANKING DOS JOGADORES ==')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse = True) #Se for item 0 ele vai mostrar a ordem a partir de chave, se for 1 é a partir de valor
for i, v in enumerate(ranking):
    print(f' {i+1}° lugar: {v[0]} com {v[1]}')
    sleep(1)