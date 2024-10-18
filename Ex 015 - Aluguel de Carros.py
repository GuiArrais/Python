#Escreva um programa que pergunte a quantidade de Km percorridos por
#um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
#Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia
#e R$0,15 por Km rodado.
km = float(input('Digite a quantidade de Kms percorridos: '))
dias = int(input('Digite quantos dias o carro foi alugado: '))
preço = dias*60 + km*0.15
print('O carro que foi alugado por {} dias e rodou {} Kms custou R${:.2f}'.format(dias, km, preço))