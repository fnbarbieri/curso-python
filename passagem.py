distancia=int(input('Qual a distância total da viagem em km? '))
if distancia <= 200:
    preco=0.50*distancia
else:
    preco=0.45*distancia
print(f'O valor da passagem será R${preco:.2f}')