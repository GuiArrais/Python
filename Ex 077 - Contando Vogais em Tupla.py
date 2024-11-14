#Crie um programa que tenha uma tupla com várias palavras (não usar 
#acentos). Depois disso, você deve mostrar, para cada palavra, quais 
#são as suas vogais.
palavras = ('Aprender', 'Programar', 'Linguagem', 'Python',
         'Curso', 'Gratis', 'Estudar', 'Praticar',
         'Trabalhar', 'Mercado', 'Programador', 'Futuro')
vogais = 'aeiouAEIOU'
for c in palavras:
    print(f'Na palavra {'\033[4;33m'}{c.upper()}{'\033[m'} = ',end='',)
    for letra in c:
        if letra.upper() in 'AEIOU':
            print(letra.upper(),end=' ')
    print('')

