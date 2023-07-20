# 7. Escrever um algoritmo que gera e
# escreve os números ímpares entre 100 e
# 200;
def impares():
    for i in range(100,201,1):
        if(i % 2 == 1):
            print(i)