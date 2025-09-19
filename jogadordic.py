jogador = {}

jogador['Nome'] = input('Nome do Jogador: ')
jogador['Partidas'] = int(input(f'Quantas partidas {jogador['Nome']} jogou? '))

gols = []
for g in range(0, jogador['Partidas']+1):
    gols.append(int(input(f'Número de gols na {g}° partida: ')))

jogador['Gols'] = gols
jogador['Total de Gols'] = sum(gols)

print(f'O jogador {jogador['Nome']} jogou {jogador['Partidas']} partidas.')
for i, gols in enumerate(jogador['Gols']): #posso utilizar o enumarate pois jogador['Gols'] é uma lista dentro do dicionário jogador
    print(f'Na partida {i+1}, fez {gols} gols.')
print(f'Total de gols: {jogador['Total de Gols']}')