c = float(input('Informe a temperatura em Graus C:'))
#f = ((9 * c) / 5) + 32   seguindo a ordem de prescedencia, nao precisa do parentese
f = 9 * c / 5 + 32
print('Atemperarura de {} C corresponde a {} F!'.format(c, f))