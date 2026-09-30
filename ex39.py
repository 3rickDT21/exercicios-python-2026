num=int(input("Digite um número menor que 1000:"))
# decompondo_numero = num/100
# decompondo_numero_10 = num/10
# print(decompondo_numero)
# print(decompondo_numero_10)
print(f'{int(num/100)} centenas')
print(f'{int((num/10)%10)} dezenas')
print(f'{int((num%10))} unidade')

if num >= 1000:
    print("O número deve ser menor q 1000!")

