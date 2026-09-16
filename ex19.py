
num1=int(input("Qual o primeiro número? "))
		
num2=int(input("Qual o segundo número? "))
		
num3=int(input("Qual o terceiro número? "))

if (num1 > num2 and num2 > num3):
		print("\n", num1, "\n",num2, "\n",num3)

elif (num1 > num2 and num3 > num2):
		print("\n", num1, "\n",num3, "\n",num2)

elif (num2 > num1 and num1 > num3):
		print("\n", num2, "\n",num1, "\n",num3)
		
elif num2 > num3 and num3 > num1:
		print("\n", num2, "\n",num3, "\n",num1)
		
elif num3 > num1 and num1 > num2:
		print("\n", num3, "\n",num1, "\n",num2)

else:
		print("\n", num3, "\n",num2, "\n",num1)