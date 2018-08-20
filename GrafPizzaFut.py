import matplotlib.pyplot as plt

jogadores = list()

resp = 0
while resp <= 0:
    resp = int(input('Informe a quantidade de jogadores que são destros: '))
    jogadores.append(resp)

resp = 0
while resp <= 0:
    resp = int(input('Informe a quantidade de jogadores que são canhotos: '))
    jogadores.append(resp)

resp = 0
while resp <= 0:
    resp = int(input('Informe a quantidade de jogadores que são ambidestros: '))
    jogadores.append(resp)

# print(f'{jogadores}')

fig = plt.figure(figsize=(8,8))
ax = fig.gca()
tipo = ['Destros', 'Canhotos', 'Ambidestros']
ax.pie(jogadores, labels=tipo, autopct='%2.f')
plt.show()