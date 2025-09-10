valores = []

while True:
    n = int(input('Digite um valor: '))

    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valores repetidos serão mostrados apenas uma vez.')
    
    continuar = ' '
    while continuar not in 'SN':
        continuar=input('Deseja adicionar mais valores? [S/N] ').strip().upper()[0]

    if continuar == 'N':
        break

print(f'Os valores digitados foram: {sorted(valores)}')