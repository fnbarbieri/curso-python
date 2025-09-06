<<<<<<< HEAD
velocidade=int(input('Qual a velocidade do carro em km/h? '))
velocidade_limite=80
multa_km=7
if velocidade < velocidade_limite:
    print('Dentro do limite permitido (80km/h).')
else:
    km_acima=velocidade-velocidade_limite
    valor_multa=km_acima*multa_km
=======
velocidade=int(input('Qual a velocidade do carro em km/h? '))
velocidade_limite=80
multa_km=7
if velocidade < velocidade_limite:
    print('Dentro do limite permitido (80km/h).')
else:
    km_acima=velocidade-velocidade_limite
    valor_multa=km_acima*multa_km
>>>>>>> 9263dbb (Exercícios)
    print(f'Velocidade acima do limite permitido (80km/h). Você foi multado no valor de R${valor_multa:.2f}!')