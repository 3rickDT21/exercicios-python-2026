mat=(input("Qual é a matéria?"))
nt1=int(input("Qual a nota do primeiro bimestre?"))
nt2=int(input("Qual a nota do segundo bimestre?"))
nt3=int(input("Qual a nota do terceiro bimestre?"))
nt4=int(input("Qual a nota do quarto bimestre?"))

media = (nt1 + nt2 + nt3 + nt4) /4

if media >= 7:
    print(f"Você foi aprovado e teve uma média de {media} na matéria {mat}")
else:
    print(f"Você foi reprovado e teve uma média de {media} na matéria {mat}")
