n1=int(input("Digite o 1º lado:"))
n2=int(input("Digite o 2º lado:"))
n3=int(input("Digite o 3º lado:"))

if(n1+n2 > n3 and n1+n3 > n2 and n2+n3> n1):
  if (n1 != n2 and n1 != n3):
    print("Esse triângulo é escaleno! ")
  elif ( n1 == n2 and n1== n3 ):
    print("Esse triângulo é equilátero! ")
  else:
    print("Esse triângulo é isósceles! ")
else:
  print("OS LADOS INFORMADOS NÃO FORMAM UM TRIÂNGULO")