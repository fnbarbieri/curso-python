matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = []
terceira = []
segunda = []
for l in range(0, 3):
    for c in range(0, 3):
        valor = int(input(f'Digite um valor para posição ({l+1}, {c+1}): '))
        matriz[l][c] = valor
        if valor % 2 == 0:
            pares.append(valor)
       
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

for l in range(0, 3):
    terceira.append(matriz[l][2])

for c in range(0, 3):
    segunda.append(matriz[1][c])
    

print(f'A soma dos valores pares digitados é igual a {sum(pares)}')
print(f'A soma dos valores da terceira coluna é igual a {sum(terceira)}')
print(f'O maior valor da segunda linha é {max(segunda)}')