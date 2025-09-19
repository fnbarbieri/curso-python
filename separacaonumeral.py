numero=input('Insira um valor entre 0 e 9999: ')
numero_formatado=numero.zfill(4)
print(f'milhar:{numero_formatado[0]}\ncenteza: {numero_formatado[1]}\ndezena: {numero_formatado[2]}\nunidade: {numero_formatado[3]}')

#numero=int(input('Insira um valor entre 0 e 9999: '))
#unidade=numero//1 % 10
#dezena=numero//10 % 10
#centena=numero//100 % 10
#milhar=numero//1000 % 10