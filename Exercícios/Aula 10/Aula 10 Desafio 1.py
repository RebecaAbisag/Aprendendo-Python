import random
import emoji
print ((emoji.emojize('Vou pensar em numero entre 0 e 5. Tente adivinhar... :face_with_tears_of_joy:', language ='alias')))
inicio = 1
fim = 5
na = random.randint(inicio,fim)
nu =int(input(emoji.emojize('Em que numero eu pensei? :thinking_face:', language='alias')))
print (emoji.emojize('PROCESSANDO...:laptop:', language='alias'))
if na == nu:
    print(emoji.emojize(f'PARABÉNS :loudly_crying_face:! Eu pensei no numero {na} você conseguiu me vencer :pouting_face:!',language='alias'))
else:
    print (emoji.emojize(f'Eu GANHEI você perdeu :rolling_on_the_floor_laughing: ! Eu pensei no número {na} e não no {nu}!',language='alias'.format(na,nu)))



#input(emoji.emojize("Apreveite a aventura...:skull::ship::dagger::anchor: ",  language='alias'))