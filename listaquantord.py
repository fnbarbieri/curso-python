valores = []
cont5 = 0
while True:
    n = int(input('Digite um valor: '))
    valores.append(n)
    if n == 5:
        cont5 +=1
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Deseja adicionar mais valores? [S/N] ').strip().upper()[0]
    
    if continuar == 'N':
        break

print(f'No total, foram digitados {len(valores)} números. Os valores em ordem decrescente: {sorted(valores, reverse=True)}. ', end='')

if 5 in valores:
    if cont5 == 1:
        print(f'O valor 5 foi digitado {cont5} vez.')
    if cont5 > 1:
        print(f'O valor 5 foi digitado {cont5} vezes.')
else:
    print('O valor 5 não foi digitado nenhuma vez.')