#Crie um programa que leia nome, sexo e idade de várias pessoas, 
#guardando os dados de várias pessoas em um dicionário e todos os 
#dicionários em uma lista. No final, mostre: 
# Quantas pessoas foram cadastradas
# A média de idade do grupo
# Uma lista com todas as mulheres 
# Uma lista com todas as pessoas com idade acima da média
dados = {}
pessoas = []
mulheres = []
idadeMaior = []
mediaIdade = 0
CA = '\033[32m'
CF = '\033[m'
while True:
    dados['nome'] = str(input('Nome: '))
    while True:
        dados['sexo'] = str(input('Sexo [M/F]: ')).upper()
        if 'F' != dados['sexo'] != 'M':
            print('Desculpe, não entendi.')
        else:
            break
    dados['idade'] = int(input('Idade: '))
    if dados['sexo'] == 'F': #Lista só de mulheres
        mulheres.append(dados['nome'])
    pessoas.append(dados.copy()) #Copia a chave para a lista
    opção = str(input('Deseja cadastrar mais pessoas? [S/N] ')).upper()[0]
    if opção == 'N':
        break

print('-='*50)
print(f'Foram cadastradas {CA}{len(pessoas)}{CF} pessoas')
for c in pessoas: #Soma as idades para depois descobrir a média
    mediaIdade += c['idade']
print(f'A média de idade do grupo é {CA}{mediaIdade/len(pessoas)}{CF}',end=' anos \n')
print(f'As mulheres do grupo são: {CA}{mulheres}{CF}')
for c in pessoas: #Calcular pessoas com idade acima da média
    if c['idade'] >= (mediaIdade/len(pessoas)):
        idadeMaior.append(c['nome'])
print(f'As pessoas com idade superior a média de idade ({CA}{mediaIdade/len(pessoas)} anos{CF}) são {CA}{idadeMaior}{CF})')