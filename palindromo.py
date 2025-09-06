<<<<<<< HEAD
print('Verificação de Palíndromo')
pontuacao=(".,!?- ")
palavra=(str(input('Digite a palavra a ser analisada (sem acentuação): '))).strip().lower()
for i in pontuacao:
    palavra = palavra.replace(i, '')

if palavra == palavra[::-1]:
    print(f'A palavra/frase {palavra} é um palíndromo!')
else:
=======
print('Verificação de Palíndromo')
pontuacao=(".,!?- ")
palavra=(str(input('Digite a palavra a ser analisada (sem acentuação): '))).strip().lower()
for i in pontuacao:
    palavra = palavra.replace(i, '')

if palavra == palavra[::-1]:
    print(f'A palavra/frase {palavra} é um palíndromo!')
else:
>>>>>>> 9263dbb (Exercícios)
    print(f'A palavra/frase {palavra} não é um palíndromo!')