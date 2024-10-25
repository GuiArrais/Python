#Crie um programa que leia o nome e o preço de vários produtos. O 
#programa deverá perguntar se o usuário vai continuar. No final, 
#mostre: 
#Qual é o total gasto na compra;
#Quantos produtos custam mais de R$1000,00;
#Qual é o nome do produto mais barato.
cont = total = caro = 0
baratoP = float('inf')
while True:
    cont += 1
    nome = input(f'Digite o {'\033[34m'}{cont}°{'\033[m'} produto: ').strip()
    preço = float(input(f'Digite o {'\033[4m'}preço{'\033[m'} do produto: R$'))
    if preço < baratoP:
        baratoP = preço
        baratoN = nome
    total += preço
    if preço >= 1000:
        caro += 1
    opção = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if opção == 'N':
        break
    if opção != 'S':
        print('Comando inválido. Digite novamente')
        opção = input('Deseja continuar? [S/N] ').strip().upper()[0]
print('-'*30)
print(f'Total gasto na compra: R${'\033[35m'}{total:.2f}{'\033[m'}')
print(f'Quantos produtos custam mais de R$1000,00: {'\033[35m'}{caro}{'\033[m'}')
print(f'Produto mais barato: {'\033[35m'}{baratoN}{'\033[m'} e custa R${'\033[35m'}{baratoP:.2f}{'\033[m'}')