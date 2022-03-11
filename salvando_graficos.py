import matplotlib.pyplot as plt

# Visualização de dados em Python

x = [1, 2, 3, 4, 5]
y = [2, 3, 7, 1, 0]
z = [200, 400, 600, 800, 1000]

titulo = 'Scatterplot: gráfico de dispersão'
eixox = 'Eixo X'
eixoy = 'Eixo Y'

# Legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

# Criar o gráfico
plt.scatter(x, y, label='Meus pontos', color='red', marker='.', s=z)
plt.plot(x, y, color='black', linestyle=':')

# Exibir o gráfico
plt.legend()
# plt.show()

# Salvando o gráfico gerado
# plt.savefig('figura1.png')
# plt.savefig('figura1.pdf')
plt.savefig('img/figura1.png', dpi=300)

