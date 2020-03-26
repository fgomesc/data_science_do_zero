from matplotlib import pyplot as plt


mentions = [500, 505]
years = [2013, 2014]

plt.bar([2016.6, 2013.6], mentions, 0.8)
plt.xticks(years)
plt.ylabel("# de vezes que ouvimos alguem dizer 'data sciences' ")

# se voce nao fizer isso, o matplotlib nomeará o eixo x de 0, 1
# e entao adiciona a +2.013e3 para fora do canto (matplotlib feio!)
plt.ticklabel_format(useOffset=False)

#enganar o eixo y mostra apenas a parte acima de 500
plt.axis([2012.5, 2014.5, 0, 506])
plt.title("Olhe o grande aumento!")
plt.show()