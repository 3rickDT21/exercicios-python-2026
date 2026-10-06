el = int (input("Qual o número total de eleitores: "))
i = 0
votoa = 0
votob = 0
votoc = 0

while (i<el):
    i = i+1
    resp= input("Quem você vai votar? [A]   [B]   [C]: ")[0].upper()

    if (resp == "A"):
        votoa=votoa+1

    elif(resp == "B"):
        votob=votob+1

    elif(resp == "C"):
        votoc=votoc+1
    else:
        print("OS votos foram nulos")


if (votoa > votob and votoa > votoc):
    print("O Candidato A, ganhou!")

elif (votob > votoa and votob > votoc):   
    print("O Candidato B, ganhou!")

elif (votoc > votoa and votoc > votob):
    print("O Candidato C, ganhou!")

else:

    if (votoa == votob ):
        print ("Empate entre Candidato A e B")

    elif (votoa == votob ):
        print ("Empate entre candidato A e C")

    else:
        print ("Empate entre candidato B e C")