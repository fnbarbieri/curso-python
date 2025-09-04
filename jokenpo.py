from random import randint
opcoes=('🪨', '📜', '✂️')
computador=randint(0, 2)

jogador=int(input('[0] 🪨\n[1] 📜 \n[2] ✂️ \nFaça sua jogada: '))
print(f'Minha jogada foi {opcoes[computador]}!\nA sua foi {opcoes[jogador]}!')

if computador == 0:
    if jogador == 0:
        print(f'Empate!')
    elif jogador == 1:
        print(f'Você venceu!')
    elif jogador == 2:
        print(f'Eu venci!')
    else:
        print(f'Opção inválida!')
if computador == 1:
    if jogador == 0:
        print(f'Eu venci!')
    elif jogador == 1:
        print(f'Empate!')
    elif jogador == 2:
        print(f'Você venceu!')
    else:
        print(f'Opção inválida!')
if computador == 2:
    if jogador == 0:
        print(f'Você venceu!')
    elif jogador == 1:
        print(f'Eu venci!')
    elif jogador == 2:
        print(f'Empate!')
    else:
        print(f'Opção inválida!')