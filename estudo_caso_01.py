"""
Crescimento da população brasileira: 1980 – 2016

Informações coletadas do DataSus

Criar um gráfico do crescimento da população brasileira, utilizando como
base de dados, o arquivo populacao_brasileira.csv, que se encontra na
pasta bd.
"""

import matplotlib.pyplot as plt

dados = open('bd/populacao_brasileira.csv').readlines()

x = []  # eixo x
y = []  # eixo y

for i in range(len(dados)):
    if i != 0:
        linha = dados[i].split(';')
        x.append(int(linha[0]))
        y.append(int(linha[1]))

plt.title('Crescimento da população brasileira: 1980 – 2016')
plt.xlabel('Ano')
plt.ylabel('População x 100.000.000')

plt.plot(x, y)
plt.bar(x, y, color='#e4e4e4')
# plt.show()

# Salvar a figura
plt.savefig('img/populacao_brasileira.png')
