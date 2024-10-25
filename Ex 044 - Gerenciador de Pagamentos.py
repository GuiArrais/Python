#Elabore um programa que calcule um valor a ser pago por um produto, 
#considerando o seu preço normal e condição de pagamento:
#-A vista dinheiro/cheque: 10% de desconto
#-A vista no cartão: 5% de desconto
#-Em até 2x no cartão: preço normal
#-3x ou mais no cartão: 20% de juros
from time import sleep
preço = float(input('Digite o valor do produto: R$'))
print('Qual a forma de pagamento?')
pagamento = int(input('{}[1] A vista dinheiro/cheque{} \n{}[2] A vista no cartão{} \n{}[3] Em até 2x no cartão{} \n{}[4] 3x ou mais no cartão{}\n'.format('\033[36m', '\033[m', '\033[35m', '\033[m', '\033[32m', '\033[m', '\033[33m', '\033[m')))
print('{}\nCARREGANDO...\n{}'.format('\033[7m', '\033[m'))
sleep(3)
print('Preço do produto: {}R${:.2f}{}'.format('\033[34m', preço, '\033[m'))
if pagamento == 1:
    print('Forma de pagamento: {}A vista dinheiro/cheque{}'.format('\033[33m', '\033[m'))
    print('Desconto de {}10% aplicado{} (-R${:.2f})'.format('\033[32m', '\033[m', (preço * 0.1)))
    print('Total a pagar: {}R${:.2f}{}'.format('\033[1;35m', (preço - (preço*0.1)), '\033[m'))
elif pagamento == 2:
    print('Forma de pagamento: {}A vista no cartão{}'.format('\033[33m', '\033[m'))
    print('Desconto de {}5% aplicado{} (-R${:.2f})'.format('\033[32m', '\033[m', (preço * 0.05)))
    print('Total a pagar: {}R${:.2f}{}'.format('\033[1;35m', (preço - (preço*0.05)), '\033[m'))
elif pagamento == 3:
    print('Forma de pagamento: {}Em até 2x no cartão{}'.format('\033[33m', '\033[m'))
    print('Total a pagar: {}R${:.2f}{}'.format('\033[1;35m', preço, '\033[m'))
elif pagamento == 4:
    print('Forma de pagamento: {}3x ou mais no cartão{}'.format('\033[33m', '\033[m'))
    print('Juros de {}20% aplicado{} (+R${:.2f})'.format('\033[31m', '\033[m', (preço * 0.2)))
    print('Total a pagar: {}R${:.2f}{}'.format('\033[1;35m', (preço + (preço*0.2)), '\033[m'))
else:
    print('Opção inválida. Tente novamente.')
    