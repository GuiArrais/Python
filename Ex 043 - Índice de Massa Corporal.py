#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
#calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
#-Abaixo de 18.5: Abaixo do peso
#-Entre 18.5 e 25: Peso ideal
#-25 até 30: Sobrepeso
#-30 a 40: Obesidade
#-Acima de 40: Obesidade mórbida
#IMC = peso / (altura^2)
peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))
imc = peso / (altura**2)
if imc < 18.5:
    print('IMC: {:.1f} \n{}Status:{} Abaixo do peso.'.format(imc, '\033[34m', '\033[m'))
elif imc >= 18.5 and imc < 25:
    print('IMC: {:.1f} \n{}Status:{} Peso ideal.'.format(imc, '\033[34m', '\033[m'))
elif imc >= 25 and imc < 30:
    print('IMC: {:.1f} \n{}Status:{} Sobrepeso.'.format(imc, '\033[34m', '\033[m'))
elif imc >= 30 and imc < 40:
    print('IMC: {:.1f} \n{}Status:{} Obesidade.'.format(imc, '\033[34m', '\033[m'))
else:
    print('IMC: {:.1f} \n{}Status:{} Obesidade mórbida.'.format(imc, '\033[34m', '\033[m'))