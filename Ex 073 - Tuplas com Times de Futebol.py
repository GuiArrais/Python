#Crie uma tupla com os 20 primeiros colocados da Tabela do 
#Campeonato Brasileiro de Futebol, na ordem de colocação. Depois 
#mostre:
#Apenas os 5 primeiros colocados;
#Os últimos 4 colocados da tabela;
#Uma lista com os times em ordem alfabética;
#Em que posição na tabela está o time da Chapecoense.
posição = 0
tabela = ('Botafogo', 'Palmeiras', 'Fortaleza', 'Flamengo', 
          'Internacional', 'São Paulo', 'Bahia', 'Cruzeiro', 
          'Vasco', 'Atlético Mineiro', 'Grêmio', 'Vitória', 
          'Corinthias', 'Fluminense', 'Criciúma', 'Bragantino', 
          'Atlético Paranaense', 'Juventude', 'Cuiabá', 'Atlético-GO')
print('5 primeiros colocados')
print(tabela[0:5])
print('-'*70)
print('4 últimos colocados')
print(tabela[-4:])
print('-'*70)
print('Ordem alfabética dos colocados')
ordem = sorted(tabela)
for c in ordem:
    print(c)
print('-'*70)
print('Em que posição o time do Cruzeiro ficou?')
for c in tabela:
    if c == 'Cruzeiro':
        posição = tabela.index(c)+1
print(f'O time do Cruzeiro ficou na {posição}ª posição.')



