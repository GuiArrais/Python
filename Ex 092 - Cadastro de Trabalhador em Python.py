#Crie um programa que leia nome, ano de nascimento e carteira de 
#trabalho e cadastre-os (com idade) em um dicionário se por acaso a 
#CTPS for diferente de zero, o dicionário receberá também o ano de 
#contratação e o salário. Calcule e acrescente, além da idade, com 
#quantos anos a pessoa vai se aposentar.
from datetime import date
dados = {}
cadastro = []
dados['nome'] = str(input('Nome: '))
anoNascimento = int(input('Ano de nascimento: '))
dados['idade'] = date.today().year - anoNascimento
dados['CTPS'] = int(input('N° da CTPS: '))
if dados['CTPS'] != 0:
    dados['anoContratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = (dados['anoContratação'] + 35)-anoNascimento
print('-'*30)
print(f'Nome: {dados['nome']}')
print(f'Idade: {dados['idade']}')
print(f'CTPS: {dados['CTPS']}')
if dados['CTPS'] != 0:
    print(f'Ano de contratação: {dados['anoContratação']}')
    print(f'Salário: R${dados['salário']:.2f}')
    print(f'Aposentadoria: {dados['aposentadoria']}',end=' anos')
