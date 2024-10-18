#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi 
#multado.
#A multa vai custar R$7,00 por cada Km acima do limite.
vel = int(input('Qual a velocidade do carro: '))
if vel <= 80:
    print('Ok, tudo certo.')
else:
    print('Você ultrapassou o limite de 80Km/h.')
    print('Você será multado em R${:.2f}'.format((vel-80)*7))
