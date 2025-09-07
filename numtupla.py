numero = tuple((int(input(f'{n+1}° número: ')) for n in range(4)))
print(f'O número 9 apareceu {numero.count(9)} vezes.')
if 3 in numero:
    print(f'O número 3 está na {numero.index(3)+1}ª posição.')
else:
    print('O valor 3 não foi digitado nenhuma vez.')
print('Os valores pares foram:')
for n in numero:
    if n % 2 == 0:
        print(n, end=' ')