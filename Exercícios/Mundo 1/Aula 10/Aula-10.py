#if (significa "se")
#bloco true(verdadeiro)
#else(significa "senão")
#bloco false(falso)
#sempre sera utilizado o verdadeiro ou o falso
#tempo = int(input('Quantos anos tem seu carro ?'))
#if tempo <= 3:
    #print ('Carro novo')
#else:
    #print('carro velho')
#print('FIM')
#condição simplifica
#tempo = int(input('Quantos anos tem seu carro ?'))
#rint('Carro novo' if tempo<3 else'Carro velho')
#print('FIM')
#nome = str(input('Qual é o seu nome?')).strip().upper()
#if nome == 'GUSTAVO':
 #   print('Qua nome lindo que você tem !')
#print ('Bom dia {}!'.format(nome))
n1 = float((input("Qual é a sua primeira nota")))
n2 = float((input("Qual é a sua segunda nota")))
m = (n1+n2)/2
print ('A sua média foi {}'.format(m))
if m >= 6:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')
