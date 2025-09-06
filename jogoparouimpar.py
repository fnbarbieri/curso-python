<<<<<<< HEAD
from random import randint
print('-' * 10)
print('Vamos jogar par ou ímpar!')
print('-' * 10)
vitorias = 0
while True:
    computador = randint(0, 10)
    usuario = int(input('Diga um valor: '))
    resultado = computador + usuario
    condicao = ' '
    while condicao not in 'PI':
        condicao = input('Par ou ímpar? [P/I]: ').strip().upper()[0]
    par = resultado % 2 == 0
    impar = resultado % 2 != 0
    if condicao in 'P' and par:
        print(f'Você jogou {usuario} e o computador jogou {computador}. A soma foi igual a {resultado} e é PAR. Você venceu!')
        print('Vamos jogar novamente...')
        vitorias += 1
    elif condicao in 'I' and impar:
        print(f'Você jogou {usuario} e o computador jogou {computador}. A soma foi igual a {resultado} e é ÍMPAR. Você venceu!')
        print('Vamos jogar novamente...')
        vitorias += 1
    elif condicao in 'I' and par:
        print(f'Você jogou {usuario} e o computador jogou {computador}. A soma foi igual a {resultado} e é PAR. Você perdeu e conseguiu vencer {vitorias} vezes!')
        break
    elif condicao in 'P' and impar:
        print(f'Você jogou {usuario} e o computador jogou {computador}. A soma foi igual a {resultado} e é ÍMPAR. Você perdeu e conseguiu vencer {vitorias} vezes!')
=======
from random import randint
print('-' * 10)
print('Vamos jogar par ou ímpar!')
print('-' * 10)
vitorias = 0
while True:
    computador = randint(0, 10)
    usuario = int(input('Diga um valor: '))
    resultado = computador + usuario
    condicao = ' '
    while condicao not in 'PI':
        condicao = input('Par ou ímpar? [P/I]: ').strip().upper()[0]
    par = resultado % 2 == 0
    impar = resultado % 2 != 0
    if condicao in 'P' and par:
        print(f'Você jogou {usuario} e o computador jogou {computador}. A soma foi igual a {resultado} e é PAR. Você venceu!')
        print('Vamos jogar novamente...')
        vitorias += 1
    elif condicao in 'I' and impar:
        print(f'Você jogou {usuario} e o computador jogou {computador}. A soma foi igual a {resultado} e é ÍMPAR. Você venceu!')
        print('Vamos jogar novamente...')
        vitorias += 1
    elif condicao in 'I' and par:
        print(f'Você jogou {usuario} e o computador jogou {computador}. A soma foi igual a {resultado} e é PAR. Você perdeu e conseguiu vencer {vitorias} vezes!')
        break
    elif condicao in 'P' and impar:
        print(f'Você jogou {usuario} e o computador jogou {computador}. A soma foi igual a {resultado} e é ÍMPAR. Você perdeu e conseguiu vencer {vitorias} vezes!')
>>>>>>> 9263dbb (Exercícios)
        break