import matplotlib.pyplot as plt

# Visualização de dados em Python

x1 = [1, 2, 3, 4, 5]
y1 = [2, 3, 7, 1, 0]

x2 = [2, 4, 6, 8, 10]
y2 = [5, 1, 3, 7, 4]

# Legendas
titulo = 'Gráfico de barras'
eixox = 'Eixo X'
eixoy = 'Eixo Y'

# Legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

# Criar o gráfico
plt.bar(x1, y1, label='Grupo 1')  # barras
plt.bar(x2, y2, label='Grupo 2')  # barras

# Exibir o gráfico
plt.legend()
plt.show()
