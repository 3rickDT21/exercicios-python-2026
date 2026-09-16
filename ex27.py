nasc=int(input("Digite o ano que você nasceu:"))
atual=int(input("Digite o ano atual:"))

idade = atual - nasc
meses = idade * 12
dias = idade * 365
seman = dias / 7

print(f"Essa é a sua idade {idade} \nSua idade em meses {meses} \nSua idade em dias {dias} \nSua idade em semanas {seman}")