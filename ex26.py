n1=int(input("Digite um número:"))
n2=int(input("Digite um número: [ATÉ 10]"))

if(n1 == 1):
    print(f"O resultado é {n2}")
elif(n2 == 1):
    print(f"O resultado é {n1}")
elif(n2 == 2):
    print("O resultado é", n1*n1)
elif(n2 == 3):
    print("O resultado é", n1*n1*n1)
elif(n2 == 4):
    print("O resultado é", n1*n1*n1*n1)
elif(n2 == 5):
    print("O resultado é", n1*n1*n1*n1*n1)
elif(n2 == 6):
    print("O resultado é", n1*n1*n1*n1*n1*n1)
elif(n2 == 7):
    print("O resultado é", n1*n1*n1*n1*n1*n1*n1)
elif(n2 == 8):
    print("O resultado é", n1*n1*n1*n1*n1*n1*n1*n1)
elif(n2 == 9):
    print("O resultado é", n1*n1*n1*n1*n1*n1*n1*n1*n1)
elif(n2 == 10):
    print("O resultado é", n1*n1*n1*n1*n1*n1*n1*n1*n1*n1)
else:
    print("NÚMERO ÍNVALIDO, NÚMERO MÁXIMO É 10")