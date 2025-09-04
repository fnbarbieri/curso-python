print('Média entre duas notas')
nota1=float(input('Insira sua primeira nota: '))
nota2=float(input('Insira sua segunda nota: '))

media = (nota1 + nota2)/2

if media < 5.0:
    print(f'Sua média foi igual a {media}. Você está REPROVADO.')
elif 7 > media >= 5.0:
    print(f'Sua média foi igual a {media}. Você está de RECUPERAÇÃO.')
else:
    print(f'Sua média foi igual a {media}. Você está APROVADO.')