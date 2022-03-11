# Boxplot - diagrama de caixa

import matplotlib.pyplot as plt
import random

vetor = []

# Populando o vetor com números aleatórios
for i in range(100):
    numero_aleatorio = random.randint(0, 50)
    vetor.append(numero_aleatorio)

# Criação do boxplot
plt.boxplot(vetor)

# Inserindo um titúlo no boxplot
plt.title('Boxplot')

# Exibição do boxplot
plt.show()
