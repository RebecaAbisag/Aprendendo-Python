numero = int(input('Informe um numero'))
#n = str(numero)
#print('Analisando o numero {}...'.format(numero))
#print ('Ele possui {} unidade'.format(n[3]))
#print ('Ele possui {} dezena'.format(n[2]))
#print ('Ele possui {} centena'.format(n[1]))
#print ('Ele possui {} milhar'.format(n[0]))
u = numero//1 % 10
d = numero//10 % 10
c = numero//100 % 10
m = numero//1000 % 10
print('Analisando o numero {}...'.format(numero))
print ('Ele possui {} unidade'.format(u))
print ('Ele possui {} dezena'.format(d))
print ('Ele possui {} centena'.format(c))
print ('Ele possui {} milhar'.format(m))
