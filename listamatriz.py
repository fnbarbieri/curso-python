matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        valor = int(input(f'Digite um valor para posição ({l+1}, {c+1}): '))
        matriz[l][c] = valor
    

    
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()