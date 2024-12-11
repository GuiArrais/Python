#Crie um programa onde o usuário possa digitar sete valores 
#numéricos e cadastre-os em uma lista única que mantenha separados 
#os valores pares e ímpares. No final, mostre os valores pares e 
#ímpares em ordem crescente.
lista = [[], []]
for c in range(0,7):
    dados = int(input(f'Digite o {c+1}° valor: '))
    if dados % 2 == 0:
        lista[0].append(dados)
    else:
        lista[1].append(dados)
print(f'Pares: {sorted(lista[0])}')
print(f'Ímpares: {sorted(lista[1])}')