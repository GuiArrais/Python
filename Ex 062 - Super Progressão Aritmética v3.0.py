#Melhore o desafio 061, perguntando para o usuário se ele quer 
#mostrar mais alguns termos. O programa encerra quando ele disser 
#que quer mostrar 0 termos.
termos = 10
n = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão dessa PA: '))
while termos != 0:
    for c in range(0, termos):
        if c != termos-1:
            print(n, end=' → ')
        else:
            print(n)
        n += r
    termos = int(input('\nQuer mostrar mais alguns termos? Quantos? '))
print('{}Fim do programa{}'.format('\033[7m', '\033[m'))

