print('Calculo de IMC')
massa=float(input('Insira o valor da sua massa em kg: '))
altura=float(input('Insira o valor da sua altura em metros: '))

imc = massa / (altura ** 2)

if imc < 18.5:
    print(f'Seu IMC é de {imc:.2f} e você esta ABAIXO DO PESO.')
elif imc <= 25:
    print(f'Seu IMC é de {imc:.2f} e você esta com o PESO IDEAL.')
elif imc <= 30:
    print(f'Seu IMC é de {imc:.2f} e você esta com SOBREPESO.')
elif imc <= 40:
    print(f'Seu IMC é de {imc:.2f} e você esta com OBESIDADE.')
else:
    print(f'Seu IMC é de {imc:.2f} e você esta com OBESIDADE MÓRBIDA.')