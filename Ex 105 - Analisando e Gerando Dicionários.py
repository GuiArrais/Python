#Faça um programa que tenha uma função notas() que pode receber 
#várias notas de alunos e vai retornar um dicionário com as 
#seguintes informações:
# Quantidade de notas
# A maior nota
# A menor nota
# A média da turma 
# A situação(opcional)
#Adicione também as docstrings da função
#resp = notas(5.5, 9.5, 10, 6.5, sit=True)
#print(resp)
def notas(*n,sit=False):
    """
    -> Função para analisar notaas e situações de vários alunos
    Args:
        n (float): uma ou mais notas dos alunos(aceita várias)
        sit (str): valor opcional indicando se deve ou não adcionar a situação
        return: dicionário com várias informações sobre a situação da turma
    """
    dados = {}
    dados['Quan_Notas'] = len(n)
    dados['maior'] = max(n)
    dados['menor'] = min(n)
    dados['media'] = sum(n) / len(n)
    
    if sit:
        if dados['media'] >= 7:
            dados['situação'] = 'Aprovado'
        elif 5 < dados['media'] < 7:
            dados['situação'] = 'Recuperação'
        else:
            dados['situação'] = 'Reprovado'
    return dados

    
#Programa Principal
resp = notas(5.5, 2.5, 1.5,sit=True)
print(resp)
help(notas)