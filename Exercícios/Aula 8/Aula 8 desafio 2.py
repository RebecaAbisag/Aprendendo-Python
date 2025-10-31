#import math
#c1=float(input ('Qual o valor do Cateto oposto ?'))
#c2=float(input('Qual o valor do cateto adjascente ?' ))
#r = (c1**2)+(c2**2)
#r2 = math.sqrt(r)
#print ('O Resultado da hipotenusa {}'.format (r2))
import math
c1=float(input ('Qual o valor do cateto oposto ?'))
c2=float(input('Qual o valor do cateto adjascente ?' ))
r2 = math.hypot(c1,c2)
print ('O Resultado da hipotenusa {}'.format (r2))

