import matplotlib.pyplot as plt

# Visualização de dados em Python

x = [1, 2, 3, 4, 5]
y = [2, 3, 7, 1, 0]

# Legendas
titulo = 'Gráfico de linhas'
eixox = 'Eixo X'
eixoy = 'Eixo Y'

# Título
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

# Criar o gráfico
plt.plot(x, y)  # linhas

# Exibir o gráfico
plt.show()
