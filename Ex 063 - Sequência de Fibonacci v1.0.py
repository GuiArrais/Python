#Escreva um programa que leia um número n inteiro qualquer e mostre 
#na tela os n primeiros elementos de uma sequência de Fibonacci.
#0→1→1→2→3→5→8
cont = 0
f1 = 0
f2 = 1
num = int(input('Quantos números da sequência de Fibonacci você quer ver? '))
while cont < num:
    if cont != num-1:
        print(f1, end='→')
    else:
        print(f1)
    n = f1 + f2
    f1 = f2
    f2 = n
    cont = cont+1


    
