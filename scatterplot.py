import matplotlib.pyplot as plt

# Visualização de dados em Python

x = [1, 2, 3, 4, 5]
y = [2, 3, 7, 1, 0]

titulo = 'Scatterplot: gráfico de dispersão'
eixox = 'Eixo X'
eixoy = 'Eixo Y'

# Legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

# Criar o gráfico
plt.scatter(x, y, label='Meus pontos', color='r')
plt.plot(x, y)

# Exibir o gráfico
plt.legend()
plt.show()
