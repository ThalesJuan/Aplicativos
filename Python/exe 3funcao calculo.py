def a(x1,y1):
    x = (x1-y1)**2
    return x
def b(x2,y2):
    y = (x2-y2)**2
    return y

x1 = float(input('Digite o valor de x1: '))
y1 = float(input('Digite o valor de y1: '))
x2 = float(input('Digite o valor de x2: '))
y2 = float(input('Digite o valor de y2: '))

r = (a(x1,y1)) + (b(x2,y2))
print (r)