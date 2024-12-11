#Crie um programa que tenha uma função chamada voto() que vai 
#receber como parâmentro o ano de nascimento de uma pessoa, 
#retornando um valor literal indicando se uma pessoa tem voto 
#NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
from datetime import date
def voto(ano):
    if 16 <= date.today().year - ano < 65:
        return 'Obrigatório'
    elif date.today().year - ano >= 65:
        return 'Opcional'
    else:
        return 'Negado'
        
    
anoNasc = int(input('Digite o ano de nascimento: '))
print(f'Idade: {date.today().year - anoNasc} anos')
print(f'Voto: {voto(anoNasc)}')