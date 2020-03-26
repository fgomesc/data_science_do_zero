from matplotlib import pyplot as plt

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [3300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

# Cria um gráfico de linha, anos no eixo x, gdp no eixo y
plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

# Adicionar um título
plt.title('GDP Nominal')

# Adicionar um selo no eixo y
plt.ylabel = ("Bilhoes $")
plt.show()