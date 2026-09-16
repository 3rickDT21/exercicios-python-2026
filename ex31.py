num = int(input("Digite um número para ver a tabuada:"))

print(f"\n-- TABUADA DO {num} ---\n")
i = 0


#for i in range(0, 11, 2): # range(start, stop+1, step)
for i in range(11): # range(start, stop+1, step)
    print(f'{num} X {i} = {num*i}' )