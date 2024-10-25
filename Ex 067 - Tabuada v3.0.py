#Faça um programa que mostre a tabuada de vários números, um de cada 
#vez, para cada valor digitado pelo usuário. O programa será 
#interrompido quando o número solicitado for negativo.
while True:
    num = int(input('Digite um número: '))
    if num < 0:
        break
    print('-'*30)
    print(f'{'\033[35m'}Tabuada do {num}{'\033[m'}:')
    print('-'*30)
    for c in range (1, 11):
        print(f'{'\033[35m'}{num}{'\033[m'} x {c:2} = {(num*c):2}')