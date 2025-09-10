valores = []
for cont in range(0, 5):
    valores.append(int(input(f'Digite o {cont+1}° valor: ')))

maior_valor = max(valores)
menor_valor = min(valores)

print(f'O maior valor digitado foi {maior_valor} nas posições ', end='')
for i, v in enumerate(valores):
    if v == maior_valor:
        print(f'{i+1}...', end='')

print(f'\nO menor valor digitado foi {menor_valor} nas posições ', end='')
for i, v in enumerate(valores):
    if v == menor_valor:
        print(f'{i+1}...', end='')