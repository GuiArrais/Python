#Crie um programa onde o usuário possa digitar 
#vários valores numéricos e cadastre-os em uma 
#lista. Caso o número já exista lá dentro, ele não 
#será adicionado. No final, serão exibidos todos 
#os valores únicos digitados, em ordem crescente.
lista = []
while True:
    num = (int(input('Digite um valor: ')))
    if num in lista: #Se o número já pertence a lista ele não será adicionado
        print(f'O número {'\033[4m'}já pertence{'\033[m'} à lista e {'\033[4m'}NÃO{'\033[m'} será adicionado.')
    else:
        lista.append(num)
    opção = input('Deseja continuar? [S/N]\n').upper()[0]
    if opção == 'N':
        break
    if 'N' != opção != 'S':
        print('Desculpe, não entendi.')
        opção = input('Deseja continuar? [S/N]\n').upper()[0]
        if opção == 'N':
            break
        if 'N' != opção != 'S':
            print('Desculpe, não entendi.')
    
print('-'*30)
print(sorted(lista))