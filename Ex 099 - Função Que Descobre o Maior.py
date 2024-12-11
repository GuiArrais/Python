#Faça um programa que tenha uma função chamada maior(), que receba 
#vários parâmetros com valores inteiros.
#Seu programa tem que analisar todos os valores e dizer qual deles 
#é o maior.
def maior(*num):
    print(f'Entre {num}, o maior número é {max(num)}')
    

maior(5,7,3,1,0,4)
maior(5,4,0,9,12)
maior(7,1,3,54,9)