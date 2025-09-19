km=float(input('Quilometros percorridos: '))
dia=int(input('Dias de aluguel: '))
valor=((60*dia)+(0.15*km))
print(f'O valor a ser pago é R${valor:.2f}')