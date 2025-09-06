<<<<<<< HEAD
print('Progressão Aritmética')

primeiro_termo=int(input('Primeiro termo: '))
razao=int(input('Razão: '))

termo_atual = primeiro_termo
contador = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while contador <= total:
        print(f'{termo_atual}', end=' -> ')
        termo_atual += razao
        contador += 1
    mais=int(input('\nQuantos termos você deseja mostrar a mais? '))
=======
print('Progressão Aritmética')

primeiro_termo=int(input('Primeiro termo: '))
razao=int(input('Razão: '))

termo_atual = primeiro_termo
contador = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while contador <= total:
        print(f'{termo_atual}', end=' -> ')
        termo_atual += razao
        contador += 1
    mais=int(input('\nQuantos termos você deseja mostrar a mais? '))
>>>>>>> 9263dbb (Exercícios)
print('Programa encerrado.')