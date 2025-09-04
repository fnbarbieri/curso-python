from math import hypot
c_oposto=float(input('Valor do cateto oposto: '))
c_adjacente=float(input('Valor do cateto adjacente: '))
hipotenusa=hypot(c_oposto, c_adjacente)
print(f'A hipotenusa é igual a {hipotenusa:.2}.')