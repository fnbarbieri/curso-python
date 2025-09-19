from datetime import datetime
dados = {}

dados['Nome'] = input('Nome: ')
nascimento = int(input('Ano de nascimento: '))
dados['Idade'] = datetime.now().year - nascimento
dados['CTPS'] = int(input('Carteira de Trabalho (0 não possui): '))
if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: R$'))
    dados['Aposentadoria'] = dados['Idade'] + ((dados['Contratação'] + 35) - datetime.now().year)

print('-'*30)
for k, v in dados.items():
    print(f'{k}: {v}')