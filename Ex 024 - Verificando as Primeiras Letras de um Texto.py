#Crie um programa que leia o nome de uma cidade e diga se ela 
#começa ou não com o nome "SANTO".
cidade = input('Digite o nome da cidade:')
#cidade = cidade.upper()
#cidade = cidade.split()
#cidade = cidade[0]
#print('SANTO' in cidade)
print(cidade[:5].upper() == 'SANTO')

