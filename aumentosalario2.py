salario=float(input('Insira o valor do seu salário: R$'))

if salario > 1250:
    novo_salario = salario + (salario*0.10)
else:
    novo_salario = salario + (salario*0.15)
    
print(f'Seu novo salario é de R${novo_salario:.2f}')