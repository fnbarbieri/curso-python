exp=input('Digite a expressão: ')
parenteses = []

for simbolo in exp:
    if simbolo == '(':
        parenteses.append('(')
    elif simbolo == ')':
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append(')')
            break

if len(parenteses) == 0:
    print('Expressão válida.')
else:
    print('Expressão inválida.')