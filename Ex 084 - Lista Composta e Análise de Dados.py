#Faça um programa que leia o nome e peso de várias pessoas, 
#guardando tudo em uma lista. No final, mostre:
# Quantas pessoa foram cadastradas
# Uma listagem com as pessoas mais pesadas
# Uma listagem com as pessoas mais leves
galera = []
dados = []
cont = maiorPeso = menorPeso = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    galera.append(dados[:])
    cont += 1
    dados.clear()
    opção = input('Deseja cadastrar mais pessoas? [S/N] ').upper()[0]
    if opção == 'N':
        break
print(f'Foram cadastradas {cont} pessoas') #Quantas pessoas foram cadastradas
for p in galera:
    if p[1] > maiorPeso:
        maiorPeso = menorPeso = p[1]
    if p[1] < menorPeso:
        menorPeso = p[1]
print(f'O maior peso foi {maiorPeso}Kg: ',end='') #Maior peso
for p in galera:
    if p[1] == maiorPeso:
        print(p[0],end=' ')
print()
print(f'O menor peso foi {menorPeso}Kg, peso de ',end='') #Menor peso   
for p in galera:
    if p[1] == menorPeso:
        print(p[0],end=' ')
    
    