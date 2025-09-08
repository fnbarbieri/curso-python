palavras = (
    'algoritmo',
    'software',
    'hardware',
    'inteligência artificial',
    'machine learning',
    'nuvem',
    'big data',
    'internet das coisas',
    'framework',
    'linguagem de programação',
    'memória',
    'rede',
    'servidor',
    'debug'
)
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos as vogais: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')