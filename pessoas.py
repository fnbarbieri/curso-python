soma_idades = 0
idade_mais_velho = 0
nome_mais_velho = ''
menor_20 = 0

for c in range(1, 5):
    print(f'-------Informações da {c}° Pessoa-------')
    nome=input('Nome: ')
    idade=int(input('Idade: '))
    sexo=input('Sexo [M/F]: ')

    soma_idades += idade

    if sexo in 'Mm':
        if idade > idade_mais_velho:
            idade_mais_velho = idade
            nome_mais_velho = nome

    if sexo in 'Ff' and idade < 20:
        menor_20 += 1

media = soma_idades / 4

print(f'A média das idades é igual a {media}.')
print(f'O homem mais velho tem {idade_mais_velho} anos e se chama {nome_mais_velho}')

if menor_20 > 1 or menor_20 == 0:
    print(f'{menor_20} mulheres tem menos de 20 anos.')
else:
    print(f'{menor_20} mulher tem menos de 20 anos.')