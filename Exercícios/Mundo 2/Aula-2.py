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
            
        