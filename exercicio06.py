#6.  Faça um algoritmo que escreva na tela
# os números de um número inicial a um
# número final. Os números inicial e final
# devem ser informados pelo usuário;
def exercicio06(inicio, fim):
    if(inicio > fim):
        for i in range(inicio,fim-1, -1):
            print(i)
    else:
        for i in range(inicio, fim+1):
            print(i)
