#This program says hello and asks for my name and my age

print('Hello, world!') #Mostra na tela o valor contido dentro dos parênteses; Python está chamando a função print() e o valor da variável está sendo passado para a função, o chamado argumento.
print('What is your name?')
myName = input() #Essa chamada de função é avaliada como uma string igual ao texto digitado pelo usuário, e a linha de código anterior atribui essa string à variável myName.
print('It is good to meet you, ' + myName)
print('The length of you name is: ')
print(len(myName)) #A função é avaliada para o valor inteiro correspondente ao número de caracteres dessa string.
print('What is your age?')
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.') #int(myAge) + 1 - converte myAge para um inteiro e soma 1.
#str(int(myAge) +1) - converte o resultado novamente para str para poder ser concatenado com o restante da frase