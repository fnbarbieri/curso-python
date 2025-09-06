<<<<<<< HEAD
print('Valor de Pagamento')

preco=float(input('Qual o valor do produto? R$'))
forma=int(input('[1] À vista (dinheiro ou cheque) - 10% de desconto \n[2] À vista (cartão) - 5% de desconto\n[3] Cartão (em 2x) - valor sem desconto\n[4] Cartão (3x ou mais) - 20% de acréscimo\nQual a forma de pagamento? '))

if forma == 1:
    preco = preco - (preco*0.10)
    print(f'O valor total do produto é R${preco:.2f}')
elif forma == 2:
    preco = preco - (preco*0.05)
    print(f'O valor total do produto é R${preco:.2f}')
elif forma == 3:
    preco = preco
    valor_parcela=preco/2
    print(f'O valor total do produto é R${preco:.2f} e será pago em 2 parcelas de R${valor_parcela:.2f}.')
elif forma == 4:
    preco = preco + (preco*0.20)
    parcela=int(input('Número de parcelas: '))
    valor_parcela=preco/parcela
    print(f'O valor total do produto é R${preco:.2f} e será pago em {parcela} vezes de R${valor_parcela:.2f}.')
else:
=======
print('Valor de Pagamento')

preco=float(input('Qual o valor do produto? R$'))
forma=int(input('[1] À vista (dinheiro ou cheque) - 10% de desconto \n[2] À vista (cartão) - 5% de desconto\n[3] Cartão (em 2x) - valor sem desconto\n[4] Cartão (3x ou mais) - 20% de acréscimo\nQual a forma de pagamento? '))

if forma == 1:
    preco = preco - (preco*0.10)
    print(f'O valor total do produto é R${preco:.2f}')
elif forma == 2:
    preco = preco - (preco*0.05)
    print(f'O valor total do produto é R${preco:.2f}')
elif forma == 3:
    preco = preco
    valor_parcela=preco/2
    print(f'O valor total do produto é R${preco:.2f} e será pago em 2 parcelas de R${valor_parcela:.2f}.')
elif forma == 4:
    preco = preco + (preco*0.20)
    parcela=int(input('Número de parcelas: '))
    valor_parcela=preco/parcela
    print(f'O valor total do produto é R${preco:.2f} e será pago em {parcela} vezes de R${valor_parcela:.2f}.')
else:
>>>>>>> 9263dbb (Exercícios)
    print('Essa opção não é válida.')