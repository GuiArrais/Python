#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "A";
#Em que posição ela aparece na primeira vez;
#Em que posição ela aparece na última vez.
frase = input('Digite uma frase qualquer: ').upper().strip()
print('Quantas vezes aparece a letra "A":', frase.count('A'))
print('Em que posição ela aparece na primeira vez:', frase.find('A')+1)
print('Em que posição ela aparece na última vez:', frase.rfind('A')+1)