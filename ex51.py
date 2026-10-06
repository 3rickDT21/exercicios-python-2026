num=int(input("Digite um número para saber se ele é primo:"))

if num <= 1:
    print("Deve ser maior que 1!")
else:
    primo = True
    for i in range(2,num):
        if (num % i == 0):
            primo = False
            break
if primo:
    print("O número é Primo!")
else:
    print("O número não é Primo!")