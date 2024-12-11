#Faça um programa que leia nome e média de um aluno, guardando 
#também a situação em um dicionário. No final, mostre o conteúdo da 
#estrutura na tela.
aluno = {}
aluno['nome'] = input('Digite o nome do aluno: ')
aluno['média'] = float(input('Digite a média do aluno: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print(aluno)
print('-'*30)
for k, v in aluno.items():
    print(f'{k}: {v}')