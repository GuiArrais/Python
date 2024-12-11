#Aprimore o desafio 93 para que ele funcione com vários jogadores, 
#incluindo um sistema de visualização de detalhes do aproveitamento 
#de cada jogador.
#Crie um programa que gerencie o aproveitamento de um jogador de 
#futebol. O programa vai ler o nome do jogador e quantas partidas 
#ele jogou. Depois vai ler a quantidade de gols feitos em cada 
#partida. No final, tudo isso será guardado em um dicionário, 
#incluindo o total de gols feitos durante o campeonato.
dados = {}
jogadores = []
gol = 0
while True:
    dados['nome'] = str(input('Nome: '))
    dados['partidas'] = int(input('Partidas jogadas: '))
    gols = []
    totalGols = 0
    for g in range(0, dados['partidas']):
        gol = int(input(f'Quantos gols na partida {g+1}: '))
        gols.append(gol)
        totalGols += gol #Calcula o total de gols de cada jogador
    dados['gols'] = (gols[:])
    dados['totalGols'] = totalGols
    jogadores.append(dados.copy())
    opção = str(input('Deseja adicionar mais jogadores? [S/N] ')).upper()[0]
    while True: #Caso a resposta seja diferente de S ou N
        if 'S' != opção != 'N':
            print('Desculpe não entendi. Responda com S ou N.')
        else:
            break
    if opção == 'N':
        break
    
print(jogadores)
print('-='*30)
print(f'{'JOGADORES':^60}')
print('-='*30)
print(f'{'Nome':^10}',end='')
print(f'{'Partidas':^10}',end='')
print(f'{'Gols':^20}',end='')
print(f'{'Total de Gols':^15}')
for c in jogadores:
    print(f'{c['nome']:^10}',end='')
    print(f'{c['partidas']:^10}',end='')
    print(f'{str(c['gols']):^20}',end='')
    print(f'{c['totalGols']:^15}')