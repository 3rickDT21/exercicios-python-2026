#1: Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;

#2: Se o delta calculado for negativo, a equação não possui raízes reais. Informe ao usuário e encerre o programa;

#3: Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe ao usuário;

#4: Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;


import math

while(True):

    a=int(input("Digite o valor de a\n: "))
	
    b=int(input("Digite o valor de b\n"))

    c=int(input("Digite o valor de c\n: "))

    if (a == 0):
        print("A equação não é de segundo grau!")
    break


