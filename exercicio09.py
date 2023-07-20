#9.Faça o mesmo que antes,porém,ao invés de ler
# 10 números,o programa deverá ler e somar números
# até que o valor digitado seja zero(0).

def somaAte0():
    num = 1
    soma = 0
    while(num != 0):
       num = int(input('Informe um número: '))
       soma += num
  return 'A soma dos números digitados é:{}' .format(soma)'