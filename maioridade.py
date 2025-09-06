<<<<<<< HEAD
print('Verificando a Maioridade')

from datetime import date

soma_maioridade = 0
soma_menoridade = 0 

for c in range(0, 7):
    ano_nascimento=int(input('Digite o ano de nascimento: '))
    idade = date.today().year - ano_nascimento
    
    if idade >= 18:
        soma_maioridade += 1
    else:
        soma_menoridade += 1

=======
print('Verificando a Maioridade')

from datetime import date

soma_maioridade = 0
soma_menoridade = 0 

for c in range(0, 7):
    ano_nascimento=int(input('Digite o ano de nascimento: '))
    idade = date.today().year - ano_nascimento
    
    if idade >= 18:
        soma_maioridade += 1
    else:
        soma_menoridade += 1

>>>>>>> 9263dbb (Exercícios)
print(f'{soma_maioridade} pessoas atingiram a maioridade e {soma_menoridade} pessoas ainda não atingiram!')