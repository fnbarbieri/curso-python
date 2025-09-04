print('Sequência de Fibonacci')

quantidade=int(input('Quantos valores da sequência de Fibonacci você deseja saber? '))

primeiro_termo = 0
segundo_termo = 1

print(f'{primeiro_termo}, {segundo_termo}', end=', ')

numero_termos = 3

while numero_termos <= quantidade:
    sequencia = primeiro_termo + segundo_termo
    print(f'{sequencia}', end=', ')
    primeiro_termo = segundo_termo
    segundo_termo = sequencia
    numero_termos += 1
print('Fim')