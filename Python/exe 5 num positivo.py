def div(n):
    s = 0
    for x in range(1, n-1):
        if n % x == 0:
            s += x
    print (s)

def demonstrativo(n):
    print(div(n))
  
for a in range(0, 5):
    while True:
        n = int(input('Escreva um número: '))
        if n < 0:
            print ('Digite um número maior que 0')
        else:
           demonstrativo(n)
           break
