#Escreva um programa para aprovar um empréstimo bancário para a 
#compra de uma casa. O programa vai perguntar o valor da casa, o 
#salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode 
#exceder 30% do salário ou então o empréstimo será negado.
from time import sleep
print('{}Empréstimo Bancário{}'.format('\033[1;35;43m', '\033[m'))
valorCasa = float(input('Qual o valor da casa:\nR$'))
salarioComprador = float(input('Qual o salário do comprador:\nR$'))
pagamentoAnos = int(input('Em quantos anos ele vai pagar?\n'))
prestaçãoMensal = valorCasa / (pagamentoAnos * 12) #Calcula
print('{}PROCESSANDO...{}\n'.format('\033[7m', '\033[m'))
sleep(3)
#RESUMO
print('Valor da casa: R${}{:.2f}{}'.format('\033[1;31m', valorCasa, '\033[m'))
print('Quantidade de parcelas: {}{}{} ({}{}{} anos)'.format('\033[1;31m', (pagamentoAnos*12), '\033[m', '\033[1;31m', pagamentoAnos, '\033[m'))
print('Valor das parcelas: {}R${:.2f}{}'.format('\033[1;31m', prestaçãoMensal, '\033[m'))
print('Salário do comprador: R${}{}{}'.format('\033[1;31m', salarioComprador, '\033[m'))
if prestaçãoMensal > (salarioComprador * 0.3):
    print('Emprestimo {}NEGADO{}.'.format('\033[4;41m', '\033[m'))
    print('O valor da prestação mensal ultrapassa {}30%{} do salário do comprador'.format('\033[33m', '\033[m'))
else:
    print('Empréstimo {}APROVADO{}.'.format('\033[4;42m', '\033[m'))
