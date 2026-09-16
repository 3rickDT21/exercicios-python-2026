sal=int(input("Qual é o seu salário? "))

bene = (sal *5 /100)

impos = (sal *7 /100)

print("Seu salário é de ", sal, " mas teve uma gratificação de ", bene, " porém, teve um imposto de ", impos,"\ne agora você tem ", sal + bene - impos)