

print('Voce deve participar de uma contagem especial seguindo as regras do fizzbuzz')

print('As regras são: Se o numero for multiplo de 3 voce deve dizer a fizz')
print('Se numero for multiplo de 5 voce deve dizer buzz')
print('Se ele for multiplo de ambos voce deve dizer fizzbuzz')
print('se ele não for multiplo de 3 ou 5 voce deve digitar o numero continuando a contagem.')

for numero in range(1, 36):
        
        if numero % 3 == 0 and numero % 5 == 0:
            resposta_correta = 'fizzbuzz'
        elif numero % 3 == 0:
            resposta_correta = 'fizz'
        elif numero % 5 == 0:
            resposta_correta = 'buzz'
        else:
            resposta_correta = str(numero)

        resposta_usuario = input(f'O número é {numero}.A sua resposta e ?:')

        if resposta_usuario != resposta_correta:
         print(f'Resposta errada.A resposta correta era {resposta_correta}.')
         print("Fim de jogo!")
         break
else:
    print('Parabens voce ganhou.')
