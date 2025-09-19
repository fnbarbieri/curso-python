#A medida de qualquer um dos lados deve ser SEMPRE MENOR do que a soma das medidas dos outros dois lados.
reta1=float(input('Valor da primeira reta: '))
reta2=float(input('Valor da segunda reta: '))
reta3=float(input('Valor da terceira reta: '))

if (reta1 < reta2 + reta3) and (reta2 < reta1 + reta3) and (reta3 <reta1 + reta2):
    print('Triangulo formado!')
else:
    print('Não é possível formar um triângulo com essas retas.')