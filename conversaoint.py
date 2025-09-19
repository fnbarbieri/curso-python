inteiro=int(input('Digite o número inteiro que deseja converter: '))
base=int(input('[1] Binário\n[2] Octal\n[3] Hexadecimal\nPara qual base deseja converter? '))

if base == 1:
    binario = bin(inteiro)
    print(f'O número {inteiro} em binário é igual a {binario[2:]}.')
elif base == 2:
    octal = oct(inteiro)
    print(f'O número {inteiro} em octal é igual a {octal[2:]}.')
elif base == 3:
    hexadecimal = hex(inteiro)
    print(f'O número {inteiro} em hexadecimal é igual a {hexadecimal[2:]}.')
else:
    print('Opção inválida. Tente novamente.')