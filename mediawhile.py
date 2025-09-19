valores_inseridos = []

while True:
    valores=int(input('Digite um valor: '))
    valores_inseridos.append(valores)
    resposta=input('Você deseja digitar mais um valor? [S/N]: ').strip().upper()[0]
    
    if resposta == 'S':
        continue
    elif resposta == 'N':  
        break

soma = sum(valores_inseridos)
media = soma / len(valores_inseridos)
maior = max(valores_inseridos)
menor = min(valores_inseridos)
print(f'A média dos valores digitados é igual a {media} e o maior valor inserido foi {maior} e o menor foi {menor}.')