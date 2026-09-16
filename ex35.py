area=int(input("Digite a Área a ser pintada (Em metros quadrados)"))

litros = area/3
latas = litros/18

if(latas * 18 < litros):
    latas = latas + 1

    valor = latas * 80

print(f"De acordo com a área {area}")
print(f"\nVocê precisará de: {latas} latas para pintar a área")
print(f"\nSubtotal de tintas")