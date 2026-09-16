n1=int(input("Digite o 1º número:"))
n2=int(input("Digite o 2º número:"))
op=input("Qual a operação desejada? [+] ou [-] ou [*] ou [/-]")

if op == "+":
    print("O resultado é", n1 + n2)
elif op == "-":
    print("O resultado é", n1 - n2)
elif op == "*":
    print("O resultado é", n1 * n2)
elif op == "/":
    print("O resultado é", n1 / n2 )
else:
    print("Operação ínvalida!") 