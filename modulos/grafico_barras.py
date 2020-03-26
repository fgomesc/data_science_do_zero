from matplotlib import pyplot as plt

movies = ["Anie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

# barras possuem o tamnho padrao de 0.8, ebtai adicionaremos 0.1 as
# coordenadas a esquerda para que cada barra seja centralizada
xs = [i + 0.1 for i, _ in enumerate(movies)]

# As barras do gráfico com as coordenadas x a esquerda [xs], alturas [num_oscars]
plt.bar(xs, num_oscars)

plt.ylabel("# de Premiações")
plt.title("Meus Filmes Favoritos")

# nomeia o eixo x com nomes de filmes na barra central
plt.xticks([i + 0.5 for i, _ in enumerate(movies)], movies)

plt.show()