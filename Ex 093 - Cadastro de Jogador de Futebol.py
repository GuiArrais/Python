#Crie um programa que gerencie o aproveitamento de um jogador de 
#futebol. O programa vai ler o nome do jogador e quantas partidas 
#ele jogou. Depois vai ler a quantidade de gols feitos em cada 
#partida. No final, tudo isso será guardado em um dicionário, 
#incluindo o total de gols feitos durante o campeonato.
jogador = {}
gols = []
totalGols = 0
jogador['nome'] = str(input('Nome do jogador: '))
jogador['partidas'] = int(input('Quantas partidas ele jogou: '))
for c in range(0, jogador['partidas']):
    gols.append(int(input(f'Quantos gols na partida {c+1}: ')))
jogador['gols'] = gols[:]
jogador['totalGols'] = sum(jogador['gols'].copy())
print('-'*30)
print(f'Nome: {jogador['nome']}')
print(f'Quantidade de jogos: {jogador['partidas']}')
for c in range(0, len(gols)):
    print(f'    =>Partida {c+1}: {gols[c]}',end=' gols \n')
print(f'Total de gols: {jogador['totalGols']}')