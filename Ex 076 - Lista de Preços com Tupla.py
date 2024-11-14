#Crie um programa que tenha uma tupla única com nomes de produtos e 
#seus respectivos preços, na sequência.
#No final, mostre uma listagem de preços, organizando os dados em 
#forma tabular.
lista = ('Lápis', 1.75, 
         'Borracha', 2, 
         'Caderno', 15.9,
         'Estojo', 25, 
         'Transferidor', 4.2, 
         'Compasso', 9.99,
         'Mochila', 120.32,
         'Canetas', 22.3,
         'Livro', 34.9)
print('-'*30)
print(f'{'LISTA DE PRODUTOS':^30}')
print('-'*30)
for c in range (0, len(lista)):
    if c % 2 == 0:
        print(f'{lista[c]:.<20}',end='')
    else:
        print(f'R${lista[c]:>7.2f}')
print('-'*30)