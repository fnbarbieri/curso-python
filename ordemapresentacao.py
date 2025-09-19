from random import shuffle
nomes=input('Digite o nome dos alunos separados por vírgula: ')
alunos=nomes.split(',')
shuffle(alunos)
print(f'A ordem de apresentação é: {alunos}.')