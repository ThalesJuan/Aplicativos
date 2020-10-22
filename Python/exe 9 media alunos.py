def media(n1, n2, n3, n4):
    m = (n1 + n2 + n3 + n4)/4

def demonstrativo(re, n1, n2, n3, n4, m, nome):
    print ('Nome do aluno:', nome)
    print ('RE do aluno:', re)
    print ('Nota 1 do aluno:', n1)
    print ('Nota 2 do aluno:', n2)
    print ('Nota 3 do aluno:', n3)
    print ('Nota 4 do aluno:', n4)
    print ('Média do aluno:', m)
    if (m >= 7):
        print('Aluno aprovado!')
    elif (m < 7):
        print('Aluno de exame')

qntalunos = int(input('Quantidade de alunos: '))
for i in range(0, qntalunos):
    nome = input('Nome do aluno: ')
    re = float(input('RE do aluno: '))
    n1 = float(input('Nota 1 do aluno: '))
    n2 = float(input('Nota 2 do aluno: '))
    n3 = float(input('Nota 3 do aluno: '))
    n4 = float(input('Nota 4 do aluno: '))
    m = (n1 + n2 + n3 + n4)/4

    demonstrativo(re, n1, n2, n3, n4, m, nome)
