cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'quatorze',
        'quinze', 'dezeseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')
while True:
    num = int(input('Digite um número de 0 a 20: '))
    if 0 <= num <= 20:
        print(f'Você digitou o número {cont[num]}')
        resp = ' '
        while resp not in 'SN':
            resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
            if resp == 'N':
                break
    else:
        print('Tente novamente. ', end='')
#print(f'Você digitou o número {cont[num]}')

'''resp = ' '
while resp not in 'SN':
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break'''

    #print('Tente novamente. ', end='')
#print(f'Você digitou o número {cont[num]}')