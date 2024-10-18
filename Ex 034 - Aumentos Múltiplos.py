#Escreva um programa que pergunte o salário de um funcionário e 
#calcule o valor de seu aumento.
#Para salários superiores a R$1250,00, calcule um aumento de 10%.
#Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Digite o valor do salário: R$'))
if salario > 1250:
    print('Aumento de 10% (R${:.2f}).\nNovo salário: R${:.2f}'.format((salario*0.1), salario+(salario*0.1)))
else:
    print('Aumento de 15% (R${:.2f}).\nNovo salário: R${:.2f}'.format((salario*0.15), salario+(salario*0.15)))