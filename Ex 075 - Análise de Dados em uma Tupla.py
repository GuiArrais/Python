#Desenvolva um programa que leia 4 valores pelo teclado e guarde-os 
#em uma tupla. No final, mostre:
#Quantas vezes apareceu o valor 9;
#Em que posição foi digitado o primeiro valor 3;
#Quais foram os números pares.
cont9 = pos3 = contPar = 0
print('Digite 4 valores inteiros')
tupla = (int(input('Primeiro número: ')),
        int(input('Segundo número: ')),
        int(input('Terceiro número: ')),
        int(input('Quarto número: ')))
print(tupla)
print(f'O número {'\033[1;36m'}9{'\033[m'} apareceu {'\033[1;36m'}{tupla.count(9)}{'\033[m'} vez(es)')
if 3 in tupla:
    print(f'O número {'\033[1;36m'}3{'\033[m'} foi digitado na {'\033[1;36m'}{tupla.index(3)+1}ª{'\033[m'} posição')
else:
    print(f'O número {'\033[1;36m'}3{'\033[m'} {'\033[1;31m'}NÃO{'\033[m'} foi digitado')
print('É par: ',end='')
for c in tupla:
     if c % 2 == 0:
          print(c,end=' ')