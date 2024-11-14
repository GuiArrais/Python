#Crie um programa onde o usuário digite uma 
#expressão qualquer que use parênteses. Seu 
#aplicativo deverá analisar se a expressão passada
#está com os parênteses abertos e fechados na 
#ordem correta.
expressão = input('Digite a expressão:')
pilha = []
for símbolo in expressão:
    if símbolo == '(':
        pilha.append('(')
    elif símbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print(f'{'\033[32m'}Sua expressão está correta{'\033[m'}')
else: 
    print(f'{'\033[31m'}Sua expressão está errada{'\033[m'}')