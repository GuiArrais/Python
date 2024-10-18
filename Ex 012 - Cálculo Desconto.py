#Faça um algoritmo que leia o preço de um produto e mostre seu novo
#preço com 5% de desconto.
preco = float(input('Qual o valor do produto?\nR$'))
print('Preço: R${:.2f}\nDesconto: R${:.2f}'.format(preco, (preco*0.05)))
precoFinal = preco-(preco*0.05)
print('Preço final com 5% de desconto: R${:.2f}'.format(precoFinal))