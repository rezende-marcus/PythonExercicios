times = ('Corintians', 'Palmeiras', ' Santos', 'Gremio', 'Cruzeiro',
         'Flamengo', 'Vasco', ' Chapecoense', 'Atletico',
         'Botafogo', 'Atletico-PR', ' Bahia', 'São Paulo',
         'Fluminense', 'Sport Recife', 'Vitoria', 'Coritiba',
         'Avaí', 'Ponte Preta', 'Atletico-GO')
print('-=' * 15)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=' * 15)
print(f'Os 4 ultimos são {times[-4:]}')
print('-=' * 15)
#print(f'Times em ordem alfabética: {sdrted(times)}')
print(f'O Chapecoense esta na {times.index("Chapecoense")+1} posição')
