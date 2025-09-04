numero=int(input('Qual número você deseja saber se é par ou ímpar? '))
resto = numero % 2
if resto == 0:
    print(f'O número {numero} é par.')
else:
    print(f'O número {numero} é ímpar.')