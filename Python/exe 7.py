def pos(x):
    if (x > 0):
        print ('1')
    elif (x < 0):
        print ('-1')
    elif (x == 0):
        print ('0')

x = int(input('Digite um valor: '))
print (pos(x))
