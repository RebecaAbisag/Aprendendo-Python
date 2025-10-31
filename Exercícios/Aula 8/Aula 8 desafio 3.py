import math
an = float(input('Digite o angulo desejado'))
ang= math.radians(an)
sn = math.sin(ang)
cs = math.cos(ang)
tg = math.tan(ang)
print ('O referente ao angulo {}° o seno é de {:.2f}, o coseno {:.2f} e a tangente é de {:.2f}!'.format(an, sn, cs,tg))

