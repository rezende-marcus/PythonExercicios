km = float(input('Quantos Km rodados? '))
dia = int(input('Por quantos dias foi alugado? '))
vkm = .15 * km
vdia = 60 * dia
soma = vkm + vdia

print('Preço total de Km rodado é R${:.2f}, preço total de diaria é R${:.2f}, total a pagar R${:.2f}'.format(vkm, vdia, soma))