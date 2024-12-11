#Crie um programa que leia nome e duas notas de vários alunos e 
#guarde tudo em uma lista composta. No final, mostre um boletim 
#contendo a média de cada um e permita que o usuário possa mostrar 
#as notas de cada aluno individualmente.
aluno = []
while True:
    dados = []
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    dados.append((dados[1] + dados[2]) / 2) #Cálculo média
    aluno.append(dados[:])
    dados.clear()
    opção = input('Deseja adicionar mais alunos? [S/N] ').upper()[0]
    if opção == 'N':
        break

print('-'*30)
print(f'{"BOLETIM":^30}')
print('-'*30)
print(f'{'\033[36m'}{'N°':5}{'\033[m'}',end='')
print(f'{'\033[34m'}{'Nome':7}{'\033[m'}',end='')
print(f'{'\033[33m'}{'Média'}{'\033[m'}')
for c, i in enumerate(aluno):
    print(f'{c+1:<5}{i[0]:<15}',end='')
    if i[3] >= 6:
        print(f'{'\033[32m'}{i[3]:.1f}{'\033[m'}')
    else:
        print(f'{'\033[31m'}{i[3]:.1f}{'\033[m'}')
while True:
    opção = int(input('Mostrar notas de qual aluno? (0 interrompe): '))
    if opção == 0:
        break
    else:
        for c, i in enumerate(aluno):
            if c == (opção-1):
                print(f'Aluno: {aluno[c][0]}')
                print(f'Nota 1: {aluno[c][1]}')
                print(f'Nota 2: {aluno[c][2]}')
        print('-'*40)
