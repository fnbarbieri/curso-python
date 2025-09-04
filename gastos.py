lista_produtos = []
lista_preco = []
produtos_1000 = 0
produto_barato = ''
preco_barato=float('inf')

while True:
    produto=input('Nome do produto: ')
    lista_produtos.append(produto)
    preco=float(input('Preço do produto: '))
    lista_preco.append(preco)
    if preco > 1000:
        produtos_1000 += 1
    if preco < preco_barato:
        preco_barato = preco
        produto_barato = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar=input('Deseja cadastrar mais produtos? [S/N] ').strip().upper()[0]
    if continuar in 'N':
        break
total = sum(lista_preco)
barato = min(lista_preco)

print(f'O valor total dos produtos foi de R${total:.2f}. {produtos_1000} produtos custam mais de R$1000,00, e o produto mais barato foi {produto_barato} custando R${preco_barato:.2f}.')