<<<<<<< HEAD
#A medida de qualquer um dos lados deve ser SEMPRE MENOR do que a soma das medidas dos outros dois lados.
print('Verificação - Triângulo')
reta1=float(input('Valor da primeira reta: '))
reta2=float(input('Valor da segunda reta: '))
reta3=float(input('Valor da terceira reta: '))

if (reta1 < reta2 + reta3) and (reta2 < reta1 + reta3) and (reta3 <reta1 + reta2):
    print('Triangulo formado!')
    if reta1 == reta2 == reta3:
        print('Esse é um triângulo equilátero!')
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print('Esse é um triângulo isóceles.')
    else:
        print('Esse é um triângulo escaleno.')
else:
=======
#A medida de qualquer um dos lados deve ser SEMPRE MENOR do que a soma das medidas dos outros dois lados.
print('Verificação - Triângulo')
reta1=float(input('Valor da primeira reta: '))
reta2=float(input('Valor da segunda reta: '))
reta3=float(input('Valor da terceira reta: '))

if (reta1 < reta2 + reta3) and (reta2 < reta1 + reta3) and (reta3 <reta1 + reta2):
    print('Triangulo formado!')
    if reta1 == reta2 == reta3:
        print('Esse é um triângulo equilátero!')
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print('Esse é um triângulo isóceles.')
    else:
        print('Esse é um triângulo escaleno.')
else:
>>>>>>> 9263dbb (Exercícios)
    print('Não é possível formar um triângulo com essas retas.')