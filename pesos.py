<<<<<<< HEAD
print('Verificação de maior e menor peso')

maior = None
menor = None

for c in range(1, 6):
    peso=float(input(f'Digite {c}° o peso (Kg): '))

    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

=======
print('Verificação de maior e menor peso')

maior = None
menor = None

for c in range(1, 6):
    peso=float(input(f'Digite {c}° o peso (Kg): '))

    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

>>>>>>> 9263dbb (Exercícios)
print(f'O maior peso é {maior:.2f}Kg e o menor peso é {menor:.2f}Kg.')