print('Soma de valores PARES.')
print('Digite os valores pares e inteiros que deseja somar: ')
soma = 0
contador = 0
for c in range(1, 7):
    numero_par=int(input(f'{c}° valor: '))
    if numero_par % 2 == 0:
        soma += numero_par
        contador += 1
print(f'A soma dos {contador} valores pares vale {soma}.')