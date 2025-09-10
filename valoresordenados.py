valores = []
for c in range(0, 5):
    n = int(input(f'Digite o {c+1}° valor: '))
    if c == 0 or n > valores[len(valores)-1]:
        valores.append(n)
    else:
        pos = 0
        while pos < len(valores):
            if n <= valores[pos]:
                valores.insert(pos, n)
                break
            pos += 1
print(f'Os valores digitados em ordem foram: {valores}')