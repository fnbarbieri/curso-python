m = 0
maioridade = 0
f_20 = 0
while True:
    idade=int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo=input('Sexo [F/M]: ').strip().upper()[0]
    if idade >= 18:
        maioridade += 1
    if sexo in 'M':
        m += 1
    if sexo in 'F' and idade < 20:
        f_20 += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar=input('Deseja cadastrar mais pessoas? [S/N]: ').strip().upper()[0]
    if continuar in 'N':
        break
print(f'Foram cadastradas {maioridade} pessoas com mais de 18 anos, {m} homens e {f_20} mulheres com menos de 20 anos.')