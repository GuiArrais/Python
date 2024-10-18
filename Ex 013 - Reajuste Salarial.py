#Faça um algoritmo que leia o salário de um funcionário e mostre seu 
#novo salário, com 15% de aumento.
salario = float(input('Digite o salário atual:\nR$'))
print('Acréscimo de 15% = R${:.2f}'.format(salario*0.15))
print('Novo salário: R${:.2f}'.format(salario+(salario*0.15)))