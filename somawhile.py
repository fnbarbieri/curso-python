print('Digite valores para serem somados e contabilizados. Digite 999 para sair do programa.')

valores_inseridos = []
contador = 0

while True:
    valores=int(input('Digite um valor: '))
    if valores == 999:
        break
    valores_inseridos.append(valores)
    contador += 1
    
soma = sum(valores_inseridos)
print(f'Foram digitados {contador} números, a soma entre eles é igual a {soma}.')