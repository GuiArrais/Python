#Crie um programa que crie uma matriz de dimensão 3x3 e preencha com 
#valores lidos pelo teclado.
#No final, mostre a matriz na tela, com a formatação correta.
matriz = [[], [], []]
for c in range(0,3):
    for l in range(0,3):
        matriz[c].append(int(input(f'Digite o valor [{c}][{l}]: ')))
print('-'*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()
