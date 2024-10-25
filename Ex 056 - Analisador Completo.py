#Desenvolva um programa que leia nome, idade e sexo de 4 pessoas. No
#final do programa, mostre:
#A média de idade do grupo;
#Qual é o nome do homem mais velho;
#Quantas mulheres têm menos de 20 anos.
contIdade = 0
idadeAvançada = 0
contMulheres = 0
for c in range (0, 4):
    nome = input('Digite o {}nome{} da {}{}ª{} pessoa: '.format('\033[2;36m', '\033[m', '\033[33m', c+1, '\033[m'))
    idade = int(input('Digite a {}idade{} da {}{}ª{} pessoa: '.format('\033[2;36m', '\033[m', '\033[33m', c+1, '\033[m')))
    contIdade += idade
    print('Qual o sexo dessa pessoa?')
    sexo = int(input('{}[1] Masculino{} \n{}[2] Feminino{}\n'.format('\033[34m', '\033[m', '\033[35m', '\033[m')))
    if sexo == 1 and idadeAvançada < idade:
        idadeAvançada = idade
        velho = nome
    if sexo == 2 and idade < 20:
        contMulheres += 1

print('A média de idade é: {}{}{} anos'.format('\033[36m', contIdade/4, '\033[m'))
print('O homem mais velho tem {}{}{} anos e se chama {}{}{}'.format('\033[32m', idadeAvançada, '\033[m', '\033[36m', velho, '\033[m'))
print('Mulheres com menos de 20 anos: {}{}{}'.format('\033[36m', contMulheres, '\033[m'))

