aluno = {}

aluno['Nome'] = input('Nome: ')
aluno['Média'] = float(input(f'Média de {aluno['Nome']}: '))

if aluno['Média'] < 5.0:
    aluno['Situação'] = 'Reprovado'
elif 5.0 <= aluno['Média'] < 7.0:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Aprovado'

print('-'*20)
for k, v in aluno.items():
    print(f'{k}: {v}')