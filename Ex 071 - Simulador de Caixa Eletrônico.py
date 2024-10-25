#Crie um programa que simule o funcionamento de um caixa eletrônico. 
#No início, pergunte ao usuário qual será o valor a ser sacado 
#(número inteiro) e o programa vai informar quantas células de cada 
#valor serão entregues.
#OBS: Considere que o caixa possui cédulas de R$50, R$20 ,R$10 e R$1.
cont50 = cont20 = cont10 = cont1 = 0
print('~'*30)
print('CAIXA ELETRÔNICO'.center(30))
print('~'*30)
print('Qual será o valor a ser sacado?')
valor = int(input('R$'))
while True:
    if valor >= 50:
        cont50 = valor//50
        valor = valor - (cont50 * 50)
    if valor >= 20:
        cont20 = valor//20
        valor = valor - (cont20 * 20)
    if valor >= 10:
        cont10 = valor//10
        valor = valor - (cont10 * 10)
    if valor >= 1:
        cont1 = valor//1
        valor = valor - (cont1 * 1)
    if valor == 0:
        break
print(f'Cédulas de R${'\033[35m'}50.00{'\033[m'}: ',end='')
print(f'\033[32m{cont50}\033[m' if cont50 != 0 else f'\033[31m{cont50}\033[m') #50
print(f'Cédulas de R${'\033[35m'}20.00{'\033[m'}: ',end='')
print(f'\033[32m{cont20}\033[m' if cont20 != 0 else f'\033[31m{cont20}\033[m') #20
print(f'Cédulas de R${'\033[35m'}10.00{'\033[m'}: ',end='')
print(f'\033[32m{cont10}\033[m' if cont10 != 0 else f'\033[31m{cont10}\033[m') #10
print(f'Cédulas de R${'\033[35m'} 1.00{'\033[m'}: ',end='')
print(f'\033[32m{cont1}\033[m' if cont1 != 0 else f'\033[31m{cont1}\033[m') #1

'''valor = int(input('Qual valor você quer sacar? \nR$'))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Cédulas de R${'\033[35m'}{céd:.2f}{'\033[m'}: {totcéd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('-'*30)'''
