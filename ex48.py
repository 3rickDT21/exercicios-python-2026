pares = []
impares = []

for i in range(10):
    n = int(input(f"Digite o {i+1} número inteiro:"))

    if n % 2 == 0:
        pares.append(n)
    elif n % 2 == 1:
        impares.append(n)
        
print(f"\nQuantidade de números pares: {len(pares)}") 
print(f"\nQuantidade de números pares: {len(impares)}")                       