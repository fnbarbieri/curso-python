from random import randint
from time import sleep
numero=randint(0, 5)
entrada=int(input('De 0 a 5, adivinhe em qual número eu estou pensando: '))
print('Pensando...')
sleep(3)
if entrada == numero:
    print(f'Você acertou! Eu estava mesmo pensando no número {numero}.')
else:
    print(f'Errado! O número que eu estava pensando era {numero}.')