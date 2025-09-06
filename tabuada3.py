<<<<<<< HEAD
while True:
    print('--' * 24)
    valor = int(input('Digite o valor de qual deseja saber a tabuada: '))
    if valor < 0:
        print('Programa encerrado!')
        break
    elif valor >= 0:
        for c in range (1, 11):
            resultado = valor * c
=======
while True:
    print('--' * 24)
    valor = int(input('Digite o valor de qual deseja saber a tabuada: '))
    if valor < 0:
        print('Programa encerrado!')
        break
    elif valor >= 0:
        for c in range (1, 11):
            resultado = valor * c
>>>>>>> 9263dbb (Exercícios)
            print(f'{valor} x {c} = {resultado}')