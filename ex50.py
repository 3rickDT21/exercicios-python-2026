nu=int(input("Digite um número que deseja saber a Fatorial:"))


result=1
for i in range(1,nu+1):
    result = result*i
print(f'O fatorial de {nu}! é {result}')