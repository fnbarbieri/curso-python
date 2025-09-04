from math import sin, cos, tan, radians
graus=float(input('Insira o valor do ângulo em graus: '))
radianos=radians(graus) #tranforma o valor inserido em graus para radianos (Python trabalha com valores em radianos)
print(f'O seno de {graus} é {sin(radianos):.2}, o cosseno é {cos(radianos):.2} e a tangente é {tan(radianos):.2}.')