from exercicio04 import somarInteiro
from exercicio05 import tabuada
from exercicio05 import coletarPositivo
from exercicio06 import exercicio06
from exercicio07 import impares
from exercicio08 import somarInteiro
from exercicio09 import somarNumero
from exercicio10 import media
from vetores import preencherVetor
from vetores import consultarVetor
from exercício11 import
from exercício16 import eleicao


from exercício14 import mediaVolei
from exercício15 import miss

from vetores import apagarPosicao
def mostrarMenu():
    print('\n\n\nEscolha uma das opções abaixo: ' +
          '\n0. SAIR'         +
          '\n1. Exercício 01' +
          '\n2. Exercício 02' +
          '\n3. Exercício 03' +
          '\n4. Exercício 04' +
          '\n5. Exercício 05' +
          '\n6. Exercício 06' +
          '\n7. Exercício 07' +
          '\n8. Exercício 08' +
          '\n9. Exercício 09' +
          '\n10. Exercício 10' +
          '\n11. Exercício 11' +
          '\n12. Exercício 12' +
          '\n13. Exercício 13' +
          '\n14. Exercício 14' +
          '\n15. Exercício 15' +
          '\n16. Exercício 16' +
          '\n17. Exercício 17' +
          '\n18. Exercício 18' +
          '\n19. Exercício 19' +
          '\n20. Exercício 20'+
          '\n21. Preencher Vetor'+
          '\n22. Consultar Vetor' +
          '\n23. Apagar posição Vetor')

def operacao():
    opcao = 1 #Instanciar = Dar um valor inicial
    while(opcao != 0):
        # Chamar o método de cima
        mostrarMenu()
        #Coletar a opção do usuário
        opcao = int(input('Digite aqui o número da opção escolhida: '))

        #Executo a ação
        if(opcao == 0):
            #Instruções do exercício 01
            print('Obrigado!')
        elif(opcao == 1):
            return
        elif(opcao == 2):
            return
        elif(opcao == 3):
            return
        elif(opcao == 4):
            #Utilizar o exercício 04
            print('\nExercício 04')
            print(somarInteiro())
        elif(opcao == 5):
            #Exercício05
            print('\nExercício 05')
            num = int(input('Informe o número'))
            n = coletarPositivo()
            tabuada(num,n)
        elif(opcao == 6):
            # Exercício06
            print('\nExercício 06')
            inicio = int(input('Informe o início'))
            fim = int(input('Informe o fim'))
            exercicio06(inicio,fim)
        elif(opcao == 7):
            # Exercício07
            print('\nExercício 07')
            impares()
        elif(opcao == 8):
            # Exercício08
            print('\nExercício 08')
            print(somarInteiro())
        elif(opcao == 9):
            # Exercício09
            print(somarNumero())
            return
        elif(opcao == 10):
            # Exercício10
            print(calcularMedia())
        elif(opcao == 11):
            # Exercício11
            print(maiorMenor())
        elif(opcao == 12):
            # Exercício12
            print('\nExercício 12')
            print(positivoNegativo())
        elif(opcao == 13):
            print('\nExercício13')
            num = int(input('Informe um numero:'))
            print(fatorial(num))



        elif(opcao == 14):
            print('\nExercício14')
            print(mediaVolei())
        elif(opcao == 15):
            print('\nExercíco15')
            print(miss())
        elif(opcao == 16):
            print('Exercício16')
            print(eleicao())
        elif(opcao == 17):
            return
        elif(opcao == 18):
            return
        elif(opcao == 19):
            return
        elif(opcao == 20):
            return

        elif(opcao ==21):
            num = int(input('Informe o tamanho do vetor: '))
            preencherVetor(num)
        elif(opcao == 22):
            num = int(input(' Informe o tamanho do vetor: '))
            consultarVetor(num)
        elif(opcao == 23):
            posicao = int(input('Informe a posição que deseja apagar'))
            apagarPosicao(posicao-1)

        else:
            print('Opção escolhida não é válida, digite novamente!')