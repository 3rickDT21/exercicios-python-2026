n1=int(input("Digite o 1º número:"))
n2=int(input("Digite o 2º número:"))
n3=int(input("Digite o 3º número:"))

if(n1 > n2 and n2 > n3 and n1 > n3):
    print("O número", n1, "é maior")
if(n2 > n1 and n1 > n3 and n2 > n3):
    print("O número", n2, "é maior")
if(n3 > n1 and n2 > n1 and n3 > n2):
    print("O número", n3, "é maior")
if(n2 > n3 and n3 > n1 and n2 > n1):
    print("O número", n2, "é maior")
if(n1 > n2 and n3 > n2 and n1 > n3):
    print("O número", n1, "é maior")
if(n1 > n2 and n3 > n2 and n3 > n1):
    print("O número", n3, "é maior")
if(n1 > n2 and n3 > n2 and n1 > n3):
    print("O número", n1, "é maior")