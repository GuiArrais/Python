#A Confederação Nacional de Natação precisa de um programa que leia 
#o ano de nascimento de um atleta e mostre sua categoria, de acordo 
#com a idade:
#-Até 9 anos: MIRIM
#-Até 14 anos: INFANTIL
#-Até 19 anos: JUNIOR
#-Até 20 anos: SENIOR
#Acima: MASTER
from datetime import date
ano = int(input('Digite o ano de nascimento: '))
idade = date.today().year - ano
if idade <= 9:
    print('Categoria: {}MIRIM{}'.format('\033[36m', '\033[m'))
elif idade <= 14:
    print('Categoria: {}INFANTIL{}'.format('\033[33m', '\033[m'))
elif idade <= 19:
    print('Categoria: {}JUNIOR{}'.format('\033[34m', '\033[m'))
elif idade == 20:
    print('Categoria: {}SENIOR{}'.format('\033[35m', '\033[m'))
else:
    print('Categoria: {}MASTER{}'.format('\033[31m', '\033[m'))