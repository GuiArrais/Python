#Faça um programa que leia o sexo de uma pessoa, mas só aceite os 
#valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente 
#até ter um valor correto.
sexo = input('Digite o sexo (M/F) da pessoa:\n').upper().strip()[0]
while sexo not in 'mMfF ':
    print('{}Sexo inválido. \nTente novamente.{}'.format('\033[31m', '\033[m'))
    sexo = input('Digite o sexo (M/F) da pessoa:\n').upper()
if sexo == 'M':
    print('Sexo {}masculino{} registrado com sucesso.'.format('\033[34m', '\033[m'))
if sexo == 'F':
    print('Sexo {}feminino{} registrado com sucesso.'.format('\033[35m', '\033[m'))
print('Fim do programa.')
    