user = {}
users = []
soma = media = 0
while True:
    user.clear()
    user['Nome'] = input('Nome: ')
    while True:
        user['Sexo'] =  input('Sexo: [M/F] ').strip().upper()[0]
        if user['Sexo'] in 'MF':
            break
        print('Dado inválido. Digite apenas M ou F.')
    user['Idade'] = int(input('Idade: '))
    soma += user['Idade']
    users.append(user.copy())
    while True:
        resp = input('Deseja cadastrar mais usuários? [S/N]: ').strip().upper()[0]
        if resp in 'SN':
            break
        print('Dado inválido. Digite apenas S ou N.')
    if resp == 'N':
        break

print('-'*30)
print(f'Total de cadastros: {len(users)}')
media = soma / len(users)
print(f'Média das idades: {media:.2f}')
print(f'Mulheres cadastradas: ', end='')
for p in users:
    if p['Sexo'] == 'F':
        print(f'{p['Nome']}', end='. ')
print()
print('Pessoas com idade acima da média: ')
for p in users:
    if p['Idade'] >= media:
        for k, v in p.items():
            print(f'{k} = {v}', end=' ')