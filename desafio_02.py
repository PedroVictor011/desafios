import random

opcoes = ['pedra','papel','tesoura']

escolha_maquina = random.choice(opcoes)

print(escolha_maquina)

escolha_jogador  = input('escolha pedra,papel ou tesoura:')

if escolha_maquina == escolha_jogador :
    print(f'Deu Empate o computador escolheu {escolha_maquina}.')

elif escolha_jogador == 'pedra' and escolha_maquina == 'tesoura' :
    print( f'Voce Ganhou o computador escolheu {escolha_maquina}.')

elif escolha_jogador == 'papel' and escolha_maquina == 'pedra' :
    print( f'Voce Ganhou o computador escolheu {escolha_maquina}.')

elif escolha_jogador == 'tesoura' and escolha_maquina == 'papel' :
    print( f'Voce Ganhou o computador escolheu {escolha_maquina}.')

elif escolha_jogador != 'pedra' or 'papel' or 'tesoura':
    print('erro escolha uma opção valida.')
else:
    print(f'Voce perdeuo computador escolheu {escolha_maquina}. ')