n1=float(input('Insira o primeiro número: '))
n2=float(input('Insira o segundo número: '))
n3=float(input('Insira o terceiro número: '))

maior = n1

if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3

menor = n1

if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

print(f'Dentre os números {n1, n2, n3}, o maior é o número {maior} e o menor é o número {menor}.')