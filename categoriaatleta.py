<<<<<<< HEAD
from datetime import date
print('Confederação Nacional de Natação - Categoria')
ano_nascimento=int(input('Insira o ano do seu nascimento: '))
idade = date.today().year - ano_nascimento

if idade <= 9:
    print(f'Você tem {idade} anos e está na categoria MIRIM.')
elif idade <= 14:
    print(f'Você tem {idade} anos e está na categoria INFANTIL.')
elif idade <=19:
    print(f'Você tem {idade} anos e está na categoria JUNIOR.')
elif idade <= 25:
    print(f'Você tem {idade} anos e está na categoria SÊNIOR')
else:
=======
from datetime import date
print('Confederação Nacional de Natação - Categoria')
ano_nascimento=int(input('Insira o ano do seu nascimento: '))
idade = date.today().year - ano_nascimento

if idade <= 9:
    print(f'Você tem {idade} anos e está na categoria MIRIM.')
elif idade <= 14:
    print(f'Você tem {idade} anos e está na categoria INFANTIL.')
elif idade <=19:
    print(f'Você tem {idade} anos e está na categoria JUNIOR.')
elif idade <= 25:
    print(f'Você tem {idade} anos e está na categoria SÊNIOR')
else:
>>>>>>> 9263dbb (Exercícios)
    print(f'Você tem {idade} anos e está na categoria MASTER.')