seq=int(input("Qual o ídice que você quer saber na sequeência de Fibonacci"))

ant1=0
ant2=1
fib=0

print(ant1, end="\t")
print(ant2, end="\t")

for i in range(2,seq+1):
    fib = ant1 + ant2
    print(fib, end="\t")
    ant1 = ant2
    ant2 = fib