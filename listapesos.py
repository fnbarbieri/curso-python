infos = []
pessoas = []
leve = pesado = 0
nome_leve = []
nome_pesado = []
while True:
    infos.append(str(input('Nome: ')))
    infos.append(float(input('Peso: ')))
    pessoas.append(infos[:])
    infos.clear()
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Deseja adicionar mais pessoas? [S/N] ').strip().upper()[0]
    if resposta == 'N':
        break

for p in pessoas:
    if p[1] <= 70.0:
        leve += 1
        nome_leve.append(p[0])
    elif p[1] >= 100.0:
        pesado += 1
        nome_pesado.append(p[0])

print(f'Foram cadastradas {len(pessoas)} pessoas, sendo que {leve} tem abaxo de 70kg ({nome_leve}) e {pesado} tem acima de 100kg ({nome_pesado}).')