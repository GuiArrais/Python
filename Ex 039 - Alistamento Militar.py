#Faça um programa que leia o ano de nascimento de um jovem e informe, 
#de acordo com sua idade:
#-Se ele ainda vai se alistar no serviço militar;
#-Se é a hora de se alistar;
#-Se já passou do tempo de alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que já 
#passou do prazo.
from datetime import date
ano = int(input('Digite o ano de nascimento: '))
idade = date.today().year - ano
if idade < 18:
    print('Idade: {}'.format(idade))
    print('Faltam {}{}{} ano(s) para o alistamento militar'.format('\033[4;36m', (18-idade), '\033[m'))
    anoAlist = date.today().year + (18-idade)
    print('Você vai se alistar em {}{}{}'.format('\033[35m', anoAlist, '\033[m'))
elif idade == 18:
    print('Idade: {}'.format(idade))
    print('É hora de se alistar.')
else:
    print('Idade: {}'.format(idade))
    print('Já passou do tempo de alistamento.\nJá se passaram {}{}{} ano(s)'.format('\033[4;36m', (idade-18), '\033[m'))
    anoAlist = date.today().year - (idade-18)
    print('Você deveria ter se alistado em {}{}{}'.format('\033[35m', anoAlist, '\033[m'))
