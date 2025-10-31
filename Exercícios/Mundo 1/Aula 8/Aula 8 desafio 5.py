import random
a1 = input('Qual nome do primeiro Aluno ?')
a2 = input('Qual nome do segundo Aluno ?')
a3 = input('Qual nome do terceiro Aluno ?')
a4 = input('Qual nome do quarto Aluno ?')
ln = [a1, a2, a3, a4]
random.shuffle(ln)
print('O ordem da apresentação será{}!'.format(ln))
