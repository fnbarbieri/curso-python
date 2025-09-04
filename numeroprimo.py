divisores=0
print('Esse número é primo?')
numero=int(input('Digite o número: '))
for c in range(1, numero + 1):
    if numero % c == 0:
        divisores += 1
    
if divisores == 2:
    print(f'O número {numero} é primo!')
else:
    print(f'O número {numero} não é primo, pois possuí {divisores} divisores!')