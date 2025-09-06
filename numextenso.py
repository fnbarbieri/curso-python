contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    try:
        numero=int(input('Digite um número de 0 a 20 para escrevê-lo por extenso: '))
        if 0 <= numero <=  20:
            print(contagem[numero])
            continuar=input('Deseja continuar? [S/N]: ').strip().upper()[0]
            if continuar in 'N':
                print('Programa encerrado.')
                break
        else:
            print('Número fora do intervalo. Tente novamente.')
    except ValueError:
        print('Entrada inválida. Tente novamente.')