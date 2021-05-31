from random import randint
computador = randint(0, 10)
print('Sou o seu computador... Acabei de pensarem em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual o foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu número? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Menos... Tente mais uma vez. ')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!!'.format(palpites))

