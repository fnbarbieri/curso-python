from random import choice
nomes=input('Insira o nome dos alunos separados por vírgula: ')
alunos=nomes.split(',')
sorteado=choice(alunos)
print(f'O aluno sorteado foi {sorteado}.')