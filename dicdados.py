from random import randint
from time import sleep
from operator import itemgetter

jogadas = {
    'Jogador 1': randint(1, 6),
    'Jogador 2': randint(1, 6),
    'Jogador 3': randint(1, 6),
    'Jogador 4': randint(1, 6)
}

print('-'*30)
print('Valores sorteados:')

for k, v in jogadas.items():
    print(f'{k} tirou o valor {v}')
    sleep(1)

ranking = ()
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)

print('-'*30)
print('Ranking dos vencedores:')

for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}')
    sleep(1)
print('-'*30)