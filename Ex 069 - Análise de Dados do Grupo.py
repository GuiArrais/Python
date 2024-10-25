#Crie um programa que leie a idade e o sexo de várias pessoas. A 
#cada pessoa cadastrada, o programa deverá perguntar se o usuário 
#quer ou não continuar. No final, mostre:
#Quantas pessoas tem mais de 18 anos;
#Quantos homens foram cadastrados;
#Quantas mulheres tem menos de 20 anos.
cont = contIdade = contHomem = contMulher = 0
while True:
    print('\n')
    print('-'*30)
    print('Cadastre uma pessoa'.center(30))
    print('-'*30)
    cont += 1
    idade = int(input(f'Digite a {'\033[4;35m'}idade{'\033[m'} da {cont}ª pessoa: '))
    if idade >= 18:
        contIdade += 1
    sexo = input(f'Digite o {'\033[4;35m'}sexo{'\033[m'} da {cont}ª pessoa: {'\033[4;35m'}[M/F]{'\033[m'} ').upper().strip()[0]
    if sexo == 'M':
        contHomem += 1
    else:
        if idade < 20:
            contMulher += 1
    opção = input(f'Quer continuar? {'\033[4;35m'}[S/N]{'\033[m'} ').upper().strip()[0]
    if opção == 'N':
        break
print('-'*30)
print(f'Pessoas com mais de 18 anos: {'\033[36m'}{contIdade}{'\033[m'}')
print(f'Homens cadastrados: {'\033[36m'}{contHomem}{'\033[m'}')
print(f'Mulheres com menos de 20 anos: {'\033[36m'}{contMulher}{'\033[m'}')
