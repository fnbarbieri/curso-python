cantoras = (
    'Beyoncé',
    'Taylor Swift',
    'Whitney Houston',
    'Lady Gaga',
    'Rihanna',
    'Adele',
    'Madonna',
    'Mariah Carey',
    'Janet Jackson',
    'Katy Perry',
    'Britney Spears',
    'Christina Aguilera',
    'P!nk (Pink)',
    'Billie Eilish',
    'Ariana Grande',
    'Shakira',
    'Selena Gomez',
    'Miley Cyrus',
    'Dua Lipa',
    'Olivia Rodrigo'
)

print('-'*20)
print(f'As 20 cantoras pop mais premiadas são:')
for nome in cantoras:
    print(nome)
print('-'*20)
print(f'As 5 primeiras são:')
for nome in cantoras[0:5]:
    print(nome)
print('-'*20)
print(f'AS 4 últimas são:')
for nome in cantoras[-4:]:
    print(nome)
print('-'*20)
print('Em ordem alfabética:')
ordenado = sorted(cantoras)
for nome in ordenado:
    print(nome)
print('-'*20)
posicao_gaga = cantoras.index('Lady Gaga')
print(f'Lady Gaga está na posição {posicao_gaga + 1}ª posição.')
print('-'*20)