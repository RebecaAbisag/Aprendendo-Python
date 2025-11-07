#condições aninhadas pois esta em formato de ninho
#if carro.esquerda(): bloco 1
#elif carro.direita(): bloco 2 
#elif carro.ré(); bloco 3 
#else bloco4

nome = str(input('Qual é o seu nome?'))
if nome=="Filipe":
    print('Que nome bonito!')
elif nome =='Pedro' or nome =='Maria' or nome == 'Paulo':
    print ('Seu nome é bem comum no Brasil.')
elif nome in 'Ana Rebeca Claudia Jessica Juliana':
    print ('Que belo nome feminino!')    
else:
    print ('Seu nome é bem normal') 
print ('Tenha um bom dia, {}!'.format(nome))

#Aprendendo base numericas 
#notação posicional 
#numero Binario é um sistema numérico em que o valor de cada digito é determinado pela sua posição
# 0-0/ 1-1/2-10/3-11/4-100/5-101/6-110/7-111/8-1000/9-1001/10-1010/11-1011/12-1100/13-1101/14-1110/15-1111/16-10000/17-10001/18-10010/19-10011/20-10100
#Calculo para conversão de binario para decimal sempre o numero * 2 elevedo aos algaritmos de esquerda para direita diminuino(3,2,1,0)

#numero 1011 = (1*2^3)+(0*2^2)(1*2^1)+(1*2^0) 
# = (1*8)+(0*4)+(1*2)+(1*1)       
# = 8+0+2+1
# = 11(Decimal)

# numero 1100 = (1*2^3)+(1*2^2)+(0*2^1)+(0*2^0)
# = (1*8)+(1*4)+(0*2)+(0*1)
# = 8+4+0+0
# = 12 (Decimal)

# numero 1001 = (1*2^3)+(0*2^2)+(0*2^1)+(1*2^0)
# = (1*8)+(0*4)+(0*2)+(1*1)
# = 8+0+0+1
# = 9 (Decimal)

# numero 10011 =(1*2^3)+(0*2^3)+(0*2^2)+(1*2^1)+(1*2^0)
# = (1*16)(0*8)+(0*4)+(1*2)+(1*1)
# = 16+0+0+2+1
# = 19 (Decimal)

# numero 10001 =(1*2^3)+(0*2^3)+(0*2^2)+(0*2^1)+(1*2^0)
# = (1*16)(0*8)+(0*4)+(1*2)+(1*1)
# = 16+0+0+0+1
# = 17 (Decimal)


#Calculo para conversão de decimo para binario é dividir por 2 e pegar os restos 
# 13 = 13/2 = 6 (resto 1)
# 13 = 6/2 = 3 (resto 0)
# 13 = 3/2 = 1 (resto 1)
# 13 = 1/2 = 0 (resto 1)
# 13 = pegar os restos e tratar de trás pra frente (1101 na base 2)

# 15 = 15/2 = 7 (resto 1)
# 15 = 7/2 = 3 (resto 1)
# 15 = 3/2 = 1 (resto 1)
# 15 = 1/2 = 0 (resto 1)
#15 = 1111

#forma mais facil de descobrir pegar as potencias os e colocar 1 em somente o que da pra somar e da ele mesmo 
#13 decimal = 16+8+4+2+1
#13 decimal = 16(Não consta pois a soma não da 13)(8)+(4)(2 ultrapassa a soma)(+1)
#13 decimal = 8=1/4=1/2=0/1=1
#13 decimal = 1101

#14 = 16+8+4+2+1
#14 = Os numeros que podemos somar que 14 é 8+4+2
#14 = 1110

#40 = 32+16+8+4+2+1
#40 = 101000
#prova real 
#101000 = (1*32)+(0*16)+(1*8)+(4*0)(2*0)+(1*0)
#101000 = 32+0+8+0+0+0
#101000 = 40

#sistema octal e hexadecimal 
#sistema octal = 0 ao 7 
#hexadecimal = 0 ao 9 e A ao f (as letras representam o numero a=10 b=11 c=12....)
#calculo do sitema octal para encontrar o decimal
#371 = (3*8^2)+(7*8^1)(1*8^0)
#371= (3*64)+(7*8)(1*1)
#371 =192+56+1
#371 = 249 (decimal)

#1257 = (1*8^3)+(2*8^2)+(5*8^1)(7*8^0)
#1257= (1*512)+(2*64)+(5*8)(7*1)
#1257 =512+128+40+7
#1257 = 687 (decimal)

#calculo do sitema decimal para encontrar o octal

# 177 = 177/8 = 22 (resto 1)
# 177= 22/8 = 2 (resto 6)
# 177 = 2/8 = 0 (resto 2)
#177 = 261 BASE OCTAL



#calculo do sitema hexadecimal para encontrar o decimal 
#1FA = (1*16^2)+(F*16^1)(A*16^0)
#1FA = (1*256)+(F*16)(A*1)
#1FA = 256+240+10
#1FA = 506 (decimal)

#13C2 = (1*16^3)+(3*16^2)+(12*16^1)(2*16^0)
#1FA = (1*4096)+(3*256)+(12*16)(2*1)
#1FA = 4096+768+192+2
#1FA = 5058 (decimal)

#calculo do sitema decimal para encontrar o hexadecimal

# 685 = 685/16 = 42 (resto 13)(D)
# 685 =42/16 = 2 (resto 10)(A)
# 685 = 2/16 = 0 (resto 2)
# 685 = 2AD (BASE 16)



