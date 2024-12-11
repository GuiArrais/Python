#Aprimore o desafio anterior, mostrando no final:
# A soma de todos os valores pares digitados;
# A soma dos valores da terceira coluna;
# O maior valor da segunda linha.
matriz = [[],[],[]]
somaPar = somaC3 = maiorL2 = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l].append(int(input(f'Digite o valor [{l}][{c}]: ')))
        if matriz[l][c] % 2 == 0:
            somaPar += matriz[l][c]
        if c == 2:
            somaC3 += matriz[l][2]
        if l == 1:
            maiorL2 = matriz[1][0]
            if matriz[1][c] > maiorL2:
                maiorL2 = matriz[1][c]
print('-='*30)                
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()
print('-='*30)                
print(f'A soma de todos os valores {'\033[4m'}pares{'\033[m'} é {'\033[32m'}{somaPar}{'\033[m'}')
print(f'A soma dos valores da {'\033[4m'}terceira coluna{'\033[m'} é {'\033[32m'}{somaC3}{'\033[m'}')
print(f'O {'\033[4m'}maior valor{'\033[m'} da segunda linha é {'\033[32m'}{maiorL2}{'\033[m'}')