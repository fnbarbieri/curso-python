import random
lista = []
jogos = []
quantidade = int(input('Número de jogos: '))
total = 1

while total <= quantidade:
    cont = 0
    while True:
        numero = random.randint(1, 61)
        if numero not in lista:
            lista.append(numero)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1

for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')