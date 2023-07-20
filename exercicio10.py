#10.Escreva um algoritmo que calcule a média dos números
# digitados pelo usuário,se eles forem pares.Termine
# a leitura se o usuário digitar zero(0);

def calcularMedia():
    num1 = 1
    soma = 0
    contador = 0
while(num != 0):
    num = int(input('Informe um número: '))
    #Verifico se o número é par
    if(num % 2 == 0):
       soma += num #somando os pares
       contador += 1 #contando os pares

 return 'A média dos pares digitados é: {}' . format(soma/contador)








