def pot(x,y):
    a = (x**y)
    return a

sair = 0
while (sair == 0):
    x = int(input('Digite o valor da base: '))
    y = int(input('Digite o valor do expoente: '))
    if (y <= 0):
        print ('Entre com o valor do expoente acima de 0')
    else:
        print (pot(x,y))

        sair = 1
