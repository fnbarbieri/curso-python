from datetime import date
print('Alistamento Obrigatório')
ano_nascimento=int(input('Insira o ano do seu nascimento: '))
idade = date.today().year - ano_nascimento
tempo_faltante = 18 - idade
tempo_atraso = idade - 18

if idade < 18:
    print(f'Você tem {idade} anos. Ainda não é hora de se alistar! Faltam {tempo_faltante} anos para o seu alistamento obrigatório. Será no ano de {date.today().year + tempo_faltante}.')
elif idade == 18:
    print(f'Você tem {idade} anos. Chegou o momento do seu alistamento obrigatório!')
else:
    print(f'Você tem {idade} anos. Já passou do prazo do seu alistamento! Seu atraso é de {tempo_atraso} anos. Alistamento deveria ocorrer no ano de {date.today().year - tempo_atraso}.')