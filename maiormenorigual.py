print('Comparação Numeral: maior, menor ou igual?')
n1=float(input('Insira o primeiro valor: '))
n2=float(input('Insira o segundo valor: '))

if n1 > n2:
    print(f'O primeiro valor ({n1}) é maior que o segundo valor ({n2}).')
elif n2 > n1:
    print(f'O segundo valor ({n2}) é maior que o primeiro valor ({n1}).')
else:
    print(f'Os valores {n1} e {n2} são iguais.')