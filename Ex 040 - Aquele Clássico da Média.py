#Crie um programa que leia duas notas de um aluno e calcule sua 
#média, mostrando uma mensagem no final, de acordo com a média 
#atingida:
#-Média abaixo de 5.0: REPROVADO
#-Média entre 5.0 e 6.9: RECUPERAÇÃO
#-Média 7.0 ou superior: APROVADO
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print('{}REPROVADO{} \nMédia: {:.1f}'.format('\033[31m', '\033[m', media))
elif 5 <= media <= 6.9:
    print('{}RECUPERAÇÃO{} \nMédia: {:.1f}'.format('\033[33m', '\033[m', media))
else:
    print('{}APROVADO{} \nMédia: {:.1f}'.format('\033[32m', '\033[m', media))