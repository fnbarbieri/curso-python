infos = []
pessoas = []
maior = menor = 0
nome_menor = []
nome_maior = []
while True:
    infos.append(str(input('Nome: ')))
    infos.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = infos[1]
    else:
        if infos[1] > maior:
            maior = infos[1]
        if infos[1] < menor:
            menor = infos[1]
    pessoas.append(infos[:])
    infos.clear()
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Deseja adicionar mais pessoas? [S/N] ').strip().upper()[0]
    if resposta == 'N':
        break

for p in pessoas:
    if p[1] <= menor:
        nome_menor.append(p[0])
    elif p[1] >= maior:
        nome_maior.append(p[0])

print(f'{len(pessoas)} pessoas foram cadastradas. O maior peso foi de {maior}kg ({nome_maior}) e o menor foi de {menor}kg ({nome_menor}).')