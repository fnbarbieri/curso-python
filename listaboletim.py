ficha = []

while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = ' '
    while resp not in 'SN':
        resp = input('Adicionar mais alunos? [S/N]: ').strip().upper()[0]
    if resp in 'N':
        break
print(f'{"No.":<4}{"Nome":<10}{"Media":>8}')
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    opc = int(input('Mostrar notas de qual aluno? (Digite 999 para encerrar o programa): '))
    if opc == 999:
        print('Programa encerrado.')
        break
    if opc <= len(ficha) - 1:
            print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')