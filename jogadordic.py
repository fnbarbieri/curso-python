time = []
jogador = {}

while True:
    jogador.clear()
    jogador['Nome'] = input('Nome do Jogador: ')
    total_partidas = int(input(f'Quantas partidas {jogador['Nome']} jogou? '))

    gols = []
    for g in range(0, total_partidas):
        gols.append(int(input(f'Número de gols na {g+1}ª partida: ')))

    jogador['Gols'] = gols
    jogador['Total de Gols'] = sum(gols)
    time.append(jogador.copy())


    while True:
        resp = input('Cadastrar mais jogadores? [S/N] ').strip().upper()
        if resp in ['S', 'N']:
            break
        print('Erro. Responda apenas S ou N.')
    if resp == 'N':
        break

print('-=' * 25)

print(f'{"Cod":<4}{"Nome":<15}{"Gols":<20}{"Total":>6}')
print('-' * 50)

for k, v in enumerate(time):
    print(f'{k:<4}{v["Nome"]:<15}{str(v["Gols"]):<20}{v["Total de Gols"]:>6}')
print('-' * 50)

while True:
    try:
        busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    except ValueError:
        print('Erro. Por favor, digite um número válido.')
        continue

    if busca == 999:
        print("Encerrando...")
        break
    
    if busca >= len(time) or busca < 0:
        print(f'Erro. Não existe jogador com o código {busca}.')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[busca]['Nome']}:')
        for i, g in enumerate(time[busca]['Gols']):
            print(f'   => Na partida {i+1}, fez {g} gol(s).')
    print('-' * 50)