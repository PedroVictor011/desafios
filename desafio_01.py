import random

numero_secreto = random.randint (1,20)

adivinhar = int(input('digite um numero entre 1 e 20:'))

while adivinhar != numero_secreto:
    
    if adivinhar > numero_secreto :
        print('o seu numero e menor')
        adivinhar = int(input('digite um numero entre 1 e 20:'))
    elif adivinhar < numero_secreto:
        print('o seu numero e maior.')
        adivinhar = int(input('digite um numero entre 1 e 20:'))
else:
    print('voce acertou')