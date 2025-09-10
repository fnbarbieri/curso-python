valores = []

while True:
    valores.append(int(input('Digite um valor: ')))
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Deseja digitar mais valores? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break

par = []
impar = []
for valor in valores:
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)

print(f'Os valores digitados foram: {valores}, sendo {par} os valores pares e {impar} os valores ímpares.')