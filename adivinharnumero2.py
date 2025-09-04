import random

tentativas = 1
computador = random.randint(0, 10)
jogador=int(input('De 0 até 10, em qual número eu estou pensando? '))

while jogador != computador:
    if jogador > computador:
        jogador=int(input(f'Menos... Tente novamente: '))
    elif jogador < computador:
        jogador=int(input(f'Mais... Tente novamente: '))
    tentativas += 1

print(f'Você acertou! Eu estava mesmo pensando no número {computador}.\nForam necessárias {tentativas} tentativas para você acertar!')