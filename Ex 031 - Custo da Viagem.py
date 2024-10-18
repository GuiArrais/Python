#Desenvolva um programa que pergunte a distância de uma viagem em Km. 
#Calcule o preço da passagem, cobrando R$0,50 por km para viagens de 
#até 200Km e R$0,45 para viagens mais longas.
d = int(input('Qual a distância da viagem: '))
if d <= 200:
    print('O preço da passagem da viagem de {}Kms custará R${:.2f}'.format(d, (d*0.5)))
else:
    print('O preço da passagem da viagem de {}Kms custará R${:.2f}'.format(d, (d*0.45)))