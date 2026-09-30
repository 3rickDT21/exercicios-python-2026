#1: Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;

#2: Se o delta calculado for negativo, a equação não possui raízes reais. Informe ao usuário e encerre o programa;

#3: Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe ao usuário;

#4: Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;


import math

a=int(input("Digite o valor de a\n: "))
b=int(input("Digite o valor de b\n: "))
c=int(input("Digite o valor de c\n: "))

if(a != 0):
	delta = (b*b) - 4*a*c
	print("Delta=", delta,"\n")
	raiz_delta = math.sqrt(delta)
	if(delta == 0):
		x1 = ((-b + raiz_delta)/(2*a))
		print("X1 e X2 é",x1,"\n")
	elif (delta > 0):
		x1 = ((-b + raiz_delta)/(2*a))
		x2 = ((-b -raiz_delta) / (2*a))
		print(f"X1= {x1} \nX2= {x2}")
	elif (delta < 0):
		print("Não existe raízes reais!")
			
else:
	print("Não é equação do segundo grau!")