<<<<<<< HEAD
print('Soma dos valores ÍMPARES de 1 a 500')
soma = 0
contador = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        contador += 1
        soma += c
=======
print('Soma dos valores ÍMPARES de 1 a 500')
soma = 0
contador = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        contador += 1
        soma += c
>>>>>>> 9263dbb (Exercícios)
print(f'A soma de todos os {contador} valores vale {soma}.')