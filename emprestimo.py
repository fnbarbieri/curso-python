print('Aprovação de Empréstimo Bancário')

valor_imovel=float(input('Por favor, insira o valor do imóvel R$'))
salario=float(input('Por favor, insira o valor do seu salário R$'))
numero_parcelas=int(input('Em quantas parcelas deseja pagar? '))

valor_parcelas = valor_imovel / numero_parcelas

if valor_parcelas <= salario*0.30:
    print(f'Seu empréstimo será pago em {numero_parcelas} vezes de R${valor_parcelas}')
else:
    print(f'O valor de R${valor_parcelas:.2f} excede 30% do seu salário, portanto, o empréstimo foi negado.')