l = []
s = 's'
while s in 'Ss':
    i = int(input('Digite um valor: '))
    s = input('Quer digitar outro valor ? (S/N): ')
    l.append(i)
l.sort()
print ('Ordem crescente:', l)