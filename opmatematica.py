lista_valores = []

for n in range(1, 3):
    valor=int(input(f'Digite o {n}° valor: '))
    lista_valores.append(valor)

while True:
    print('[1] Somar\n[2] Multiplicar\n[3] Maior Valor\n[4] Digitar Novos Números\n[5] Sair do Programa')
    decisao=int(input('Qual opção você deseja?\n'))
    if decisao == 1:
        soma = sum(lista_valores)
        print(f'A soma dos valores {lista_valores[0]} e {lista_valores[1]} é igual a {soma}.')
    elif decisao == 2:
        multiplicacao = lista_valores[0] * lista_valores[1]
        print(f'A multiplicação dos valores {lista_valores[0]} e {lista_valores[1]} é igual a {multiplicacao}.')
    elif decisao == 3:
        if lista_valores[0] == lista_valores[1]:
            print(f'Os números são iguais.')
        else:
            print(f'Entre os valores {lista_valores[0]} e {lista_valores[1]}, o valor {max(lista_valores)} é o maior.')
    elif decisao == 4:
        lista_valores.clear()
        for n in range(1, 3):
            valor=int(input(f'Digite o {n}° valor: '))
            lista_valores.append(valor)
    elif decisao == 5:
        print('Programa encerrado.')
        break
    else:
        print('Opção inválida. Tente novamente.')