#14.Escreva um programa que leia um valor correspondente ao número de jogadores de
# um time de vôlei. O programa deverá ler uma altura para cada um dos jogadores e,
# ao final,informar a altura média do time.
from exercício05 import coletarPositivo



def mediaVolei():
    soma = 0
    qtde = int(input('Informe a quantidade de pessoas no time: '))
    #Coletar todos as alturas
    for i in range(qtde):
        altura = coletarPositivo()
        soma += altura
        return 'A altura média do time é {}'. format(soma/qtde)