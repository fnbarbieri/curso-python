sexo=str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]

while sexo not in 'MF':
    sexo=str(input('Dado inválido. Por favor, digite seu sexo [M/F]: ')).strip().upper()[0]
    
print('Informação registrada!\nPrograma finalizado.')