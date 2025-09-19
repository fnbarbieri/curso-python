print('Progressão Aritmética')
termo=int(input('Primeiro Termo: '))
razao=int(input('Razão da progressão: '))
for c in range (0, 10):
    termo_atual = termo + c * razao
    print(f'{termo_atual}', end=', ')