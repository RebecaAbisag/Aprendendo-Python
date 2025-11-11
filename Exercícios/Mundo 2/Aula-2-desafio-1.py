import math
import emoji
import time

BoasVindas = emoji.emojize('')
print ('Bem vindo ao Banco Bobadilla, estou aqui para ajudar a financiar sua casa!\U0001F3E0 \U0001F600')
time.sleep(2)
print ('Para isso preciso de algumas informações...\U0001F914')
time.sleep(2)
casa = int(input("Qual o valor da casa?"))
salario = int(input("Qual o valor do seu salário?"))
parcelas = int(input("Quantas parcelas serão?"))
caselas = casa/parcelas 
porcentagem = caselas/salario * 100
print (f"Sua parcela é de R$ {caselas:.2f}, correspondente a {porcentagem:.2f}% do seu salário!")
time.sleep(3)
if porcentagem <= 30:
    print ('\u2705 Parabéns seu financiamento foi aprovado pois ele foi menor que 30%!\U0001F600')
else:
    print ('\u274c Seu emprestimo não foi aprovado, ele foi maior que 30% do seu salário, tente uma proxima!\U0001F622')
