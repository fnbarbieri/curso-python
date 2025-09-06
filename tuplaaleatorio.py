from random import randint
numeros = tuple(randint(1, 10) for n in range(5))
print(f'Os números sorteados foram: {numeros}')
print(f'O maior número foi {max(numeros)} e o menor foi {min(numeros)}')