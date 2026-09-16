altura=float(input("Qual é a sua altura? "))

sex=str(input("Qual é o seu sexo? [H]Homem, [M]Mulher "))

hom = (72.7*altura) - 58
mul = (62.1*altura) - 44.7

if(sex == "H" or sex == "h"):
    print("Seu peso ideal é ", hom)

elif(sex == "M" or sex == "m"):
	print("Seu peso ideal é ", mul)
else:
	print("Digite um dos sexos acima! ")