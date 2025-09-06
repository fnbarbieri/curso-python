<<<<<<< HEAD
from math import factorial

print('Vamos trabalhar com fatorial!')
valor = []

while True:
    valor.clear()
    numero=int(input('Digite o número do qual deseja saber o fatorial: '))
    fatorial=factorial(numero)
    c = numero
    while c > 0:
        print(f'{c}', end='')
        print(f' x ' if c > 1 else f' = {factorial(numero)}', end='')
        c -= 1
    continuar=input('\nDeseja digitar outro valor? [S/N]: ').strip().upper()[0]
    if continuar in 'S':
        continue
    else:
        print('Programa encerrado!')
        break


'''n=int(input('Digite um número para saber o seu fatorial: '))
c = n
while c > 0:
    print(f'{c}', end='')
    print(f' x ' if c > 1 else f' = {factorial(n)}', end='')
=======
from math import factorial

print('Vamos trabalhar com fatorial!')
valor = []

while True:
    valor.clear()
    numero=int(input('Digite o número do qual deseja saber o fatorial: '))
    fatorial=factorial(numero)
    c = numero
    while c > 0:
        print(f'{c}', end='')
        print(f' x ' if c > 1 else f' = {factorial(numero)}', end='')
        c -= 1
    continuar=input('\nDeseja digitar outro valor? [S/N]: ').strip().upper()[0]
    if continuar in 'S':
        continue
    else:
        print('Programa encerrado!')
        break


'''n=int(input('Digite um número para saber o seu fatorial: '))
c = n
while c > 0:
    print(f'{c}', end='')
    print(f' x ' if c > 1 else f' = {factorial(n)}', end='')
>>>>>>> 9263dbb (Exercícios)
    c -= 1'''